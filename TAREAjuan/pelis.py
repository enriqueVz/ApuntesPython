import requests
from bs4 import BeautifulSoup
import csv

# URL de la página de IMSDb
url = 'https://imsdb.com/'

# Realizar la solicitud HTTP y obtener la respuesta
response = requests.get(url)

# Parsear el contenido HTML de la respuesta
soup = BeautifulSoup(response.text, 'html.parser')

# Seleccionar los elementos que contienen las películas más recientes
newest_releases = soup.find_all('a', class_='title')

# Crear el archivo CSV y escribir los encabezados
with open('peliculas.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Título', 'Año', 'Valoración', 'Duración'])

    # Iterar sobre los elementos y extraer los datos
    for release in newest_releases:
        # Extraer el título de la película
        title_text = release.text.strip()
        
        # Extraer el año de creación
        year = release.find_next('td', class_='info').text.strip().split(' (')[1].split(')')[0]
        
        # Extraer la valoración
        rating = release.find_next('td', class_='info').text.strip().split('Rating: ')[1].split(' ')[0]
        
        # Extraer la duración
        runtime = release.find_next('td', class_='info').text.strip().split('Runtime: ')[1].split(' ')[0]
        
        # Escribir los datos en el archivo CSV
        writer.writerow([title_text, year, rating, runtime])
        print("listo jefe")