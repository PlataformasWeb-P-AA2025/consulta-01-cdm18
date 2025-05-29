from pymongo import MongoClient

# Configuración de conexión MongoDB
MONGO_URI = 'mongodb://localhost:27017'

# Crear cliente
client = MongoClient(MONGO_URI)

# Base de datos
db = client['atp_tennis_matches']

# Colección
collection = db['matches_2022_2023']
