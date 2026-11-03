# Arquitectura

```text
Camera/file/synthetic source
            │
            ▼
       HSV detector ──► Detection
            │
            ▼
       Planar mapper ──► XY (mm)
            │
            ▼
    Workspace validator
            │
            ▼
  Simulated grasp sequence + JSON report
```

La fuente está desacoplada de la lógica para poder usar archivos ahora y, más adelante, imágenes ROS 2 publicadas por `openarm_camera_bridge`. La salida no controla hardware: es un contrato de planificación que un adaptador futuro deberá revisar y ejecutar de forma segura.

