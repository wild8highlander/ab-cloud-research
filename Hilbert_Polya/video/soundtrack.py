#!/usr/bin/env python3
"""Ambient soundtrack for 'Zeros & Gates' — 210 s, 48 kHz stereo WAV.
Layers: pad chords (Dm add9 / Bbmaj7 / F add9 / C add9), sub drone,
filtered noise swells, shutter clicks, zero chimes (pentatonic bells).
"""
import numpy as np
import wave

SR = 48000
DUR = 210.0
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(96)

L = np.zeros(N)
R = np.zeros(N)

# ---------------- helpers ----------------
def adsr(n, a, r, sus=1.0):
    env = np.ones(n) * sus
    na, nr = int(a * SR), int(r * SR)
    na, nr = min(na, n), min(nr, n)
    if na > 0:
        env[:na] = np.linspace(0, sus, na)
    if nr > 0:
        env[-nr:] = np.linspace(env[-nr] if n > nr else sus, 0, nr)
    return env

def add_tone(bufL, bufR, f0, t0, dur, amp, partials=((1, 1.0), (2, 0.35), (3, 0.14)), pan=0.0, detune=0.0015):
    n0, n1 = int(t0 * SR), min(int((t0 + dur) * SR), N)
    n0 = max(0, n0)
    if n1 <= n0: return
    tt = np.arange(n1 - n0) / SR
    env = adsr(n1 - n0, min(3.5, dur * 0.3), min(6.0, dur * 0.5))
    lfo = 1 + detune * np.sin(2 * np.pi * 0.11 * tt + rng.uniform(0, 6))
    sig = np.zeros(n1 - n0)
    for mul, amp_p in partials:
        sig += amp_p * np.sin(2 * np.pi * f0 * mul * lfo * tt + rng.uniform(0, 6))
    sig *= amp * env
    gl = np.cos((pan + 1) * np.pi / 4); gr = np.sin((pan + 1) * np.pi / 4)
    bufL[n0:n1] += sig * gl
    bufR[n0:n1] += sig * gr

def add_noise_swell(t0, dur, amp, f_lo=120, f_hi=1800, pan=0.0):
    n0, n1 = int(t0 * SR), min(int((t0 + dur) * SR), N)
    n0 = max(0, n0)
    if n1 <= n0: return
    m = n1 - n0
    noise = rng.normal(0, 1, m)
    spec = np.fft.rfft(noise)
    freqs = np.fft.rfftfreq(m, 1 / SR)
    band = (freqs >= f_lo) & (freqs <= f_hi)
    spec[~band] = 0
    spec *= 1 / np.sqrt(np.maximum(freqs, 1) / f_lo)
    sig = np.fft.irfft(spec, m)
    sig /= np.max(np.abs(sig)) + 1e-9
    env = adsr(m, dur * 0.45, dur * 0.45)
    sig *= amp * env
    gl = np.cos((pan + 1) * np.pi / 4); gr = np.sin((pan + 1) * np.pi / 4)
    L[n0:n1] += sig * gl; R[n0:n1] += sig * gr

def add_click(t0, amp=0.10, f=2600):
    n0 = max(0, int(t0 * SR))
    m = int(0.018 * SR)
    if n0 + m >= N: return
    noise = rng.normal(0, 1, m)
    tt = np.arange(m) / SR
    sig = noise * np.exp(-tt * 320) * np.sin(2 * np.pi * f * tt)
    sig *= amp / (np.max(np.abs(sig)) + 1e-9)
    L[n0:n0+m] += sig; R[n0:n0+m] += sig * 0.8

def add_chime(t0, f0, amp=0.16):
    dur = 2.2
    n0, n1 = int(t0 * SR), min(int((t0 + dur) * SR), N)
    n0 = max(0, n0)
    m = n1 - n0
    tt = np.arange(m) / SR
    sig = (np.sin(2*np.pi*f0*tt) + 0.42*np.sin(2*np.pi*f0*2.76*tt) + 0.18*np.sin(2*np.pi*f0*5.4*tt))
    sig *= np.exp(-tt * 2.1) * amp
    # simple echo
    echo = np.zeros(m)
    d = int(0.31 * SR)
    if m > d:
        echo[d:] = sig[:-d] * 0.34
    d2 = int(0.62 * SR)
    echo2 = np.zeros(m)
    if m > d2:
        echo2[d2:] = sig[:-d2] * 0.15
    sig = sig + echo + echo2
    L[n0:n1] += sig * 0.95; R[n0:n1] += sig * 1.0

# ---------------- 1. pad chords (2 loops of 4 chords x 26.25 s) ----------------
CHORDS = [
    ("Dm add9",  [73.42, 174.61, 220.0, 261.63, 329.63]),
    ("Bb maj7",  [58.27, 146.83, 220.0, 261.63, 349.23]),
    ("F add9",   [87.31, 174.61, 261.63, 392.0, 587.33]),
    ("C add9",   [65.41, 164.81, 196.0, 293.66, 392.0]),
]
seg = 26.25
for loop in range(2):
    for ci, (name, freqs) in enumerate(CHORDS):
        t0 = loop * 105.0 + ci * seg
        for fi, f in enumerate(freqs):
            amp = 0.055 if fi == 0 else 0.042
            pan = rng.uniform(-0.5, 0.5)
            add_tone(L, R, f, t0 - 1.5, seg + 3.0, amp * (1.0 - 0.08 * fi), pan=pan)

# sub drone throughout, breathing
drone_env = 0.06 + 0.02 * np.sin(2 * np.pi * t / 37.0)
sub = np.sin(2 * np.pi * 36.71 * t) + 0.5 * np.sin(2 * np.pi * 73.42 * t)
L += sub * drone_env * 0.9
R += sub * drone_env * 1.0

# ---------------- 2. noise swells at scene starts ----------------
for (ts, dur, amp) in [(0, 10, 0.05), (20, 8, 0.06), (50, 8, 0.07), (76, 8, 0.055),
                        (110, 10, 0.065), (160, 9, 0.06), (190, 12, 0.05)]:
    add_noise_swell(ts, dur, amp, pan=rng.uniform(-0.4, 0.4))

# ---------------- 3. shutter clicks (scenes 2 and 4) ----------------
rng_click = np.random.default_rng(77)
ttt = 20.0
while ttt < 49.0:
    if rng_click.random() < 0.55:
        add_click(ttt, amp=0.05, f=rng_click.uniform(2200, 3200))
    ttt += rng_click.uniform(0.55, 1.6)
ttt = 76.0
while ttt < 110.0:
    if rng_click.random() < 0.6:
        add_click(ttt, amp=0.045, f=rng_click.uniform(2400, 3400))
    ttt += rng_click.uniform(0.4, 1.1)

# ---------------- 4. zero chimes (prologue: first 5; montage: 24; spectrum: tail) ----------------
PENTA = [293.66, 329.63, 369.99, 440.0, 493.88, 587.33, 659.26, 739.99, 880.0, 987.77]
# prologue sparse
for i, ts in enumerate([3.0, 7.5, 11.5, 15.0, 18.0]):
    add_chime(ts, PENTA[i % len(PENTA)], 0.13)
# montage: zeros emerge 112 s → 158 s, 24 chimes accelerating
zs = np.linspace(112.0, 157.0, 24)
for i, ts in enumerate(zs):
    add_chime(ts, PENTA[i % len(PENTA)] * (1.0 if i < 12 else 2.0) / (1.0 if i < 12 else 2.0), 0.15)
# spectrum: arpeggio up
for i in range(8):
    add_chime(161.0 + i * 1.1, PENTA[(i + 3) % len(PENTA)], 0.11)
# epilogue: final two
add_chime(194.0, PENTA[0], 0.14)
add_chime(200.5, PENTA[0] * 2, 0.10)

# ---------------- 5. low pulse during "error" scene (scene 3) ----------------
ttt = 51.0
while ttt < 75.0:
    add_tone(L, R, 55.0, ttt, 0.9, 0.10, partials=((1, 1.0), (2, 0.2)), pan=rng.uniform(-0.3, 0.3))
    ttt += 2.6

# ---------------- 6. glitchy narrowband wobble in scene 3 (film burning) ----------------
n0, n1 = int(56 * SR), int(74 * SR)
m = n1 - n0
burn = rng.normal(0, 1, m)
spec = np.fft.rfft(burn)
freqs = np.fft.rfftfreq(m, 1/SR)
band = (freqs > 900) & (freqs < 2400)
spec[~band] = 0
burn = np.fft.irfft(spec, m)
burn /= np.max(np.abs(burn)) + 1e-9
burn_env = (np.sin(2*np.pi*0.7*np.arange(m)/SR) * 0.5 + 0.5) * 0.035
L[n0:n1] += burn * burn_env
R[n0:n1] += burn * burn_env * 0.8

# ---------------- master ----------------
fade_in = int(2.0 * SR); fade_out = int(6.0 * SR)
env = np.ones(N)
env[:fade_in] = np.linspace(0, 1, fade_in)
env[-fade_out:] = np.linspace(1, 0, fade_out)
L *= env; R *= env

peak = max(np.max(np.abs(L)), np.max(np.abs(R)))
L *= 0.85 / peak; R *= 0.85 / peak

data = np.zeros((N, 2))
data[:, 0] = L; data[:, 1] = R
pcm = (np.clip(data, -1, 1) * 32767).astype(np.int16)

with wave.open("video_audio.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())

print("audio written: 210 s, peak normalized")
