
import pandas as pd
import os
import datetime
from sqlalchemy import create_engine


server = 'kikeejercicio.database.windows.net'
database = 'kikeejercicio'
username = 'kike'
password = 'Lalaquique1!'
driver = 'ODBC Driver 18 for SQL Server'  # Puedes necesitar ajustar el controlador según tu instalación
connection_string = f'mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver={driver.replace(" ", "+")}'


# Crea el motor de SQLAlchemy
engine = create_engine(connection_string)


# Ruta del archivo CSV
csv_file = 'script_del_titanic_peli.csv'
csv_path = os.path.abspath(csv_file)

# Leer el archivo CSV
df = pd.read_csv(csv_path, names=['Línea', 'Apariciones de Jack', 'Apariciones de Rose', 'Longitud media de las frases', 'Palabra más larga', 'Palabra más usada', 'Palabras más usadas', 'Frecuencia','Palabra más corta'])  # Asignar nombre a la columna

# Crear la tabla en la base de datos
df.to_sql('Script del Titanic', engine, if_exists='replace', index=False)

print("Tabla Titanic y datos subidos con éxito.")
print("----------------------")
print("Columnas creadas:")
print("----------------------")
print('Línea')
print('Apariciones de Jack')
print('Apariciones de Rose')
print('Longitud media de las frases')
print('Palabra más larga')
print('Palabras más usadas')
print('Palabra más corta')







