# Simulación de un Péndulo Doble.
Este proyecto es una simulación de un péndulo doble utilizando Python junto con la biblioteca `matplotlib` para visualizar el movimiento del péndulo y las gráficas de sus ángulos a lo largo del tiempo. El código utiliza las ecuaciones de movimiento derivadas de la [**formulación lagrangiana**](https://www.phys.lsu.edu/faculty/gonzalez/Teaching/Phys7221/DoublePendulum.pdf) y el método de **Runge-Kutta de cuarto orden (RK4)** para integrar numéricamente las ecuaciones de movimiento en el tiempo.

El resultado es un GIF que muestra la animación del péndulo doble y sus trayectorias (lado izquierdo) y una gráfica animada de los ángulos de los péndulos en función del tiempo (lado derecho). El cual se guarda como `pendulo_doble.gif`. 

##

## Clases principales:
* **Pendulo**: Clase base abstracta que define las propiedades y métodos básicos del péndulo.
*  **PenduloDoble**: Hereda de `Pendulo` y añade la implementación de las ecuaciones de Lagrange para el movimiento del péndulo doble.
*  **Energias**: Clase que define los métodos para calcular la energía cinética, potencial y mecánica (total) del sistema.

## Parámetros ajustables:

Se pueden cambiar los valores iniciales de las siguientes variables para observar diferentes comportamientos:

* `g`: Aceleración gravitacional (por defecto 9.81 $m/s^2$).
* `m1`, `m2`: Masa de los péndulos (kg).
* `L1`, `L2`: Longitudes de los péndulos (m).
* `t1`, `t2`: Ángulos iniciales de los péndulos.
* `w1`, `w2`: Velocidades angulares iniciales ().

Los parámetros se definen en la sección de **Condiciones iniciales** del código:

    g = 9.81  # Gravedad
    m1, m2 = 1.0, 1.0  # Masas de los péndulos
    L1, L2 = 1.0, 1.0  # Longitudes de los péndulos
    t1, t2 = math.radians(45), math.radians(45)  # Ángulos iniciales | Si se desea en radianes cambiar a math.pi
    w1, w2 = 0.0, 0.0  # Velocidades iniciales

En caso de que se desee poner los ángulos iniciales en radianes puede cambiar `math.radians()` a `math.pi`. 

Ejemplo: En el archivo están 45 grados, equivalente a $\pi / 4$ en radianes. Para cambiarlo simplemente modifique `math.radians(45)` a `math.pi/4`.

## Visualización de las energías del sistema:

En la sección **Visualización en tiempo real de la energía del sistema**, se puede ver la evolución de la energía potencial, cinética y mecánica del sistema en el transcurso de la animación. Puede añardirlo simplemente quitando las comillas de los comentarios.

    Visualización en tiempo real de la energía del sistema.
    
    energia_potencial = pendulo.energia_potencial()
    energia_cinetica = pendulo.energia_cinetica()
    energia_mecanica = pendulo.energia_mecanica()
    print(f"Tiempo: {frame * dt:.2f}s")
    print(f"Energía Potencial: {energia_potencial:.4f} J")
    print(f"Energía Cinética: {energia_cinetica:.4f} J")
    print(f"Energía Mecánica: {energia_mecanica:.4f} J")
    print("-" * 40)
    
