# Sistema básico para análisis de datos meteorológicos sin librerías externas

# Función de login
def login():
    usuarios = {
        "sr.gacha": "elgacha",
        "usuario1": "password1"
    }
    
    print("Bienvenido al sistema de análisis de datos meteorológicos ENMA")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Acceso concedido")
        return True
    else:
        print("Acceso denegado")
        return False

# Recolección de datos meteorológicos simulados
def recolectar_datos():
    dias = int(input("¿Cuántos días de datos deseas ingresar? "))
    temperatura_suelo = []
    humedad_relativa = []

    for i in range(dias):
        print(f"\nDía {i + 1}:")
        temp = float(input("Ingrese la temperatura del suelo (°C): "))
        humedad = float(input("Ingrese la humedad relativa (%): "))
        temperatura_suelo.append(temp)
        humedad_relativa.append(humedad)
    
    return temperatura_suelo, humedad_relativa

# Análisis básico de los datos
def analizar_datos(temperatura_suelo, humedad_relativa):
    # Calcular promedio
    temp_promedio = sum(temperatura_suelo) / len(temperatura_suelo)
    humedad_promedio = sum(humedad_relativa) / len(humedad_relativa)
    
    print(f"\n--- Resumen de Datos ---")
    print(f"Promedio de la temperatura del suelo: {temp_promedio:.2f}°C")
    print(f"Promedio de la humedad relativa: {humedad_promedio:.2f}%")
    
    # Análisis básico
    if temp_promedio > 25 and humedad_promedio < 50:
        print("Alerta: Condiciones de sequía posibles.")
    else:
        print("Condiciones climáticas normales.")

# Main
if login():
    temperatura, humedad = recolectar_datos()
    analizar_datos(temperatura, humedad)
else:
    print("El sistema se cerrará.")
