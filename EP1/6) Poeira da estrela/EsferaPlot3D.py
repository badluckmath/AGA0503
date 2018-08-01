

# Essa plotagem é inútil. Fiz a implementação, mas na hora que plotei a primeira vez
# eu percebi que o tamanho da esfera central é tão menor que a casca de poeira que
# basicamente n dá pra ver nada, mas é legal pra perceber como o shell de poeira
# é gigantesco. Fica parecendo uma bola azul dentro de outra, sendo que lá no meio tem a estrela

# Bibliotecas utilizadas
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

R = 1         # Utiliza-se raio da estrela como 1, já que os raios interno e externo
              #do shell de poeira são definidos em função dessa grandeza

Re = 20 * R   # Raio externo do shell
Ri = 200 * R  # Raio interno do shell

# Esfera central (estrela)
u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:10j]
x = R * np.cos(u)*np.sin(v)
y = R * np.sin(u)*np.sin(v)
z = R * np.cos(v)
ax.plot_surface(x, y, z, color="red")

# Shell de poeira, raio interno
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
x = Ri * np.cos(u)*np.sin(v)
y = Ri * np.sin(u)*np.sin(v)
z = Ri * np.cos(v)
ax.plot_wireframe(x, y, z, color="blue")

# Shell de poeira, raio externo
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
x = Re * np.cos(u)*np.sin(v)
y = Re * np.sin(u)*np.sin(v)
z = Re * np.cos(v)
ax.plot_wireframe(x, y, z, color="blue")

plt.show()
