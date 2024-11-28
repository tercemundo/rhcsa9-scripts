#!/usr/bin/python3
import os
import subprocess

# Verificar si el script se ejecuta como root
if os.geteuid() != 0:
    print("Este script debe ser ejecutado como root.")
    exit(1)

try:
    # Instalar nfs-utils
    print("Instalando nfs-utils...")
    subprocess.run(['yum', '-y', 'install', 'nfs-utils'], check=True)
    print("Instalación de nfs-utils completada.")

    # Definir la línea a agregar
    line_to_add = "/home 192.168.56.0/24(rw,sync,no_root_squash)\n"

    # Ruta del archivo /etc/exports
    exports_file = '/etc/exports'

    # Agregar la línea al archivo /etc/exports
    with open(exports_file, 'a') as file:
        file.write(line_to_add)
    print("La línea se ha agregado correctamente a /etc/exports.")

except subprocess.CalledProcessError as e:
    print(f"Error al instalar nfs-utils: {e}")
    exit(1)
except Exception as e:
    print(f"Ocurrió un error: {e}")
    exit(1)
