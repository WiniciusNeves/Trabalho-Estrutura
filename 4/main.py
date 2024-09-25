import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x**2 + 3*x + 1

def g(x):
    return x**2 - 2*x + 4

def soma_polinomios(x):
    return f(x) + g(x)

def produto_polinomios(x):
    return f(x) * g(x)

x = np.linspace(-5, 5, 400)

plt.figure(figsize=(10, 6))

plt.plot(x, f(x), label=r'$f(x) = 2x^2 + 3x + 1$', color='blue', linewidth=2)

plt.plot(x, g(x), label=r'$g(x) = x^2 - 2x + 4$', color='green', linewidth=2)

plt.plot(x, soma_polinomios(x), label=r'$f(x) + g(x)$', color='red', linestyle='--', linewidth=2)

plt.plot(x, produto_polinomios(x), label=r'$f(x) \times g(x)$', color='purple', linestyle='-.', linewidth=2)

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title('Operações em Polinômios no Anel $\\mathbb{Z}[x]$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()