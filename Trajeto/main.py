import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# Carregar o arquivo "projeteis.csv" com os dados de projétil
data = pd.read_csv('Trajeto/projeteis.csv')

# Função de movimento do projétil
def projectile_motion(t, v0, theta):
    g = 9.81  # aceleração da gravidade (m/s²)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - (0.5 * g * t**2)
    return x, y

# Configurar ângulo e tempo
theta = np.radians(45)
t_values = np.linspace(0, 10, 100)

# Definir limite de projéteis
limite = 156  # Alterar para limitar o número de projéteis

# Configurar o gráfico
plt.figure(figsize=(14, 8))
plt.title('Trajetória de Projéteis: Ajuste com Regressão e Rede Neural')
plt.xlabel('Distância (m)')
plt.ylabel('Altura (m)')

# Loop para projetar cada trajetória no mesmo gráfico
for i, (index, row) in enumerate(data.iterrows()):
    if i >= limite:
        break
    
    v0 = row['V0']
    x_data, y_data = projectile_motion(t_values, v0, theta)
    
    # Adicionar ruído
    np.random.seed(42)
    y_data_noisy = y_data + np.random.normal(scale=5, size=y_data.shape)
    
    # Normalizar os dados
    t_values_norm = (t_values - np.mean(t_values)) / np.std(t_values)
    y_data_noisy_norm = (y_data_noisy - np.mean(y_data_noisy)) / np.std(y_data_noisy)
    
    # Dividir em treino e teste
    t_train, t_test, y_train, y_test = train_test_split(
        t_values_norm.reshape(-1, 1), y_data_noisy_norm, test_size=0.2, random_state=42
    )
    
    # Ajuste parabólico com curve_fit
    def parabola(t, a, b, c):
        return a * t**2 + b * t + c
    
    params, _ = curve_fit(parabola, t_train.flatten(), y_train, p0=[-0.5 * 9.81, v0 * np.sin(theta), 0])
    y_fit = parabola(t_values_norm, *params)
    
    # Rede neural para ajuste
    model_nn = Sequential([
        Dense(64, activation='relu', input_shape=(1,)),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        Dense(1)
    ])
    model_nn.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    model_nn.fit(t_train, y_train, epochs=100, batch_size=10, verbose=0)
    
    # Previsões da rede neural
    y_nn_fit_norm = model_nn.predict(t_values_norm.reshape(-1, 1)).flatten()
    y_nn_fit = y_nn_fit_norm * np.std(y_data_noisy) + np.mean(y_data_noisy)
    
    # Plot de dados com ajuste no mesmo gráfico
    plt.plot(x_data, y_data_noisy, color='gray', linestyle='--', linewidth=0.5, alpha=0.5, label='Dados com Ruído' if i == 0 else "")
    plt.plot(x_data, y_fit * np.std(y_data_noisy) + np.mean(y_data_noisy), color='blue', linewidth=0.7, label='Ajuste com Regressão' if i == 0 else "")
    plt.plot(x_data, y_nn_fit, color='green', linewidth=0.7, label='Ajuste com Rede Neural' if i == 0 else "")

# Legenda para diferenciar as curvas
plt.legend()
plt.grid()
plt.show()
