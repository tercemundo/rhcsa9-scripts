#!/usr/bin/python3

import os
import shutil
import glob

def copiar_repositorios():
    """Copiar archivos .repo desde /etc/yum.repos.d/bkp a /etc/yum.repos.d/."""
    dir_origen = '/etc/yum.repos.d/bkp/'
    dir_destino = '/etc/yum.repos.d/'

    # Obtener todos los archivos .repo en el directorio de origen
    archivos_repo = glob.glob(os.path.join(dir_origen, '*.repo'))

    # Copiar cada archivo al directorio de destino
    for archivo in archivos_repo:
        shutil.copy(archivo, dir_destino)
        print(f'Copiado: {archivo} a {dir_destino}')

def borrar_myrepo():
    """Borrar el archivo myrepo.repo."""
    archivo_myrepo = '/etc/yum.repos.d/myrepo.repo'

    if os.path.exists(archivo_myrepo):
        os.remove(archivo_myrepo)
        print(f'Borrado: {archivo_myrepo}')
    else:
        print(f'El archivo {archivo_myrepo} no existe.')

if __name__ == "__main__":
    copiar_repositorios()
    borrar_myrepo()

