import pandas as pd
from pymongo import MongoClient

# conectar a base mongo
client = MongoClient('mongodb://localhost:27017/')
db = client['atp_tennis_matches']
collection = db['matches_2022_2023']
# consulta para saber el top 5 de ciudades con más partidos jugados

# utilizando dataframes, leer los documentos desde MongoDB y convertirlos a DataFrame
df = pd.DataFrame(list(collection.find()))

# se agrupa por 'Winner' y se cuenta el total de victorias
top_winners = df.groupby('Winner').size().reset_index(name='Total Wins')

# para ordenar de mayor a menor y mostrar los 5 primeras filas
top_winners_sorted = top_winners.sort_values(by='Total Wins', ascending=False).head(5)

# Mostrar resultados
print("\nTop 5 jugadores con más victorias:")
print(top_winners_sorted)