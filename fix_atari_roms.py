"""
Script para arreglar la instalación de atari-py y los ROMs de Atari
Este script intenta solucionar problemas comunes con atari-py y los ROMs de Atari
"""

import os
import sys
import subprocess
import shutil
import tempfile
import zipfile
from pathlib import Path
import urllib.request

def descargar_archivo(url, destino):
    print(f"Descargando {url}...")
    try:
        urllib.request.urlretrieve(url, destino)
        print(f"✓ Descargado correctamente a {destino}")
        return True
    except Exception as e:
        print(f"✗ Error al descargar: {e}")
        return False

def instalar_atari_py():
    print("\n1. Intentando instalar atari-py desde el fork de OpenAI...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/openai/atari-py.git"])
        print("✓ atari-py instalado correctamente")
        return True
    except subprocess.CalledProcessError:
        print("✗ Error al instalar atari-py desde OpenAI")
        
        print("\nIntentando instalar atari-py desde PyPI...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "atari-py==0.2.6"])
            print("✓ atari-py instalado correctamente desde PyPI")
            return True
        except subprocess.CalledProcessError:
            print("✗ Error al instalar atari-py desde PyPI")
            return False

def instalar_roms():
    print("\n2. Instalando ROMs de Atari...")
    
    # Crear directorio temporal
    temp_dir = tempfile.mkdtemp()
    rom_zip = os.path.join(temp_dir, "roms.zip")
    
    # URL de los ROMs de Atari
    rom_url = "http://www.atarimania.com/roms/Roms.zip"
    
    # Descargar ROMs
    if not descargar_archivo(rom_url, rom_zip):
        rom_url = "https://s3.amazonaws.com/atari-roms/Roms.zip"
        if not descargar_archivo(rom_url, rom_zip):
            print("✗ No se pudieron descargar los ROMs de Atari")
            return False
    
    # Extraer ROMs
    try:
        print("Extrayendo ROMs...")
        with zipfile.ZipFile(rom_zip, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        print("✓ ROMs extraídos correctamente")
    except Exception as e:
        print(f"✗ Error al extraer ROMs: {e}")
        return False
    
    # Buscar directorio de atari_py
    try:
        import atari_py
        atari_py_path = os.path.dirname(atari_py.__file__)
        rom_dir = os.path.join(atari_py_path, "atari_roms")
        print(f"Directorio de ROMs de atari-py: {rom_dir}")
        
        # Crear directorio si no existe
        os.makedirs(rom_dir, exist_ok=True)
        
        # Copiar ROMs
        roms_encontrados = 0
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.endswith(".bin"):
                    src = os.path.join(root, file)
                    dst = os.path.join(rom_dir, file.lower())
                    shutil.copy2(src, dst)
                    roms_encontrados += 1
        
        print(f"✓ {roms_encontrados} ROMs copiados a {rom_dir}")
        return True
    except Exception as e:
        print(f"✗ Error al instalar ROMs: {e}")
        return False
    finally:
        # Limpiar directorio temporal
        shutil.rmtree(temp_dir, ignore_errors=True)

def verificar_instalacion():
    print("\n3. Verificando instalación...")
    try:
        import atari_py
        print("✓ atari_py importado correctamente")
        
        juegos = atari_py.list_games()
        print(f"✓ Juegos disponibles: {len(juegos)}")
        print(f"Primeros 5 juegos: {juegos[:5]}")
        
        if "space_invaders" in juegos:
            print("✓ Space Invaders disponible")
            return True
        else:
            print("✗ Space Invaders no disponible")
            return False
    except Exception as e:
        print(f"✗ Error al verificar instalación: {e}")
        return False

def main():
    print("=== ARREGLANDO ATARI-PY Y ROMS DE ATARI ===")
    
    if instalar_atari_py() and instalar_roms() and verificar_instalacion():
        print("\n✅ INSTALACIÓN COMPLETADA CORRECTAMENTE")
        print("Ahora puedes ejecutar el notebook APR_Grupo_9_fixed.ipynb")
    else:
        print("\n❌ INSTALACIÓN INCOMPLETA")
        print("Intenta usar el notebook alternativo APR_Grupo_9_simple_env.ipynb")
    
    print("\nPresiona Enter para salir...")
    input()

if __name__ == "__main__":
    main()
