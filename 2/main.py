import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles

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
imagem = r"I = { f(x) ∈ ℝ | -4 ≤ f(x) ≤ 10 }"  
print(dominio)
print(imagem)

plt.figure(figsize=(8, 8))

set_a = {1, 2, 3, 4, 5, 9, 10}
set_b = {4, 5, 6, 7, 8, 10, 11}

venn_diagram = venn2([set_a, set_b], ('Conjunto A', 'Conjunto B'))
venn2_circles([set_a, set_b], linestyle='dashed')
for text in venn_diagram.set_labels:
    if text: text.set_fontsize(16)
for text in venn_diagram.subset_labels:
    if text: text.set_fontsize(12)

plt.title('Diagrama de Venn de A e B')
plt.show()


