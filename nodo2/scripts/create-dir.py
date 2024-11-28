#!/usr/bin/python3

import os
import sys

def crear_directorio(ruta):
    """Crea un directorio en la ruta especificada si no existe."""
    try:
        # Crear el directorio y sus padres si no existen
        os.makedirs(ruta, exist_ok=True)
        print(f"Directorio '{ruta}' creado o ya existe.")
    except Exception as e:
        print(f"Error al crear el directorio: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Definir la ruta del directorio a crear
    ruta_directorio = "/export/home"
    
    # Crear el directorio
    crear_directorio(ruta_directorio)
