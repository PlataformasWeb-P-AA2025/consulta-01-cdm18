import pandas as pd
from config import collection

# leer el archivo excel de 2022 y cargarlo en un dataframe
df_2022 = pd.read_excel('data/2022.xlsx')

# convertir la columna 'Date' a formato datetime, asegurando que el día esté antes que el mes
df_2022['Date'] = pd.to_datetime(df_2022['Date'], dayfirst=True, errors='coerce')

# lista de columnas numéricas que necesitamos convertir para poder trabajar con ellas
num_cols = [
    'ATP', 'WRank', 'LRank', 'WPts', 'LPts', 'W1', 'L1', 'W2', 'L2', 'W3', 'L3',
    'W4', 'L4', 'W5', 'L5', 'Wsets', 'Lsets',
    'B365W', 'B365L', 'PSW', 'PSL', 'MaxW', 'MaxL', 'AvgW', 'AvgL'
]

# recorremos las columnas que necesitamos convertir y las pasamos a tipo numérico
for col in num_cols:
    if col in df_2022.columns:
        df_2022[col] = pd.to_numeric(df_2022[col], errors='coerce')

# reemplazamos los valores NaN (vacíos o incorrectos) por None, para que mongo los entienda bien
df_2022 = df_2022.where(pd.notnull(df_2022), None)

# convertimos todo el dataframe a un formato de diccionario que mongo pueda insertar fácilmente
records = df_2022.to_dict(orient='records')

# insertamos los datos procesados en la base de datos
result = collection.insert_many(records)

# mostramos cuántos documentos fueron insertados correctamente
print(f'Datos 2022 insertados: {len(result.inserted_ids)} documentos')
