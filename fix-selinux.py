#!/usr/bin/python3
import os
import re

# Verificar si el script se ejecuta como root
if os.geteuid() != 0:
    print("Este script debe ser ejecutado como root.")
    exit(1)

# Rutas de los archivos de configuración
selinux_config_file = '/etc/selinux/config'
grub_config_files = [
    '/etc/grub2.cfg', 
    '/boot/grub2/grub.cfg'
]

# Modificar configuración de SELinux
try:
    # Leer el contenido del archivo de SELinux
    with open(selinux_config_file, 'r') as file:
        selinux_lines = file.readlines()

    # Modificar la línea que establece el modo de SELinux
    for i in range(len(selinux_lines)):
        if selinux_lines[i].startswith('SELINUX='):
            selinux_lines[i] = 'SELINUX=enforcing\n'
            break

    # Escribir los cambios de vuelta en el archivo de SELinux
    with open(selinux_config_file, 'w') as file:
        file.writelines(selinux_lines)

    # Modificar configuración de Grub en ambos archivos
    for grub_config_file in grub_config_files:
        try:
            # Leer el contenido del archivo de Grub
            with open(grub_config_file, 'r') as file:
                grub_lines = file.readlines()

            # Modificar la línea de kernelopts
            for i in range(len(grub_lines)):
                if 'set kernelopts=' in grub_lines[i]:
                    # Usamos regex para reemplazar solo la parte de kernelopts
                    grub_lines[i] = re.sub(
                        r'set kernelopts=".*?"', 
                        'set kernelopts="root=UUID=bc8391f4-d4a4-40c8-a0d1-fe4e7cbbd31e rw"', 
                        grub_lines[i]
                    )
                    break

            # Escribir los cambios de vuelta en el archivo de Grub
            with open(grub_config_file, 'w') as file:
                file.writelines(grub_lines)

        except FileNotFoundError:
            print(f"El archivo {grub_config_file} no existe. Saltando...")
        except PermissionError:
            print(f"No se tienen permisos para modificar {grub_config_file}. Saltando...")
        except Exception as e:
            print(f"Ocurrió un error al modificar {grub_config_file}: {e}")

    # Regenerar la configuración de Grub (en sistemas basados en RHEL/CentOS)
    os.system('grub2-mkconfig -o /boot/grub2/grub.cfg')

    # Reiniciar el sistema para aplicar los cambios
    os.system('reboot')

except Exception as e:
    print(f"Ocurrió un error general: {e}")
    exit(1)
