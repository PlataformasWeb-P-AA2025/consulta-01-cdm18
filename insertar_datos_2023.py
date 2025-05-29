import pandas as pd
from config import collection

# Leer Excel 2023
df_2023 = pd.read_excel('data/2023.xlsx')

# Procesar columna Date a datetime con dayfirst=True
df_2023['Date'] = pd.to_datetime(df_2023['Date'], dayfirst=True, errors='coerce')

# Convertir columnas numéricas (lista adaptada)
num_cols = [
    'ATP', 'WRank', 'LRank', 'WPts', 'LPts', 'W1', 'L1', 'W2', 'L2', 'W3', 'L3',
    'W4', 'L4', 'W5', 'L5', 'Wsets', 'Lsets',
    'B365W', 'B365L', 'PSW', 'PSL', 'MaxW', 'MaxL', 'AvgW', 'AvgL'
]

for col in num_cols:
    if col in df_2023.columns:
        df_2023[col] = pd.to_numeric(df_2023[col], errors='coerce')

# Reemplazar NaN con None
df_2023 = df_2023.where(pd.notnull(df_2023), None)

# Convertir a diccionario y guardar en MongoDB
records = df_2023.to_dict(orient='records')

result = collection.insert_many(records)
print(f'Datos 2023 insertados: {len(result.inserted_ids)} documentos')
