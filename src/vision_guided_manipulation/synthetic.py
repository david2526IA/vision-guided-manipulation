from __future__ import annotations

import cv2
import numpy as np


def tabletop_scene() -> np.ndarray:
    """Deterministic overhead scene: red, green and blue known objects."""
    image = np.full((480, 640, 3), (42, 42, 42), dtype=np.uint8)
    cv2.circle(image, (150, 145), 28, (0, 0, 255), -1)  # red in BGR
    cv2.circle(image, (330, 250), 32, (0, 255, 0), -1)
    cv2.circle(image, (505, 170), 30, (255, 0, 0), -1)
    return image

