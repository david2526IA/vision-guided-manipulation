from __future__ import annotations

import argparse
import json
from pathlib import Path

import cv2
import yaml

from .pipeline import ManipulationPipeline
from .synthetic import tabletop_scene


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulation-only vision guided manipulation MVP")
    parser.add_argument("--config", default="configs/mvp.yaml")
    parser.add_argument("--target", default="green", choices=("red", "green", "blue"))
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--synthetic", action="store_true")
    source.add_argument("--image", type=Path)
    parser.add_argument("--output", type=Path, default=Path("artifacts/result.json"))
    args = parser.parse_args()
    with Path(args.config).open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    image = tabletop_scene() if args.synthetic else cv2.imread(str(args.image))
    if image is None:
        raise SystemExit("Could not load input image.")
    result = ManipulationPipeline(config).run(image, args.target)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result.as_dict(), indent=2), encoding="utf-8")
    print(json.dumps(result.as_dict(), indent=2))
    return 0 if result.status.value == "planned" else 1


if __name__ == "__main__":
    raise SystemExit(main())

