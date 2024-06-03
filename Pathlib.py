from pathlib import Path, PureWindowsPath

carpeta = Path('C:\\Users\\evazquez\\Desktop\\DIR PY')

if not carpeta.exists():
    print("NO EXISTE")
else:
    print("EXISTE")

ruta_win =PureWindowsPath(carpeta)
print(ruta_win)