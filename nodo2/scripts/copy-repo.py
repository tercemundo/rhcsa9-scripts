#!/usr/bin/python3

import shutil
import os
import sys

def copiar_directorio(src, dst):
    """Copia un directorio de origen a un directorio de destino."""
    try:
        # Verificar si el directorio de origen existe
        if not os.path.exists(src):
            print(f"El directorio de origen '{src}' no existe.")
            sys.exit(1)

        # Copiar el directorio
        shutil.copytree(src, dst)
        print(f"Directorio '{src}' copiado a '{dst}' con éxito.")
    except Exception as e:
        print(f"Error al copiar el directorio: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Definir las rutas de origen y destino
    ruta_origen = "/usr/local/balinux/text2pdf"
    ruta_destino = "/var/www/html/text2pdf"

    # Copiar el directorio
    copiar_directorio(ruta_origen, ruta_destino)
