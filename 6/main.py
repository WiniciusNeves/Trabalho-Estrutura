import numpy as np
import matplotlib.pyplot as plt

x_linear = np.linspace(-10, 10, 400)
x_quadratic = np.linspace(-10, 10, 400)
x_exponential = np.linspace(0, 5, 400)  
x_logarithmic = np.linspace(0.1, 5, 400) 

m = 2
b = 1
f_linear = m * x_linear + b

a = 1
b_q = 0
c = 0
f_quadratic = a * x_quadratic**2 + b_q * x_quadratic + c

a_exp = 1
b_exp = 2
f_exponential = a_exp * (b_exp ** x_exponential)

b_log = 2
f_logarithmic = np.log(x_logarithmic) / np.log(b_log)  

plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(x_linear, f_linear, label='f(x) = 2x + 1', color='blue')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('Função Linear')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x_quadratic, f_quadratic, label='f(x) = x²', color='green')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('Função Quadrática')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x_exponential, f_exponential, label='f(x) = 2^x', color='red')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('Função Exponencial')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x_logarithmic, f_logarithmic, label='f(x) = log₂(x)', color='purple')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('Função Logarítmica')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
