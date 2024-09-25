import numpy as np
import matplotlib.pyplot as plt

quadrado = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 1]])


def rotacionar(quadrado, angulo):
    theta = np.radians(angulo)
    matriz_rotacao = np.array([[np.cos(theta), -np.sin(theta)],
                               [np.sin(theta), np.cos(theta)]])
    return np.dot(quadrado, matriz_rotacao.T)


angulos = [0, 90, 180, 270]
cores = ['blue', 'green', 'orange', 'red']

plt.figure(figsize=(6, 6))


for i, angulo in enumerate(angulos):
    quadrado_rotacionado = rotacionar(quadrado, angulo)
    plt.plot(quadrado_rotacionado[:, 0], quadrado_rotacionado[:, 1], label=f'Rotação {angulo}°', color=cores[i])

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Representação do Grupo Cíclico C4 (Rotações)')
plt.legend()
plt.grid(True)


plt.xlim(-2, 2)
plt.ylim(-2, 2)


plt.gca().set_aspect('equal', adjustable='box')
plt.show()