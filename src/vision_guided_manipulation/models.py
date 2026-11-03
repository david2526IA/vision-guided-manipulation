from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum


class Status(str, Enum):
    PLANNED = "planned"
    RETRY = "retry"
    REJECTED = "rejected"


@dataclass(frozen=True)
class Detection:
    label: str
    pixel_x: float
    pixel_y: float
    area_px: float
    confidence: float


@dataclass(frozen=True)
class GraspPlan:
    x_mm: float
    y_mm: float
    approach_z_mm: float
    grasp_z_mm: float
    lift_z_mm: float
    steps: tuple[str, ...]


@dataclass(frozen=True)
class Result:
    status: Status
    target: str
    attempts: int
    reason: str | None
    detection: Detection | None
    plan: GraspPlan | None
    latency_ms: float

    def as_dict(self) -> dict:
        payload = asdict(self)
        payload["status"] = self.status.value
        return payload

