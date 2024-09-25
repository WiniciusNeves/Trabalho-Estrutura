import numpy as np
import matplotlib.pyplot as plt

numeros_complexos = [1 + 2j, -2 + 3j, 3 - 1j, -1 - 2j]

partes_reais = [z.real for z in numeros_complexos]
partes_imaginarias = [z.imag for z in numeros_complexos]

plt.figure(figsize=(6, 6))
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.scatter(partes_reais, partes_imaginarias, color='red')

for i, z in enumerate(numeros_complexos):
    plt.text(z.real, z.imag, f'z{i+1}={z}', fontsize=12, color='blue')
    plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color='green')

plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.title('Números Complexos no Plano de Argand')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True)

plt.show()
