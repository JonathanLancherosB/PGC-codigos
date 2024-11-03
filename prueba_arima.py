import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simular datos climáticos
np.random.seed(42)
fechas = pd.date_range(start='2023-01-01', periods=250, freq='D')
temperatura_suelo = np.random.normal(loc=22, scale=3, size=len(fechas))  # Promedio 22°C
humedad_aire = np.random.normal(loc=45, scale=10, size=len(fechas))      # Promedio 45%

# Crear DataFrame
df = pd.DataFrame({
    'fecha': fechas,
    'temperatura_suelo': temperatura_suelo,
    'humedad_aire': humedad_aire
})

# Configuración de estilo
plt.style.use('dark_background')  
plt.rcParams['figure.facecolor'] = '#2e2e2e'  
plt.rcParams['axes.facecolor'] = '#2e2e2e'  
plt.rcParams['font.family'] = 'Comic Sans MS'  
plt.rcParams['axes.labelcolor'] = 'white'  
plt.rcParams['axes.titlesize'] = 16  
plt.rcParams['axes.titlecolor'] = 'white'  

# Crear la primera figura para temperatura y humedad
fig, axs = plt.subplots(2, 1, figsize=(14, 10))

# Gráfica de la temperatura del suelo
axs[0].plot(df['fecha'], df['temperatura_suelo'], label='Temperatura del Suelo', color='orange', lw=2)
axs[0].fill_between(df['fecha'], df['temperatura_suelo'], color='orange', alpha=0.2)
axs[0].axhline(y=25, color='red', linestyle='--', label='Umbral de Sequía (25°C)', lw=2)
axs[0].set_title('Simulación de la Temperatura del Suelo')
axs[0].set_xlabel('Fecha')
axs[0].set_ylabel('Temperatura (°C)')
axs[0].legend(loc='upper right')

# Gráfica de la humedad del aire
axs[1].plot(df['fecha'], df['humedad_aire'], label='Humedad del Aire', color='blue', lw=2)
axs[1].fill_between(df['fecha'], df['humedad_aire'], color='blue', alpha=0.2)
axs[1].axhline(y=40, color='red', linestyle='--', label='Umbral de Sequía (40%)', lw=2)
axs[1].set_title('Simulación de la Humedad del Aire')
axs[1].set_xlabel('Fecha')
axs[1].set_ylabel('Humedad (%)')
axs[1].legend(loc='upper right')

# Ajustar el espaciado entre subgráficas
plt.tight_layout()

# Mostrar la primera gráfica
plt.show()
# Clasificación de sequías: Si la temperatura > 25°C y la humedad < 40%, se considera sequía
condicion_sequia = np.where((temperatura_suelo > 25) & (humedad_aire < 40), 'Sequía', 'Normal')

# Añadir la condición de sequía al DataFrame
df['condicion_sequia'] = condicion_sequia

# Configuración de estilo para la segunda gráfica
plt.style.use('dark_background')  
plt.rcParams['figure.facecolor'] = '#2e2e2e'
plt.rcParams['axes.facecolor'] = '#2e2e2e'
plt.rcParams['font.family'] = 'Comic Sans MS'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.titlecolor'] = 'white'  

# Crear la segunda figura para predicción de sequías
plt.figure(figsize=(14, 6))
plt.plot(df['fecha'], df['condicion_sequia'], label='Condición del Clima', color='green', lw=2)
sequias = df[df['condicion_sequia'] == 'Sequía']
plt.scatter(sequias['fecha'], sequias['condicion_sequia'], color='red', label='Sequías', zorder=5)
plt.title('Predicción de Sequías Basada en Condiciones Climáticas')
plt.xlabel('Fecha')
plt.ylabel('Condición')
plt.legend(loc='upper right')

# Mostrar la segunda gráfica
plt.show()
