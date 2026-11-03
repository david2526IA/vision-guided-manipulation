# Vision-Guided Manipulation

> Visión artificial y planificación de agarre, con seguridad desde el diseño y sin afirmar ejecución física no verificada.

[![CI](https://github.com/david2526IA/vision-guided-manipulation/actions/workflows/ci.yml/badge.svg)](https://github.com/david2526IA/vision-guided-manipulation/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-vision-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![Safety](https://img.shields.io/badge/execution-simulation--only-F59E0B)](LIMITATIONS.md)

**Vision-Guided Manipulation** es un MVP reproducible para convertir una imagen cenital en una propuesta de agarre 2D: detecta tres objetos conocidos por color, transforma el píxel al plano de trabajo, valida límites y genera una secuencia segura de aproximación, cierre y elevación. La ejecución actual es deliberadamente simulada; no mueve robots ni publica órdenes de actuadores.

The same repository includes a deterministic, simulation-first baseline suitable for validating perception-to-planning logic before hardware integration.

## Flujo

```text
Imagen / escena sintética
        │
        ▼
Segmentación HSV + filtros geométricos
        │
        ▼
Centro del objeto en píxeles
        │ homografía calibrada
        ▼
Pose 2D sobre mesa (mm)
        │ límites y margen de seguridad
        ▼
Plan de agarre simulado + métricas JSON
```

## Qué demuestra hoy

- Detección reproducible de objetos rojo, verde y azul sobre fondo controlado.
- Transformación píxel → milímetros mediante una homografía configurable.
- Rechazo de objetivos fuera del área de trabajo o demasiado pequeños.
- Máquina de estados con reintento ante una detección no válida.
- Resultados auditables en JSON, pruebas unitarias y CI.

## Inicio rápido

```bash
git clone https://github.com/david2526IA/vision-guided-manipulation.git
cd vision-guided-manipulation
python -m venv .venv
```

Activa el entorno y ejecuta:

```bash
pip install -e ".[dev]"
vgm --synthetic --target green --output artifacts/demo.json
pytest
```

El comando crea una escena determinista, propone un agarre para el objeto verde y guarda un informe. Para una imagen propia:

```bash
vgm --image path/to/top_camera.png --target red --output artifacts/result.json
```

## Alcance y siguiente fase

Este repositorio **no** valida profundidad, calibración de una cámara real, cinemática inversa ni movimiento físico. El siguiente paso es integrar una cámara calibrada mediante [`openarm-ros2-camera-bridge`](https://github.com/david2526IA/openarm-ros2-camera-bridge), sustituir la pose plana por RGB-D/estimación 6D y conectar el plan a MoveIt o al controlador del robot detrás de una confirmación humana y un circuito de seguridad.

Consulta [SPEC.md](SPEC.md), [ARCHITECTURE.md](ARCHITECTURE.md) y [LIMITATIONS.md](LIMITATIONS.md) antes de integrar hardware.

## Tecnologías

`Python` · `OpenCV` · `NumPy` · `YAML` · `ROS 2 (integración futura)` · `MoveIt (integración futura)` · `visión artificial` · `robótica segura`

## Licencia

MIT © 2026 David. Véase [LICENSE](LICENSE).

