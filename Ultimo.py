import random
import time
import csv

# Base de datos simulada de usuarios
usuarios = {
    "ola": "ola123",
    "sr.gacha": "elgacha123"
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

# Función de registro de nuevos usuarios
def registrar():
    print("Registro de nuevo usuario")
    nuevo_usuario = input("Nombre de usuario: ")
    if nuevo_usuario in usuarios:
        print("El usuario ya existe. Intente con otro nombre.")
        return False
    nueva_contraseña = input("Contraseña: ")
    usuarios[nuevo_usuario] = nueva_contraseña
    print(f"Usuario {nuevo_usuario} registrado exitosamente.")
    return True

# Simulación de valores de temperatura del suelo y humedad del aire
def monitorear_clima():
    # Rango normal de temperatura (en grados Celsius)
    temperatura_suelo = random.uniform(15, 40)
    # Rango normal de humedad relativa (en porcentaje)
    humedad_aire = random.uniform(20, 80)
    return temperatura_suelo, humedad_aire

# Evaluar si las condiciones indican sequía
def evaluar_sequia(temperatura_suelo, humedad_aire):
    if temperatura_suelo > 35 and humedad_aire < 30:
        return True
    return False

# Guardar resultados de monitoreo en un archivo CSV
def guardar_log(temp_suelo, hum_aire, alerta):
    with open('log_monitoreo.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), temp_suelo, hum_aire, alerta])

# Mostrar el historial de alertas
def ver_historial():
    try:
        with open('log_monitoreo.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\n--- Historial de Monitoreo ---")
            for row in reader:
                print(f"{row[0]} - Temperatura: {row[1]}°C, Humedad: {row[2]}%, Alerta: {row[3]}")
    except FileNotFoundError:
        print("No hay historial disponible. Aún no se ha registrado ningún monitoreo.")

# Proceso de login y/o registro
def iniciar_sesion():
    while True:
        print("\n1. Iniciar sesión\n2. Registrar nuevo usuario\n3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            if login():
                break
        elif opcion == "2":
            registrar()
        elif opcion == "3":
            exit()
        else:
            print("Opción no válida.")

# Menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar monitoreo")
        print("2. Ver historial de alertas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_monitoreo()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Función principal de monitoreo
def iniciar_monitoreo():
    while True:
        temp_suelo, hum_aire = monitorear_clima()
        alerta_sequia = evaluar_sequia(temp_suelo, hum_aire)
        alerta = "Sí" if alerta_sequia else "No"
        print(f"Temperatura del suelo: {temp_suelo:.2f}°C, Humedad del aire: {hum_aire:.2f}%, Alerta: {alerta}")
        
        # Guardar log de monitoreo
        guardar_log(temp_suelo, hum_aire, alerta)
        
        continuar = input("¿Desea continuar monitoreando? (s/n): ").lower()
        if continuar != 's':
            break
        time.sleep(5)  # Esperar 5 segundos antes de la próxima lectura

# Iniciar el programa
if __name__ == "__main__":
    iniciar_sesion()
    menu_principal()
