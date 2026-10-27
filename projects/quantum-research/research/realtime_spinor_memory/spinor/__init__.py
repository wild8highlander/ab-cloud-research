# -*- coding: utf-8 -*-
"""spinor — ядро вспомогательного исследования «машина без долговременной
памяти» (AB Cloud Quantum Research, research/realtime_spinor_memory).

Машина хранит ЕДИНСТВЕННЫЙ летучий регистр — спинорную фазу φ ∈ [0, 2π)
— и исполняет шаги в реальном времени: φ ← (φ + θ) mod 2π. Никакой
истории, никакого долговременного хранилища: состояние после сброса
не восстановимо, а стоимость шага не растёт со временем работы."""
from .core import MODELS, SpinorMachine, state_footprint
from .tasks import LogMachine, modular_counter

__all__ = ["MODELS", "SpinorMachine", "state_footprint",
           "LogMachine", "modular_counter"]
__version__ = "1.0.0"
