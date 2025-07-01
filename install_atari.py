# Script para instalar atari-py usando conda
# Ejecutar este script antes de abrir el notebook

import os
import sys

# Verificar si conda está disponible
try:
    # Intentar instalar atari-py usando conda
    print("Instalando atari-py usando conda...")
    os.system("conda install -y -c conda-forge atari_py")
    
    # Verificar la instalación
    try:
        import atari_py
        print("atari_py instalado correctamente")
        print("Juegos disponibles:", atari_py.list_games()[:5], "...")
    except ImportError:
        print("Error: No se pudo importar atari_py después de la instalación con conda")
        
        # Intentar instalar con pip usando el fork de OpenAI
        print("Intentando instalar con pip usando el fork de OpenAI...")
        os.system("pip install git+https://github.com/openai/atari-py.git")
        
        try:
            import atari_py
            print("atari_py instalado correctamente con pip")
        except ImportError:
            print("Error: La instalación con pip también falló")
            print("Por favor, instale atari-py manualmente")
            sys.exit(1)
            
except Exception as e:
    print(f"Error al instalar atari-py: {e}")
    print("Por favor, instale atari-py manualmente usando:")
    print("conda install -y -c conda-forge atari_py")
    print("o")
    print("pip install atari-py")
    sys.exit(1)

print("\nInstalación completada con éxito. Ahora puede ejecutar el notebook APR_Grupo_9_fixed.ipynb")
