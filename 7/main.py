import numpy as np
import matplotlib.pyplot as plt

def eq1(x):
    return (6 - 2 * x) / 3  

def eq2(x):
    return (x + 1) / 2    

def eq3(x):
    return 5 - 3 * x   

x_values = np.linspace(-1, 3, 400) 

y1_values = eq1(x_values)
y2_values = eq2(x_values)
y3_values = eq3(x_values)

plt.figure(figsize=(10, 6))

plt.plot(x_values, y1_values, label='2x + 3y = 6', color='blue')
plt.plot(x_values, y2_values, label='x - 2y = -1', color='green')
plt.plot(x_values, y3_values, label='3x + y = 5', color='red')

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
