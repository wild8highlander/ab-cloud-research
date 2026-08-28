"""
verifier_core.py — Core verification engine for the monograph.

Contains the TaskRunner class that executes verification tasks, collects
results, generates figures, and produces reports. Each task is a function
that takes a Config and returns a TaskResult.

The suite contains 240+ tasks organized into 16 chapters:
  Ch 1-2:  Analytical origin of b (Kirchhoff, Rodrigues)
  Ch 3:    Selberg zeta and b
  Ch 4:    Euler e identity, γ, C_K, C_s
  Ch 5:    Anosov flow
  Ch 6:    Smagorinsky/Kolmogorov constants
  Ch 7:    b as phase rotation (Rodrigues formula)
  Ch 8:    Regularity proof verification
  Ch 9:    Physical dissipation
  Ch 10:   2D NSE
  Ch 11:   3D NSE (5 models)
  Ch 12:   φ-attractor
  Ch 13:   Universality
  Ch 14:   Comparison with classical approaches
  Ch 15:   Open questions
  Ch 16:   KdV + b (the new chapter)

Author: Z.ai Research, 2026
"""
from __future__ import annotations

import json
import time
import traceback
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Callable, List, Dict, Any, Optional
import numpy as np

# Import config
from config import Config


# ==================================================================
# Task result dataclass
# ==================================================================
@dataclass
class TaskResult:
    """Result of a single verification task."""
    task_id: str
    chapter: int
    title: str
    description: str
    passed: bool
    expected: Any
    measured: Any
    residual: float
    tolerance: float
    elapsed_s: float
    details: Dict[str, Any] = field(default_factory=dict)
    figure_paths: List[str] = field(default_factory=list)
    error: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

    def summary_line(self) -> str:
        status = "✓ PASS" if self.passed else "✗ FAIL"
        return (f"[{self.task_id:>6s}] Ch{self.chapter:02d} {status}  "
                f"{self.title[:50]:50s}  "
                f"residual={self.residual:.2e}  "
                f"({self.elapsed_s:.3f}s)")


# ==================================================================
# Task registry
# ==================================================================
TASK_REGISTRY: Dict[str, Callable] = {}


def register_task(task_id: str, chapter: int):
    """Decorator to register a verification task."""
    def decorator(func: Callable):
        TASK_REGISTRY[task_id] = func
        func._task_id = task_id
        func._chapter = chapter
        return func
    return decorator


# ==================================================================
# Task runner
# ==================================================================
class TaskRunner:
    """Executes verification tasks and collects results."""

    def __init__(self, config: Config):
        self.config = config
        self.results: List[TaskResult] = []
        self.figures_dir = Path(config.output_dir) / config.figures_dir
        self.results_dir = Path(config.output_dir) / config.results_dir
        self.reports_dir = Path(config.output_dir) / config.reports_dir
        self.figures_dir.mkdir(parents=True, exist_ok=True)
        self.results_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def run_task(self, task_id: str, task_func: Callable) -> TaskResult:
        """Run a single task and return its result."""
        t0 = time.time()
        try:
            result = task_func(self.config, self.figures_dir)
            if not isinstance(result, TaskResult):
                raise ValueError(f"Task {task_id} did not return a TaskResult")
            result.elapsed_s = time.time() - t0
            if self.config.verbose:
                print(f"  {result.summary_line()}")
            return result
        except Exception as e:
            elapsed = time.time() - t0
            error_msg = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
            result = TaskResult(
                task_id=task_id,
                chapter=getattr(task_func, '_chapter', 0),
                title=task_func.__name__,
                description=task_func.__doc__ or "",
                passed=False,
                expected=None,
                measured=None,
                residual=float('inf'),
                tolerance=1e-6,
                elapsed_s=elapsed,
                error=error_msg,
            )
            if self.config.verbose:
                print(f"  {result.summary_line()}  ERROR: {e}")
            return result

    def run_chapter(self, chapter: int) -> List[TaskResult]:
        """Run all tasks for a given chapter."""
        chapter_tasks = [
            (tid, func) for tid, func in TASK_REGISTRY.items()
            if getattr(func, '_chapter', 0) == chapter
        ]
        chapter_tasks.sort(key=lambda x: x[0])
        print(f"\n{'='*60}")
        print(f"  Chapter {chapter}: {len(chapter_tasks)} tasks")
        print(f"{'='*60}")
        results = []
        for tid, func in chapter_tasks:
            result = self.run_task(tid, func)
            self.results.append(result)
            results.append(result)
        return results

    def run_all(self) -> List[TaskResult]:
        """Run all tasks for all configured chapters."""
        print(f"\n{'#'*60}")
        print(f"  MONOGRAPH VERIFICATION SUITE")
        print(f"  Chapters: {self.config.chapters_to_run}")
        print(f"  Total registered tasks: {len(TASK_REGISTRY)}")
        print(f"{'#'*60}")

        t_total = time.time()
        for ch in self.config.chapters_to_run:
            if ch in [getattr(f, '_chapter', 0) for f in TASK_REGISTRY.values()]:
                self.run_chapter(ch)

        total_time = time.time() - t_total
        n_pass = sum(1 for r in self.results if r.passed)
        n_fail = sum(1 for r in self.results if not r.passed)
        print(f"\n{'#'*60}")
        print(f"  COMPLETE: {len(self.results)} tasks in {total_time:.1f}s")
        print(f"  PASSED: {n_pass}  FAILED: {n_fail}")
        print(f"  Pass rate: {100*n_pass/max(len(self.results),1):.1f}%")
        print(f"{'#'*60}")
        return self.results

    def save_results_json(self):
        """Save all results to JSON."""
        path = self.results_dir / "all_results.json"
        data = {
            "config": self.config.to_dict(),
            "summary": {
                "total_tasks": len(self.results),
                "passed": sum(1 for r in self.results if r.passed),
                "failed": sum(1 for r in self.results if not r.passed),
                "total_time_s": sum(r.elapsed_s for r in self.results),
            },
            "results": [r.to_dict() for r in self.results],
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=2, default=str)
        print(f"\nResults saved to {path}")
        return path


# ==================================================================
# Helper functions for tasks
# ==================================================================
def make_result(task_id: str, chapter: int, title: str, description: str,
                expected, measured, tolerance=1e-6, **kwargs) -> TaskResult:
    """Helper to create a TaskResult."""
    # Handle boolean comparisons
    if isinstance(expected, bool) or isinstance(measured, bool):
        passed = bool(expected) == bool(measured)
        residual = 0.0 if passed else 1.0
    elif isinstance(expected, (int, float)) and isinstance(measured, (int, float)):
        residual = abs(float(measured) - float(expected))
        passed = residual < tolerance
    elif expected == measured:
        passed = True
        residual = 0.0
    else:
        passed = False
        residual = 1.0
    return TaskResult(
        task_id=task_id, chapter=chapter, title=title,
        description=description, passed=passed,
        expected=expected, measured=measured,
        residual=residual, tolerance=tolerance,
        elapsed_s=0.0,  # will be set by runner
        details=kwargs,
    )


if __name__ == "__main__":
    cfg = Config.default()
    runner = TaskRunner(cfg)
    print(f"Registered tasks: {len(TASK_REGISTRY)}")
    print(f"Chapters with tasks: {sorted(set(getattr(f, '_chapter', 0) for f in TASK_REGISTRY.values()))}")
