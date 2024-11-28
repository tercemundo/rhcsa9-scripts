#!/usr/bin/python3

import os

# Verificar si el script se ejecuta como root
if os.geteuid() != 0:
    print("Este script debe ser ejecutado como root.")
    exit(1)

# Definir la línea a agregar
line_to_add = "/home 192.168.56.0/24(rw,sync,no_root_squash)\n"

# Ruta del archivo /etc/exports
exports_file = '/etc/exports'

# Agregar la línea al archivo /etc/exports
with open(exports_file, 'a') as file:
    file.write(line_to_add)

print("La línea se ha agregado correctamente a /etc/exports.")
