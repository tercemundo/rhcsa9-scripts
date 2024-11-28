#!/usr/bin/python3

import subprocess
import sys

def crear_usuario(nombre_usuario, uid, home_dir):
    """Crea un usuario en el sistema con el nombre, UID y directorio home especificados."""
    try:
        # Ejecutar el comando useradd
        subprocess.run(['useradd', '-m', '-u', str(uid), '-d', home_dir, nombre_usuario], check=True)
        print(f"Usuario '{nombre_usuario}' creado con UID {uid} y directorio home '{home_dir}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el usuario: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Definir el nombre de usuario, UID y directorio home
    nombre_usuario = "qq"
    uid = 1060
    home_dir = "/export/home/qq"
    
    # Crear el usuario
    crear_usuario(nombre_usuario, uid, home_dir)
