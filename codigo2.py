import random
import time

# Base de datos simulada de usuarios

usuarios = {
    "ola": "ola123",
    "agricultor2": "5678"
}

# Función de login

def login():
    print("Sistema de Predicción de Sequías - Iniciar Sesión")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"Bienvenido, {usuario}!")
        return True
    else:
        print("Credenciales incorrectas. Inténtelo de nuevo.")
        return False

# Simulación de valores de temperatura del suelo y humedad del aire

def monitorear_clima():
    # Rango normal de temperatura (en grados Celsius)
    temperatura_suelo = random.uniform(15, 40)
    # Rango normal de humedad relativa (en porcentaje)
    humedad_aire = random.uniform(20, 80)
    return temperatura_suelo, humedad_aire

def evaluar_sequia(temperatura_suelo, humedad_aire):
    if temperatura_suelo > 35 and humedad_aire < 30:
        return True
    return False

# Proceso de login antes de empezar el monitoreo
intentos = 0
while intentos < 3:
    if login():
        break
    intentos += 1
    if intentos == 3:
        print("Demasiados intentos fallidos. El sistema se cerrará.")
        exit()

# Monitoreo del clima
while True:
    temp_suelo, hum_aire = monitorear_clima()
    print(f"Temperatura del suelo: {temp_suelo:.2f}°C, Humedad del aire: {hum_aire:.2f}%")
    
    if evaluar_sequia(temp_suelo, hum_aire):
        print("¡Alerta de sequía! Las condiciones son críticas para el cultivo.")
    else:
        print("Las condiciones climáticas son normales.")
    
    # Esperar 5 segundos antes de la siguiente simulación
    time.sleep(5)
