import pandas as pd
from config import collection

# leer el archivo excel de 2023 y cargarlo en un dataframe
df_2023 = pd.read_excel('data/2023.xlsx')

# convertir la columna 'Date' a formato datetime, asegurando que el día esté antes que el mes
df_2023['Date'] = pd.to_datetime(df_2023['Date'], dayfirst=True, errors='coerce')

# lista de columnas numéricas que necesitamos convertir para poder trabajar con ellas
num_cols = [
    'ATP', 'WRank', 'LRank', 'WPts', 'LPts', 'W1', 'L1', 'W2', 'L2', 'W3', 'L3',
    'W4', 'L4', 'W5', 'L5', 'Wsets', 'Lsets',
    'B365W', 'B365L', 'PSW', 'PSL', 'MaxW', 'MaxL', 'AvgW', 'AvgL'
]

# recorremos las columnas que necesitamos convertir y las pasamos a tipo numérico
for col in num_cols:
    if col in df_2023.columns:
        df_2023[col] = pd.to_numeric(df_2023[col], errors='coerce')

# reemplazamos los valores NaN (vacíos o incorrectos) por None, para que mongo los entienda bien
df_2023 = df_2023.where(pd.notnull(df_2023), None)

# convertimos todo el dataframe a un formato de diccionario que mongo pueda insertar fácilmente
records = df_2023.to_dict(orient='records')

# insertamos los datos procesados en la base de datos
result = collection.insert_many(records)

# mostramos cuántos documentos fueron insertados correctamente
print(f'Datos 2023 insertados: {len(result.inserted_ids)} documentos')
