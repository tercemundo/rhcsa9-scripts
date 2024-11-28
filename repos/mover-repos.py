#!/usr/bin/python3

import os
import shutil
import glob

def copiar_repositorios_y_borrar():
    # Definir el directorio de origen y el de destino
    dir_origen = '/etc/yum.repos.d/'
    dir_destino = os.path.join(dir_origen, 'bkp')

    # Crear el directorio de destino si no existe
    os.makedirs(dir_destino, exist_ok=True)

    # Obtener todos los archivos .repo en el directorio de origen
    archivos_repo = glob.glob(os.path.join(dir_origen, '*.repo'))

    # Copiar cada archivo al directorio de destino
    for archivo in archivos_repo:
        shutil.copy(archivo, dir_destino)
        print(f'Copiado: {archivo} a {dir_destino}')

    # Borrar todos los archivos .repo del directorio de origen
    for archivo in archivos_repo:
        os.remove(archivo)
        print(f'Borrado: {archivo}')

if __name__ == "__main__":
    copiar_repositorios_y_borrar()

