from __future__ import annotations

import cv2
import numpy as np

from .models import Detection


def detect_largest_object(image: np.ndarray, label: str, config: dict) -> Detection | None:
    """Return the largest valid HSV contour for one configured known object."""
    object_config = config["objects"].get(label)
    if object_config is None:
        raise ValueError(f"Unknown target '{label}'.")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(object_config["lower_hsv"], dtype=np.uint8)
    upper = np.array(object_config["upper_hsv"], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    contour = max(contours, key=cv2.contourArea)
    area = float(cv2.contourArea(contour))
    if area < float(config["minimum_area_px"]):
        return None
    moments = cv2.moments(contour)
    if moments["m00"] == 0:
        return None
    x = moments["m10"] / moments["m00"]
    y = moments["m01"] / moments["m00"]
    confidence = min(1.0, area / 2000.0)
    return Detection(label=label, pixel_x=x, pixel_y=y, area_px=area, confidence=confidence)

