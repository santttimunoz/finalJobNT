from pymongo import MongoClient

# Conexión a MongoDB Atlas
client = MongoClient('mongodb+srv://santiagomunoz:admin123@cluster0.qelxcgx.mongodb.net/?retryWrites=true&w=majority')

if client:
    print("Conexión exitosa a MongoDB")
else:
    print("Error de conexión a MongoDB")
    
# base de datos
db = client['FinalJob']

# colecciones
empleados = db['empleados']
proyectos = db['proyectos']
asignaciones = db['asignaciones']

#insertar 
empleadoUno = {"nombre":"santiago",
               "edad":23,
               "cargo":"desarrollador"}
empleados.insert_one(empleadoUno)
