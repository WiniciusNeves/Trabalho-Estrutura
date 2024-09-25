import numpy as np
import matplotlib.pyplot as plt

v = np.array([[1], [1]])  
n = 4 

def plot_vector(ax, v, color='b', label=None):
    ax.quiver(0, 0, v[0, 0], v[1, 0], angles='xy', scale_units='xy', scale=1, color=color, label=label)

def expand_u(v):
    return 2 * v  

def contract_u(v):
    return 0.5 * v  

def expand_x(v):
    return np.array([[2 * v[0, 0]], [v[1, 0]]])  

def contract_x(v):
    return np.array([[0.5 * v[0, 0]], [v[1, 0]]])  

def reflect_x(v):
    return np.array([[v[0, 0]], [-v[1, 0]]]) 

def reflect_origin(v):
    return -v  

def reflect_y_equals_x(v):
    return np.array([[v[1, 0]], [v[0, 0]]]) 

def rotate_clockwise(v, phi):
    rotation_matrix = np.array([[np.cos(phi), np.sin(phi)],
                                 [-np.sin(phi), np.cos(phi)]])
    return rotation_matrix @ v  


fig, axs = plt.subplots(3, 3, figsize=(15, 10))
phi = np.pi / 4  


transformations = [
    (expand_u(v), "Expansão na direção de u"),
    (contract_u(v), "Contração na direção de u"),
    (expand_x(v), "Expansão na direção do eixo x"),
    (contract_x(v), "Contração na direção do eixo x"),
    (reflect_x(v), "Reflexão em torno do eixo x"),
    (reflect_origin(v), "Reflexão em torno da origem"),
    (reflect_y_equals_x(v), "Reflexão em torno da reta y = x"),
    (rotate_clockwise(v, phi), "Rotação no sentido horário"),
]

for ax, (transformed_vector, title) in zip(axs.flatten(), transformations):
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.axhline(0, color='grey', lw=0.5)
    ax.axvline(0, color='grey', lw=0.5)
    ax.grid()
    plot_vector(ax, v, color='b', label='Vetor original')
    plot_vector(ax, transformed_vector, color='r', label='Vetor transformado')
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.legend()

plt.tight_layout()
plt.show()
