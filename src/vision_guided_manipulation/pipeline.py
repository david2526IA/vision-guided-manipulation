from __future__ import annotations

import time

import numpy as np

from .models import Result, Status
from .planner import make_safe_plan
from .vision import detect_largest_object


class ManipulationPipeline:
    """Perception-to-plan pipeline. It never commands physical hardware."""

    def __init__(self, config: dict) -> None:
        if config.get("simulation_only") is not True:
            raise ValueError("This MVP supports only simulation_only=true.")
        self.config = config

    def run(self, image: np.ndarray, target: str, max_attempts: int = 2) -> Result:
        start = time.perf_counter()
        detection = None
        for attempt in range(1, max_attempts + 1):
            detection = detect_largest_object(image, target, self.config)
            if detection is None:
                continue
            plan, reason = make_safe_plan(detection, self.config)
            elapsed = (time.perf_counter() - start) * 1000
            if plan is not None:
                return Result(Status.PLANNED, target, attempt, None, detection, plan, elapsed)
            return Result(Status.REJECTED, target, attempt, reason, detection, None, elapsed)
        elapsed = (time.perf_counter() - start) * 1000
        return Result(Status.RETRY, target, max_attempts, "target_not_detected", None, None, elapsed)

