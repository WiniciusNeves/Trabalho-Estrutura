import numpy as np
import matplotlib.pyplot as plt

# Conjunto aberto, fechado e Limite
# Definir o eixo real
x = np.linspace(1, 3, 400)

# Conjuntos
conjunto_fechado = (x == 2)  # Fechado: {2}
conjunto_aberto = (x > 1) & (x < 2)  # Aberto: (1, 2)

plt.figure(figsize=(8, 4))

# Representar conjunto fechado {2}
plt.plot(x[conjunto_fechado], x[conjunto_fechado], 'go-', label='Conjunto Fechado {2}', markersize=5)

# Representar conjunto aberto (1, 2)
# plt.plot(x[conjunto_aberto], x[conjunto_aberto], 'bo', label='Conjunto Aberto (1, 2)', markersize=5)

# Adicionar linha para abertura (limite aberto)
plt.plot([1, 2, 3], [2, 2, 2], 'r-', label='Limite do Conjunto Aberto', linewidth=2)

# Adicionar detalhes ao gráfico
plt.title('Representação de Conjuntos Abertos e Fechados no Eixo Real')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(1, 3)
plt.ylim(1.5, 2.5)
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()

