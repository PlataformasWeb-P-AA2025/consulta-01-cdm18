import pandas as pd
from config import collection

# Leer Excel 2022
df_2022 = pd.read_excel('data/2022.xlsx')

# Procesar columna Date a datetime con dayfirst=True
df_2022['Date'] = pd.to_datetime(df_2022['Date'], dayfirst=True, errors='coerce')

# Convertir columnas numéricas (lista adaptada)
num_cols = [
    'ATP', 'WRank', 'LRank', 'WPts', 'LPts', 'W1', 'L1', 'W2', 'L2', 'W3', 'L3',
    'W4', 'L4', 'W5', 'L5', 'Wsets', 'Lsets',
    'B365W', 'B365L', 'PSW', 'PSL', 'MaxW', 'MaxL', 'AvgW', 'AvgL'
]

for col in num_cols:
    if col in df_2022.columns:
        df_2022[col] = pd.to_numeric(df_2022[col], errors='coerce')

# Reemplazar NaN con None
df_2022 = df_2022.where(pd.notnull(df_2022), None)

# Convertir a diccionario y guardar en MongoDB
records = df_2022.to_dict(orient='records')

result = collection.insert_many(records)
print(f'Datos 2022 insertados: {len(result.inserted_ids)} documentos')
