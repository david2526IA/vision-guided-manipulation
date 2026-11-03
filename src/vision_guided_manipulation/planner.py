from __future__ import annotations

import numpy as np

from .models import Detection, GraspPlan


def pixel_to_table_mm(detection: Detection, config: dict) -> tuple[float, float]:
    matrix = np.asarray(config["homography"], dtype=float)
    projected = matrix @ np.array([detection.pixel_x, detection.pixel_y, 1.0])
    if projected[2] == 0:
        raise ValueError("Invalid homography projection.")
    return float(projected[0] / projected[2]), float(projected[1] / projected[2])


def make_safe_plan(detection: Detection, config: dict) -> tuple[GraspPlan | None, str | None]:
    x_mm, y_mm = pixel_to_table_mm(detection, config)
    workspace = config["workspace_mm"]
    margin = float(workspace["margin"])
    inside = (
        float(workspace["x_min"]) + margin <= x_mm <= float(workspace["x_max"]) - margin
        and float(workspace["y_min"]) + margin <= y_mm <= float(workspace["y_max"]) - margin
    )
    if not inside:
        return None, "target_outside_safe_workspace"
    grasp = config["grasp"]
    plan = GraspPlan(
        x_mm=x_mm,
        y_mm=y_mm,
        approach_z_mm=float(grasp["approach_z_mm"]),
        grasp_z_mm=float(grasp["grasp_z_mm"]),
        lift_z_mm=float(grasp["lift_z_mm"]),
        steps=("approach", "descend", "close_gripper", "lift"),
    )
    return plan, None

