#!/usr/bin/python3

import subprocess
import sys

def check_httpd_status():
    # Ejecutar el comando systemctl status httpd
    try:
        status_output = subprocess.check_output(['systemctl', 'status', 'httpd'], stderr=subprocess.STDOUT, text=True)
        if "Active: failed" in status_output:
            print("\033[92mhttpd caído, es normal para el lab\033[0m")  # Verde
        else:
            print("\033[91mHTTP está normal, hay que ajustarlo\033[0m")  # Rojo
    except subprocess.CalledProcessError as e:
        print(f"Error al verificar el estado de httpd: {e.output}")

def check_exportfs_status():
    # Ejecutar el comando exportfs -av
    try:
        exportfs_output = subprocess.check_output(['exportfs', '-av'], text=True)
        if "exporting 192.168.56.0/24:/home" in exportfs_output:
            print("El directorio /home está correctamente exportado.")
        else:
            print("El directorio /home no está exportado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al verificar los exports: {e.output}")

if __name__ == "__main__":
    check_httpd_status()
    check_exportfs_status()
