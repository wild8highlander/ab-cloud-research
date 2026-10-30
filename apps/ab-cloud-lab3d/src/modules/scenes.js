/**
 * scenes.js — the three 3D modules of the AB-Cloud laboratory (Three.js):
 *   1. Hofstadter lattice with vortices (Landau gauge + monumental atan
 *      phases; the GUE mechanism of the suite);
 *   2. Dirac cone (linear dispersion E(k)=±|k| at α=1/2, vortex q=+1);
 *   3. ζ critical strip (|ζ(σ+it)| surface, critical line + embedded zeros).
 */
'use strict';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { zeta, FIRST_ZEROS } from './zeta.js';

export function makeScene(container) {
  const width = container.clientWidth || 800;   // guard: 0-size host (hidden tab, CSS not applied yet)
  const height = container.clientHeight || 600;
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x000000);
  const camera = new THREE.PerspectiveCamera(50, width / height, 0.1, 500);
  camera.position.set(26, 20, 30);
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(width, height);
  // crisp on HiDPI/retina displays (cap at 2 to protect GPU memory)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  container.appendChild(renderer.domElement);
  // survive GPU process resets: without these listeners a lost context leaves
  // a permanently black canvas until a manual reload
  const onCtxLost = (e) => { e.preventDefault(); };
  const onCtxRestored = () => {
    // three.js re-uploads scene resources automatically on the next render
    renderer.render(scene, camera);
  };
  renderer.domElement.addEventListener('webglcontextlost', onCtxLost);
  renderer.domElement.addEventListener('webglcontextrestored', onCtxRestored);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  const ambient = new THREE.AmbientLight(0xffffff, 0.55);
  scene.add(ambient);
  const dir = new THREE.DirectionalLight(0xffffff, 1.1);
  dir.position.set(30, 40, 25);
  scene.add(dir);
  let raf = 0;
  const animate = () => {
    raf = requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  };
  animate();
  const lights = new Set([ambient, dir]); // never disposed
  const onResize = () => {
    const w = container.clientWidth, h = container.clientHeight;
    if (w > 0 && h > 0) { // guard: hidden/collapsed host would give NaN aspect
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    }
  };
  window.addEventListener('resize', onResize);
  // free GPU resources of a subtree (prevents context memory leak on rebuilds)
  const disposeDeep = (obj) => {
    obj.traverse?.((o) => {
      o.geometry?.dispose?.();
      if (Array.isArray(o.material)) o.material.forEach(m => m.dispose?.());
      else o.material?.dispose?.();
    });
  };
  return {
    scene, camera, renderer, controls,
    clear() {
      // remove everything EXCEPT the base lights; disposing GPU resources.
      // (the old count-based loop `length > 3` kept one stale group alive and
      //  accumulated scene content on every tab switch)
      for (let i = scene.children.length - 1; i >= 0; i--) {
        const c = scene.children[i];
        if (lights.has(c)) continue;
        scene.remove(c);
        disposeDeep(c);
      }
    },
    dispose() {
      cancelAnimationFrame(raf);
      window.removeEventListener('resize', onResize);
      this.clear();
      controls.dispose();
      renderer.domElement.removeEventListener('webglcontextlost', onCtxLost);
      renderer.domElement.removeEventListener('webglcontextrestored', onCtxRestored);
      renderer.dispose();
      renderer.forceContextLoss?.(); // release the GPU context promptly
      renderer.domElement.parentNode?.removeChild(renderer.domElement);
    },
  };
}

/* ---- module 1: Hofstadter lattice with vortices ---- */
export function buildHofstadter(s, L = 18, alpha = 0.5, nv = 4, seed = 96) {
  s.clear();
  // deterministic vortex placement (same convention as the Python port)
  let sd = seed;
  const rnd = () => (sd = (sd * 1103515245 + 12345) % 2147483648) / 2147483648;
  const vortices = [];
  for (let i = 0; i < nv; i++)
    vortices.push([1 + rnd() * (L - 1), 1 + rnd() * (L - 1)]);

  const group = new THREE.Group();
  const lineMat = new THREE.LineBasicMaterial({ color: 0x2c3e66 });
  const pts = [];
  for (let i = 0; i < L; i++) {
    for (let j = 0; j < L; j++) {
      pts.push(new THREE.Vector3(i, 0, j), new THREE.Vector3(i + 1, 0, j));
      pts.push(new THREE.Vector3(i, 0, j), new THREE.Vector3(i, 0, j + 1));
    }
  }
  group.add(new THREE.LineSegments(new THREE.BufferGeometry().
    setFromPoints(pts), lineMat));

  // site bars colored by the Landau phase 2πα·j
  const box = new THREE.BoxGeometry(0.22, 1, 0.22);
  for (let i = 0; i < L; i++) {
    for (let j = 0; j < L; j++) {
      const phase = (2 * Math.PI * alpha * (j + 1)) % (2 * Math.PI);
      const hue = phase / (2 * Math.PI);
      const m = new THREE.MeshBasicMaterial({ color: new THREE.Color().setHSL(hue, 0.75, 0.55) });
      const h = 0.4 + 0.9 * Math.abs(Math.sin(phase));
      const mesh = new THREE.Mesh(box, m);
      mesh.position.set(j, h / 2, i);
      mesh.scale.y = h;
      group.add(mesh);
    }
  }
  // vortex markers (flux tubes)
  const cone = new THREE.ConeGeometry(0.5, 1.6, 20);
  for (const [vx, vy] of vortices) {
    const m = new THREE.Mesh(cone, new THREE.MeshBasicMaterial({ color: 0xff5533 }));
    m.position.set(vy, 1.4, vx);
    group.add(m);
  }
  s.scene.add(group);
  s.camera.position.set(L * 1.3, L, L * 1.5);
  s.controls.target.set(L / 2, 0, L / 2);
  return { vortices };
}

/* ---- module 2: Dirac cone ---- */
export function buildDiracCone(s, kmax = 6, vF = 1.9) {
  s.clear();
  const seg = 72;
  const geo = new THREE.PlaneGeometry(2 * kmax, 2 * kmax, seg, seg);
  geo.rotateX(-Math.PI / 2);
  const pos = geo.attributes.position;
  const colors = [];
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i), z = pos.getZ(i);
    const k = Math.hypot(x, z);
    const E = vF * k * (k <= kmax ? 1 : 0);
    pos.setY(i, E);
    const t = Math.min(1, Math.abs(E) / (vF * kmax));
    const c = new THREE.Color().setHSL(E >= 0 ? 0.58 : 0.0, 0.8, 0.35 + 0.35 * t);
    colors.push(c.r, c.g, c.b);
  }
  geo.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
  geo.computeVertexNormals();
  const mesh = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({
    vertexColors: true, side: THREE.DoubleSide, wireframe: false, transparent: true, opacity: 0.92,
  }));
  s.scene.add(mesh);
  const grid = new THREE.GridHelper(2 * kmax, 12, 0x223355, 0x1a2440);
  grid.position.y = -0.01;
  s.scene.add(grid);
  s.camera.position.set(9, 7, 11);
  s.controls.target.set(0, 0, 0);
}

/* ---- module 3: ζ critical strip ---- */
export function buildZetaStrip(s, tmax = 40, nSigma = 81, nT = 240) {
  s.clear();
  let eMax = 0;
  // direct mapping: sigma in [0, 1.2], t in [0, tmax]
  const seg = nSigma * nT;
  const zgeo = new THREE.BufferGeometry();
  const vertices = new Float32Array(seg * 3);
  const zcol = new Float32Array(seg * 3);
  const indices = [];
  const sigmas = [], ts = [], zs = [];
  for (let a = 0; a < nSigma; a++) {
    for (let b = 0; b < nT; b++) {
      const sigma = (a / (nSigma - 1)) * 1.2;
      const t = (b / (nT - 1)) * tmax;
      const w = zeta([sigma, t]);
      const m = Math.hypot(w[0], w[1]);
      eMax = Math.max(eMax, m);
      sigmas.push(sigma); ts.push(t); zs.push(m);
    }
  }
  for (let i = 0; i < sigmas.length; i++) {
    vertices[3 * i] = sigmas[i] - 0.6;
    vertices[3 * i + 1] = Math.min(zs[i], 6);
    vertices[3 * i + 2] = ts[i] - tmax / 2;
    const h = Math.min(0.85, zs[i] / 3);
    const c = new THREE.Color().setHSL(0.62 - 0.62 * h, 0.85, 0.28 + 0.4 * h);
    zcol[3 * i] = c.r; zcol[3 * i + 1] = c.g; zcol[3 * i + 2] = c.b;
  }
  for (let a = 0; a < nSigma - 1; a++) {
    for (let b = 0; b < nT - 1; b++) {
      const i0 = a * nT + b, i1 = i0 + 1, i2 = i0 + nT, i3 = i2 + 1;
      indices.push(i0, i2, i1, i1, i2, i3);
    }
  }
  zgeo.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
  zgeo.setAttribute('color', new THREE.BufferAttribute(zcol, 3));
  zgeo.setIndex(indices);
  zgeo.computeVertexNormals();
  const mesh = new THREE.Mesh(zgeo, new THREE.MeshBasicMaterial({
    vertexColors: true, side: THREE.DoubleSide,
  }));
  s.scene.add(mesh);

  // critical line Re s = 1/2  ->  x = 0
  const critMat = new THREE.LineBasicMaterial({ color: 0xffd54a });
  const critPts = [new THREE.Vector3(-0.1, 0, -tmax / 2), new THREE.Vector3(-0.1, 0, tmax / 2)];
  s.scene.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(critPts), critMat));

  // embedded zeros (γ₁..γ₁₅ within t ≤ 40)
  const sphere = new THREE.SphereGeometry(0.22, 16, 16);
  for (const g of FIRST_ZEROS) {
    if (g > tmax) break;
    const m = new THREE.Mesh(sphere, new THREE.MeshBasicMaterial({ color: 0xff3355 }));
    m.position.set(-0.1, 0.05, g - tmax / 2);
    s.scene.add(m);
  }
  s.camera.position.set(4.5, 7, 22);
  s.controls.target.set(-0.1, 1.2, 0);
  return { eMax };
}
