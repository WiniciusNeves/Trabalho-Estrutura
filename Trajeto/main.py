import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definindo a função da trajetória do projétil
def projectile_motion(t, v0, theta):
    g = 9.81  # aceleração da gravidade (m/s²)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - (0.5 * g * t**2)
    return x, y

# Gerar dados simulados
v0 = 50  # velocidade inicial (m/s)
theta = np.radians(45)  # ângulo de lançamento (graus)
t_values = np.linspace(0, 10, 100)  # tempos (s)

# Calcular posições (x, y)
x_data, y_data = projectile_motion(t_values, v0, theta)

# Adicionando um pouco de ruído aos dados para simular medições reais
np.random.seed(42)
y_data_noisy = y_data + np.random.normal(scale=5, size=y_data.shape)

# Função de ajuste para regressão não linear
def fit_function(t, v0, theta):
    g = 9.81
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - (0.5 * g * t**2)
    return y

# Ajustar o modelo aos dados com curve_fit
params, _ = curve_fit(fit_function, t_values, y_data_noisy, p0=[v0, theta])

# Parâmetros ajustados
v0_fit, theta_fit = params

# Gerar dados ajustados
y_fit = fit_function(t_values, v0_fit, theta_fit)

# Visualizar os resultados
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data_noisy, color='red', label='Dados com Ruído', s=10)
plt.plot(x_data, y_fit, color='blue', label='Ajuste da Trajetória', linewidth=2)
plt.title('Trajetória de um Projétil com Ajuste de Regressão Não Linear')
plt.xlabel('Distância (m)')
plt.ylabel('Altura (m)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.show()

# Exibir parâmetros ajustados
print(f'Velocidade Inicial Ajustada: {v0_fit:.2f} m/s')
print(f'Ângulo de Lançamento Ajustado: {np.degrees(theta_fit):.2f} graus')
