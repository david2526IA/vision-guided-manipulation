# Especificación del MVP

## Objetivo

Procesar una imagen cenital de una mesa controlada, localizar uno de tres objetos conocidos y generar una propuesta de agarre en coordenadas 2D de mesa.

## Entradas y salidas

| Entrada | Contrato |
|---|---|
| Imagen BGR | PNG/JPEG o escena sintética, vista cenital estable |
| Objetivo | `red`, `green` o `blue` |
| Configuración | rangos HSV, homografía, límites de mesa y tamaños mínimos |

| Salida | Contrato |
|---|---|
| Detección | color, centro en píxeles, área y confianza geométrica |
| Propuesta | punto XY en mm, altura de aproximación, altura de agarre y elevación |
| Informe | estado, reintentos, razones de rechazo y latencia |

## Criterios de aceptación

1. En las escenas sintéticas versionadas, los tres objetos deben localizarse cerca de su centro esperado.
2. Un objetivo fuera de límites debe resultar en `rejected`, sin una propuesta ejecutable.
3. El modo por defecto debe permanecer en `simulation_only: true`.
4. Ningún módulo debe emitir comandos de robot, PLC o actuador.

