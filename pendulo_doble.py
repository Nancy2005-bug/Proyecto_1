import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from abc import ABC, abstractmethod
from functools import cache

class Pendulo(ABC):
    
    def __init__(self, g, m1, m2, t1, t2, w1, w2, L1, L2):
        self.g = g
        self.m1 = m1
        self.m2 = m2
        self.t1 = t1
        self.t2 = t2
        self.w1 = w1
        self.w2 = w2
        self.L1 = L1
        self.L2 = L2
    
    @property
    def g(self):
        return self._g
    
    @g.setter
    def g(self, valor):
        if valor > 0:
            self._g = valor
        else:
            raise ValueError("La gravedad debe ser un número positivo.")
    
    @property
    def m1(self):
        return self._m1
    
    @m1.setter 
    def m1(self, valor):
        if valor > 0:
            self._m1 = valor
        else:
            return ValueError("La masa debe ser positiva.")
    
    @property
    def m2(self):
        return self._m2
    
    @m2.setter 
    def m2(self, valor):
        if valor > 0:
            self._m2 = valor
        else:
            return ValueError("La masa debe ser positiva.")
    
    @property
    def t1(self):
        return self._t1
    
    @t1.setter
    def t1(self, valor):
        self._t1 = valor
    
    @property
    def t2(self):
        return self._t2
    
    @t2.setter
    def t2(self, valor):
        self._t2 = valor
    
    @property
    def w1(self):
        return self._w1
    
    @w1.setter
    def w1(self, valor):
        self._w1 = valor
    
    @property
    def w2(self):
        return self._w2
    
    @w2.setter
    def w2(self, valor):
        self._w2 = valor
    
    @property
    def L1(self):
        return self._L1
    
    @L1.setter
    def L1(self, valor):
        if valor > 0:
            self._L1 = valor
        else:
            return ValueError("La longitud del péndulo debe tener valores positivos.")
    
    @property
    def L2(self):
        return self._L2  
    
    @L2.setter
    def L2(self, valor):
        if valor > 0:
            self._L2 = valor
        else:
            return ValueError("La longitud del péndulo debe tener valores positivos.")  
    
    @abstractmethod
    def lagrange(self, t1, t2, w1, w2):
        pass

class Energias:
    
    def energia_potencial(self):
        m1 = self.m1
        t1 = self.t1
        L1 = self.L1
        m2 = self.m2
        t2 = self.t2
        L2 = self.L2
        g = self.g
        y1 = -L1 * math.cos(t1)
        y2 = y1 - L2 * math.cos(t2)
        return m1 * g * y1 + m2 * g * y2
    
    def energia_cinetica(self):
        m1 = self.m1
        t1 = self.t1
        w1 = self.w1
        L1 = self.L1
        m2 = self.m2
        t2 = self.t2
        w2 = self.w2
        L2 = self.L2
        K1 = 0.5 * m1 * (L1 * w1)**2
        K2 = 0.5 * m2 * ((L1 * w1)**2 + (L2 * w2)**2 +
                         2 * L1 * L2 * w1 * w2 * math.cos(t1 - t2))
        return K1 + K2
    
    def energia_mecanica(self):
        return self.energia_cinetica() + self.energia_potencial()

# Clase concreta para el péndulo doble
class PenduloDoble(Pendulo, Energias):
    
    @cache
    def lagrange(self, t1, t2, w1, w2):
        m1, L1 = self.m1, self.L1
        m2, L2 = self.m2, self.L2
        g = self.g
        
        a1 = (L2 / L1) * (m2 / (m1 + m2)) * math.cos(t1 - t2)
        a2 = (L1 / L2) * math.cos(t1 - t2)
        
        f1 = -(L2 / L1) * (m2 / (m1 + m2)) * (w2**2) * math.sin(t1 - t2) - (g / L1) * math.sin(t1)
        f2 = (L1 / L2) * (w1**2) * math.sin(t1 - t2) - (g / L2) * math.sin(t2)
        
        g1 = (f1 - a1 * f2) / (1 - a1 * a2)
        g2 = (f2 - a2 * f1) / (1 - a1 * a2)
        
        return [w1, w2, g1, g2]
    
    
    def time_step(self, dt):
        y = [self.t1, self.t2, self.w1, self.w2]
        
        k1 = self.lagrange(*y)
        k2 = self.lagrange(*(y[i] + dt * k1[i] / 2 for i in range(4)))
        k3 = self.lagrange(*(y[i] + dt * k2[i] / 2 for i in range(4)))
        k4 = self.lagrange(*(y[i] + dt * k3[i] for i in range(4)))
        
        R = [1.0 / 6.0 * dt * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]) for i in range(4)]
        
        self.t1 += R[0]
        self.t2 += R[1]
        self.w1 += R[2]
        self.w2 += R[3]

"""
Condiciones iniciales
"""
g = 9.81 # Gravedad
m1, m2 = 1.0, 1.0 # Masas de los péndulos
L1, L2 = 1.0, 1.0 # Longitudes de los péndulos
t1, t2 = math.radians(180), math.radians(181)  # Ángulos iniciales 
w1, w2 = 0.0, 0.0  # Velocidades iniciales

pendulo = PenduloDoble(g, m1, m2, t1, t2, w1, w2, L1, L2)

# Configuración de la animación
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [1, 1]})

# Axes para el movimiento del péndulo
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)
ax1.set_aspect('equal')
ax1.set_title('Movimiento del Péndulo Doble')
ax1.grid()
time_text = ax1.text(-1.5, 1.8, '', fontsize=12) # tiempo en la gráfica del péndulo

# Axes para las gráficas de las velocidades angulares
ax2.set_xlim(0, 10)
ax2.set_ylim(-10, 10)
ax2.set_title('Ángulos en función del tiempo')
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("Ángulo (rad)")
ax2.grid()

# Líneas para el péndulo
line, = ax1.plot([], [], lw=2, color='black')
point1, = ax1.plot([], [], 'bo') 
point2, = ax1.plot([], [], 'ro') 
trail1, = ax1.plot([], [], 'b-', alpha=0.5)
trail2, = ax1.plot([], [], 'r-', alpha=0.5)  

# Líneas para las gráficas de las velocidades angulares
t_data, theta1_data, theta2_data = [], [], []
line_theta1, = ax2.plot([], [], 'b-', label='Péndulo 1')
line_theta2, = ax2.plot([], [], 'r-', label='Péndulo 2')
ax2.legend()

x1_trail, y1_trail = [], []
x2_trail, y2_trail = [], []

# Función de inicialización de la animación
def init():
    line.set_data([], [])
    point1.set_data([], [])
    point2.set_data([], [])
    trail1.set_data([], [])
    trail2.set_data([], [])
    line_theta1.set_data([], [])
    line_theta2.set_data([], [])
    time_text.set_text('')
    return line, point1, point2, trail1, trail2, line_theta1, line_theta2, time_text

def update(frame):
    global pendulo
    dt = 0.05
    pendulo.time_step(dt)
    
    # Posiciones del péndulo
    x1 = pendulo.L1 * math.sin(pendulo.t1)
    y1 = -pendulo.L1 * math.cos(pendulo.t1)
    x2 = x1 + pendulo.L2 * math.sin(pendulo.t2)
    y2 = y1 - pendulo.L2 * math.cos(pendulo.t2)
    
    line.set_data([0, x1, x2], [0, y1, y2])
    point1.set_data([x1], [y1])
    point2.set_data([x2], [y2])
    
    # Agrega las posiciones actuales a las listas de trayectoria
    x1_trail.append(x1)
    y1_trail.append(y1)
    x2_trail.append(x2)
    y2_trail.append(y2)
    
    # Limite de la longitud de la trayectoria mostrada
    trail_length = 200  
    if len(x1_trail) > trail_length:
        x1_trail.pop(0)
        y1_trail.pop(0)
    if len(x2_trail) > trail_length:
        x2_trail.pop(0)
        y2_trail.pop(0)
    
    # Actualización de las trayectorias
    trail1.set_data(x1_trail, y1_trail)
    trail2.set_data(x2_trail, y2_trail)
    
    time_text.set_text(f'Tiempo = {frame*dt:.1f}s')
    
    # Actualización de los datos de las velocidades angulares
    t_data.append(frame * dt)
    theta1_data.append(pendulo.t1)
    theta2_data.append(pendulo.t2)
        
    line_theta1.set_data(t_data, theta1_data)
    line_theta2.set_data(t_data, theta2_data)
    
    """
    energia_potencial = pendulo.energia_potencial()
    energia_cinetica = pendulo.energia_cinetica()
    energia_mecanica = pendulo.energia_mecanica()
    print(f"Tiempo: {frame * dt:.2f}s")
    print(f"Energía Potencial: {energia_potencial:.4f} J")
    print(f"Energía Cinética: {energia_cinetica:.4f} J")
    print(f"Energía Mecánica: {energia_mecanica:.4f} J")
    print("-" * 40)
    """
    
    return line, point1, point2, trail1, trail2, line_theta1, line_theta2, time_text

ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=50)

#plt.tight_layout()
plt.show()

