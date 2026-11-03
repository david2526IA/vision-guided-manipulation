from pathlib import Path

import yaml

from vision_guided_manipulation.pipeline import ManipulationPipeline
from vision_guided_manipulation.synthetic import tabletop_scene


def config() -> dict:
    return yaml.safe_load(Path("configs/mvp.yaml").read_text(encoding="utf-8"))


def test_green_target_generates_safe_plan() -> None:
    result = ManipulationPipeline(config()).run(tabletop_scene(), "green")
    assert result.status.value == "planned"
    assert result.plan is not None
    assert 140 < result.plan.x_mm < 170
    assert 100 < result.plan.y_mm < 130


def test_absent_target_requests_retry() -> None:
    image = tabletop_scene() * 0
    result = ManipulationPipeline(config()).run(image, "red")
    assert result.status.value == "retry"
    assert result.attempts == 2


def test_plan_near_edge_is_rejected() -> None:
    image = tabletop_scene()
    image[:] = 42
    import cv2
    cv2.circle(image, (5, 5), 25, (0, 255, 0), -1)
    result = ManipulationPipeline(config()).run(image, "green")
    assert result.status.value == "rejected"
    assert result.reason == "target_outside_safe_workspace"

