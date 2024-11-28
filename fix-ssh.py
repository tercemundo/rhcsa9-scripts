#!/usr/bin/python3


import os
import shutil
import subprocess

# Check if the script is running as root
if os.geteuid() != 0:
    print("This script must be run as root.")
    exit(1)

# Define source and destination paths
source_file = '/usr/local/balinux/sshd_config'
destination_file = '/etc/ssh/sshd_config'

# Copy the source file to the destination, overwriting if it exists
shutil.copy2(source_file, destination_file)

# Restart the SSH service
subprocess.run(['systemctl', 'restart', 'sshd'])

print("File copied and SSH service restarted successfully.")
