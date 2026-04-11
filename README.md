# Webots Laboratorio1

## Descripción del laboratorio
En este laboratorio se experimentará la simulación de robots por medio de Webots. En esta simulación lograremos comprender el comportamiento cinemático de un robot móvil (E-Puck). Se experimentará colocando distintas velocidades en las ruedas para ver el comportamiento y como este va cambiando según la variación de esta, también se introducirá ruido para ver como varian los movimientos del robot.

## Cómo ejecutar la simulación
Para ejecutar la simulación lo que debemos seguir los siguientes pasos
1. Colocar el siguiente codigo en el cmd o terminal de tu dispositivo `git clone https://github.com/DavidHenriquezBravo/Webots_lab1.git`. Se creará la carpeta "Webots_lab1" en la dirección `C:\Users\<nombre_usuario>` (o el equivalente en sistemas operativos diferentes de Windows).
2. Abre Webots y ve a **File > OpenWorld**. Desde ahí, navega hasta la carpeta donde se clonó el repositorio, entra a `worlds` y selecciona el archivo `Lab1.wbt`
3. Una vez abierto el archivo debes asegurarte de que esté seleccionado el control `ControlerPy.py`, y luego presionar el boton `>` para iniciar la simulación.
   * En este punto tienes 6 opciones, los cuales se pueden activar al presionar la tecla indicada:
     1. Hacer una linea recta (Presionar 1).
     2. Hacer un circulo (Presionar 2).
     3. Hacer un cuadrado (Presionar 3).
     4. Hacer una curva (Presionar 4).
     5. Rotar en el mismo lugar (Presionar 5).
     6. Detener robot* (Presionar 0).
     
     *No se puede detener el robot mientras hace un cuadrado.

## Resultados
Los resultados que logramos obtener fueron los siguientes:
1. Logramos darnos cuenta cómo el ruido afecta en la trayectoria de los robots. Al introducir esta variable hemos visto como los robots puedes desviarse un poco al avanzar, afectando sus rutas "ideales" (libres de ruido).
2. Hemos podido ver cómo las diferentes velocidades en las ruedas afectan la trayectorias, ya sea realizando lineas rectas, curvas o circulos, incluyendo el cómo colocar una velocidad en negativo puede hacer que la ruta cambie de sentido.

## Preguntas de análisis
1. ¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?
   * El robot avanza en linea recta.
2. ¿Cómo cambia la trayectoria cuando las velocidades son diferentes?
   * Cuando las velocidades son diferentes el robot tiende a realizar una curva, incluso haciendo un círculo.
3. ¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?
   * Depende. Si ambas ruedas cuentan con la misma velocidad, el robot empieza a realizar un circulo. En cambio, si tienen diferentes velocidades, girará o se moverá en el sentido contrario al como deberia hacerlo si es que ambas ruedas tuvieran el mismo sentido.
4. ¿Qué tipo de movimiento permite dibujar un círculo?
   * El movimiento que permite dibujar un circulo es cuando una rueda tiene una velocidad inferior a la otra.
