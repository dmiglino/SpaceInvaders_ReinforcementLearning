@echo off
echo Instalando atari-py usando conda...
call conda install -y -c conda-forge atari_py
echo.
echo Si la instalacion con conda fallo, intentando con pip...
call pip install git+https://github.com/openai/atari-py.git
echo.
echo Instalacion completada. Presiona cualquier tecla para salir.
pause
