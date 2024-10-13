import requests  
import sqlite3  
import json  

# Obtener datos del API  
response = requests.get("https://apis.net.pe/api/tipo-cambio/2023")  
datos = response.json()  

# Conectar a la base de datos SQLite  
conn = sqlite3.connect('base.db')  
c = conn.cursor()  

# Crear tabla  
c.execute('''  
    CREATE TABLE IF NOT EXISTS sunat_info (  
        fecha TEXT,  
        compra REAL,  
        venta REAL  
    )  
''')  

# Insertar datos en la tabla  
for registro in datos:  
    c.execute('''  
        INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)  
    ''', (registro['fecha'], registro['compra'], registro['venta']))  

conn.commit()  
conn.close()