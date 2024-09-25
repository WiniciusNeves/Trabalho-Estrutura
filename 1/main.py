import numpy as np
import matplotlib.pyplot as plt
# Conjunto aberto, fechado e Limite
# Definir o eixo real
x = np.linspace(-1, 4, 400)

# Conjuntos
conjunto_fechado = (0 <= x) & (x <= 1)  # Fechado: [0, 1]
conjunto_aberto = (2 < x) & (x < 3)  # Aberto: (2, 3)

plt.figure(figsize=(8, 4))

# Representar conjunto fechado [0, 1]
plt.plot(x[conjunto_fechado], x[conjunto_fechado], 'go-', label='Conjunto Fechado [0, 1]', markersize=5)

# Representar conjunto aberto (2, 3)
plt.plot(x[conjunto_aberto], x[conjunto_aberto], 'bo', label='Conjunto Aberto (2, 3)', markersize=5)

# Adicionar pontos para abertura (limite aberto)
plt.plot(2, 2, 'ro', label='Limite do Conjunto Aberto', markersize=8, fillstyle='none')
plt.plot(3, 3, 'ro', markersize=8, fillstyle='none')

# Adicionar detalhes ao gráfico
plt.title('Representação de Conjuntos Abertos e Fechados no Eixo Real')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-1, 4)
plt.ylim(-0.5, 3)
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()
