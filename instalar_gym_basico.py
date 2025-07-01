"""
Script para instalar gym básico sin atari-py
Este script instala solo los paquetes necesarios para ejecutar el notebook APR_Grupo_9_simple_env.ipynb
que usa CartPole-v1 en lugar de SpaceInvaders-v0
"""

import sys
import subprocess
import os

def instalar_paquetes():
    print("Instalando paquetes básicos para gym (sin atari-py)...")
    
    # Lista de paquetes a instalar
    paquetes = [
        "gym==0.17.3",
        "pyglet==1.5.0",
        "h5py==3.1.0",
        "Pillow==9.5.0",
        "keras-rl2==1.0.5",
        "tensorflow==2.5.3"
    ]
    
    # Instalar cada paquete
    for paquete in paquetes:
        print(f"\nInstalando {paquete}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
            print(f"✓ {paquete} instalado correctamente")
        except subprocess.CalledProcessError:
            print(f"✗ Error al instalar {paquete}")
    
    print("\nInstalación completada.")
    print("Ahora puedes ejecutar el notebook APR_Grupo_9_simple_env.ipynb")

if __name__ == "__main__":
    instalar_paquetes()
    input("\nPresiona Enter para salir...")
