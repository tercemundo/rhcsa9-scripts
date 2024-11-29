#!/usr/bin/python3

import subprocess
import os
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"No se puede reiniciar httpd")
        print(f"Error: {e.stderr}")
        sys.exit(1)

# Verificar si httpd está instalado
def check_httpd_installed():
    try:
        subprocess.run(["rpm", "-q", "httpd"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

# Instalar httpd si no está instalado
if not check_httpd_installed():
    run_command("yum -y install httpd")

# Cambiar el puerto en httpd.conf
with open("/etc/httpd/conf/httpd.conf", "r") as f:
    contenido = f.read()

contenido_modificado = contenido.replace("Listen 80", "Listen 82")

with open("/etc/httpd/conf/httpd.conf", "w") as f:
    f.write(contenido_modificado)

# Reiniciar httpd
run_command("systemctl restart httpd")

print("Configuración de httpd completada exitosamente.")
