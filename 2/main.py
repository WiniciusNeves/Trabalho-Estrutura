import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def f(x):
    return x**2 - 4 

x_values = np.linspace(-5, 5, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'f(x) = x² - 4', color='blue')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('Gráfico da Função f(x) = x² - 4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-5, 5)
plt.ylim(-5, 10)
plt.grid()
plt.legend()
plt.show()

dominio = r"D = { x ∈ ℝ | -5 ≤ x ≤ 5 }"
imagem = r"I = { f(x) ∈ ℝ | f(x) ≥ -4 }"  
print(dominio)
print(imagem)

plt.figure(figsize=(8, 8))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

venn2([set_a, set_b], ('Conjunto A', 'Conjunto B'))
plt.title('Diagrama de Venn de A e B')
plt.show()
