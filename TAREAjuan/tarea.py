#Una empresa de comercio electrónico necesita optimizar su pipeline de datos para mejorar la eficiencia y reducir los tiempos de procesamiento. El pipeline actual se encarga de:
#Extracción de datos: Recopilar datos de ventas de múltiples fuentes (sistemas de punto de venta, plataformas de e-commerce, etc.).
#Transformación de datos: Unificar formatos y eliminar inconsistencias en los datos.
#Carga de datos: Cargar los datos transformados en un data warehouse.


# pip install azure-storage-file-share
from typing import Counter
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from sqlalchemy import create_engine
import os
import csv




URL = 'https://www.dailyscript.com/scripts/Titanic.txt'
response = requests.get(URL)
content = response.text
ruta= r"C:\Users\evazquez\Desktop\materiales"
rutaycsv= ruta + '\script_del_titanic_peli.csv'

sopita = BeautifulSoup(content, 'html.parser')
print(sopita.prettify())

lines = []
for line in sopita.get_text().split('\n'):
    lines.append(line.strip())

dfPeli = pd.DataFrame({"Línea": lines})

jack_count = sum(line.count("Jack") for line in lines)
rose_count = sum(line.count("Rose") for line in lines)



word_counts = Counter(' '.join(lines).split())
frase_lengths = [len(line.split()) for line in lines]
frase_mean_length = sum(frase_lengths) / len(frase_lengths)
pal_corta = min(word_counts, key=lambda x: len(x))
pal_larga = max(word_counts, key=lambda x: len(x))
top10largo = pd.DataFrame({'Palabras más usadas': [word for word, count in word_counts.most_common(10)], 'Frecuencia': [count for word, count in word_counts.most_common(10)]})


dfPeli.loc[0, 'Apariciones de Jack'] = jack_count
dfPeli.loc[0, 'Apariciones de Rose'] = rose_count
dfPeli.loc[0, 'Longitud media de las frases'] = frase_mean_length
dfPeli.loc[0, 'Palabra más larga'] = pal_larga
dfPeli.loc[0, 'Palabra más usada'] = word_counts.most_common(1)[0][0]
dfPeli = pd.concat([dfPeli, top10largo], axis=1)
dfPeli.loc[0, 'Palabra más corta'] = pal_corta

dfPeli.to_csv(rutaycsv, index=False)

print("Archivo CSV creado correctamente!")


