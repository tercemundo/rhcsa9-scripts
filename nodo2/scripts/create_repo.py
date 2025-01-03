#!/usr/bin/python3
import os
import subprocess

# Función para instalar los servicios preliminares
def preparar_entorno():
    try:
        # Instalar Apache
        print("Instalando Apache...")
        subprocess.run(['yum', '-y', 'install', 'httpd'], check=True)

        # Configurar firewall
        print("Configurando firewall...")
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=80/tcp'], check=True)
        subprocess.run(['firewall-cmd', '--reload'], check=True)

        # Crear directorio y copiar RPM
        print("Creando directorio y copiando RPM...")
        os.makedirs('/usr/local/balinux', exist_ok=True)
        subprocess.run(['cp', '/root/rhcsa9-scripts/rpmbuild/RPMS/x86_64/hola-1.0-1.el9.x86_64.rpm', '/usr/local/balinux/hola-1.0.rpm'], check=True)

        print("Entorno preparado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al preparar el entorno: {e}")

# Función para instalar createrepo
def instalar_createrepo():
    try:
        # Intentar instalar createrepo
        print("Instalando createrepo...")
        subprocess.run(['yum', '-y', 'install', 'createrepo'], check=True)
        print("createrepo instalado correctamente.")
    except subprocess.CalledProcessError:
        print("Error al intentar instalar createrepo.")

# Cambiar el puerto de Apache
def cambiar_puerto_apache():
    archivo_conf = '/etc/httpd/conf/httpd.conf'
    # Leer el archivo de configuración
    with open(archivo_conf, 'r') as file:
        lineas = file.readlines()
    # Modificar la línea que contiene "Listen 82"
    with open(archivo_conf, 'w') as file:
        for linea in lineas:
            if 'Listen 82' in linea:
                linea = linea.replace('Listen 82', 'Listen 80')
            file.write(linea)
    # Reiniciar Apache para aplicar cambios
    subprocess.run(['systemctl', 'restart', 'httpd'], check=True)
    print("Puerto de Apache cambiado a 80 y servicio reiniciado.")

# Crear repositorio y copiar el paquete RPM
def crear_repositorio():
    ruta_repo = '/var/www/html/repo'
    paquete_rpm = '/usr/local/balinux/hola-1.0.rpm'
    # Crear el directorio del repositorio si no existe
    os.makedirs(ruta_repo, exist_ok=True)
    # Copiar el paquete RPM al repositorio
    subprocess.run(['cp', paquete_rpm, ruta_repo], check=True)
    # Crear el repositorio usando createrepo
    subprocess.run(['createrepo', ruta_repo], check=True)
    print("Repositorio creado y paquete RPM indexado.")

if __name__ == "__main__":
    # Ejecutar las funciones
    preparar_entorno()
    instalar_createrepo()
    cambiar_puerto_apache()
    crear_repositorio()
