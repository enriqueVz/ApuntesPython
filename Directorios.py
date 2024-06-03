import os
from pathlib import Path

ruta = os.getcwd() #CURRENT WORKING DIRECTORY
print(ruta)

ruta1 = os.chdir('C:\\Users\\evazquez\\Desktop\\DIR PY')
archivo = open('XD.txt')
print(archivo.read())

os.rmdir('RUTA') #pa borrar dirs

otro_arch = open('C:\\Users\\evazquez\\Desktop\\DIR PY')
print(otro_arch.read())


carpeta = Path('C:\\Users\\evazquez\\Desktop\\DIR PY') #PA TOS LOS SO
archivo = carpeta / 'otro_arch.txt'

