import numpy as np
import matplotlib.pyplot as plt

def eq1(x, z):
    return (4 - 3 * x + z) / 1  

def eq2(x, y):
    return (-2 * x - 5 * y) / 7    

x_values = np.linspace(-1, 3, 400) 
y_values = np.linspace(-1, 3, 400)
z_values = np.linspace(-1, 3, 400) 

y1_values = eq1(x_values, z_values)
y2_values = eq2(x_values, y_values)

A = np.array([[3, 1, -1], [2, 5, 7], [1, 0, 0]])
b = np.array([4, 0, 0])

x, y, z = np.linalg.solve(A, b)

plt.figure(figsize=(10, 6))

plt.plot(x_values, y1_values, label='3x + y - z = 4', color='blue')
plt.plot(x_values, y2_values, label='2x + 5y + 7z = 0', color='green')

plt.scatter(x, y, label='Solução', color='red')

plt.xlim(-1, 3)
plt.ylim(-1, 5)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.title('Sistema de Equações Lineares')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

