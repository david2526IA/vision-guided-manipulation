# Límites de seguridad y validez

- La pose es **2D planar**, no una pose 6D. No usarla para agarrar piezas reales sin calibración y percepción de profundidad.
- La detección HSV funciona solo en iluminación y colores controlados; no es un detector YOLO ni un modelo entrenado.
- La homografía incluida es una configuración de demostración. Debe reemplazarse tras calibrar cámara, plano de mesa y unidades reales.
- `simulation_only` evita por diseño cualquier interfaz de movimiento. La integración física exige límites articulares, control de colisión, parada de emergencia, velocidad reducida, supervisión humana y pruebas incrementales.
- Las métricas de escenas sintéticas prueban software, no rendimiento físico ni seguridad de una celda.

