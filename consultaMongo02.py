import pandas as pd
from pymongo import MongoClient

# conectar a base mongo
client = MongoClient('mongodb://localhost:27017/')
db = client['atp_tennis_matches']
collection = db['matches_2022_2023']
# consulta para saber el top 5 jugadores con más victorias

# utilizando dataframes, leer los documentos desde MongoDB y convertirlos a DataFrame
df = pd.DataFrame(list(collection.find()))

# se utiuliza el df para contar cuántos partidos se jugaron en cada ciudad
city_count = df['Location'].value_counts().reset_index(name='TotalMatches')

# formateamos las columnas
city_count.columns = ['City', 'TotalMatches']

# Mostrar resultados
print("\nTop 5 ciudades con más partidos jugados:")
# .head es para mostrar las primeras 5 filas
print(city_count.head(5))