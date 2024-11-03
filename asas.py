import pandas as pd

# Intenta leer el archivo directamente
try:
    df = pd.read_csv('datos_climaticos.csv')
    print(df.head())  # Muestra las primeras filas del dataframe
except Exception as e:
    print(f"Ocurrió un error: {e}")
