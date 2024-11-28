#!/usr/bin/python3

import subprocess
import sys

def crear_usuario(nombre_usuario, uid):
    """Crea un usuario en el sistema con el nombre y UID especificados."""
    try:
        # Ejecutar el comando useradd
        subprocess.run(['useradd', '-m', '-u', str(uid), nombre_usuario], check=True)
        print(f"Usuario '{nombre_usuario}' creado con UID {uid}.")
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el usuario: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Definir el nombre de usuario y UID
    nombre_usuario = "qq"
    uid = 1060
    
    # Crear el usuario
    crear_usuario(nombre_usuario, uid)
