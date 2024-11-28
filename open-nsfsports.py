#!/usr/bin/python3

import subprocess

def abrir_puertos():
    """Abrir puertos necesarios para NFS en el firewall."""
    try:
        # Abrir el puerto 2049 para NFS
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=2049/tcp'], check=True)
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=2049/udp'], check=True)

        # Abrir el puerto 111 para rpcbind
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=111/tcp'], check=True)
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=111/udp'], check=True)

        # Abrir el puerto 20048 para mountd
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=20048/tcp'], check=True)
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=20048/udp'], check=True)

        # Abrir puertos adicionales para rpc.statd (opcional)
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=32764-32767/tcp'], check=True)
        subprocess.run(['firewall-cmd', '--permanent', '--add-port=32764-32767/udp'], check=True)

        # Recargar la configuración del firewall
        subprocess.run(['firewall-cmd', '--reload'], check=True)
        
        print("Puertos abiertos y configuración del firewall recargada.")

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar comando: {e}")

def reiniciar_servicios():
    """Reiniciar los servicios NFS y rpcbind."""
    try:
        subprocess.run(['systemctl', 'restart', 'nfs-server'], check=True)
        subprocess.run(['systemctl', 'restart', 'rpcbind'], check=True)
        
        print("Servicios NFS y rpcbind reiniciados.")

    except subprocess.CalledProcessError as e:
        print(f"Error al reiniciar servicios: {e}")

if __name__ == "__main__":
    abrir_puertos()
    reiniciar_servicios()
