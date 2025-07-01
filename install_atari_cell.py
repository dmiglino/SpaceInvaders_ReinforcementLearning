# Celda de instalación actualizada para APR_Grupo_9_fixed.ipynb
# Copiar y pegar este código en la celda de instalación del notebook

# ejecutar solo la primera vez..

if IN_COLAB:
  %pip install gym==0.17.3
  %pip install git+https://github.com/openai/atari-py.git
  %pip install keras-rl2==1.0.5
  %pip install tensorflow==2.12
else:
  %pip install gym==0.17.3
  %pip install git+https://github.com/openai/atari-py.git
  %pip install pyglet==1.5.0
  %pip install h5py==3.1.0
  %pip install Pillow==9.5.0
  %pip install keras-rl2==1.0.5
  %pip install Keras==2.2.4
  %pip install tensorflow==2.5.3
  %pip install torch==2.0.1
  %pip install agents==1.4.0
