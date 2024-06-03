import os
import shutil

print(os.getcwd())  # RUTA ACTUAL

shutil.move("x.txt", "C//X/X/X/X/X/X")

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {ruta}")
    print(f"las subcarpetas son: ")
    for sub in subcarpeta:
        print(sub)
    print(f"Los archivos son: ")
    for a in archivo:
        print({a})
              print("\n")
