import requests
import zipfile
import os

# URL de la imagen
url = " https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
# Nombre de la imagen y del archivo ZIP
image_name ="Kanon.jpg"
zip_name = "imagenes.zip"

# Descargar la imagen
response = requests.get(url)

if response.status_code == 200:
    with open(image_name, 'wb') as file:
        file.write(response.content)
    
    print(f"Imagen descargada como {image_name}")

else:
    print("Error al descargar la imagen")

# Crear un archivo ZIP y añadir la imagen
with zipfile.ZipFile(zip_name, 'w') as zipf:
    zipf.write(image_name)
print(f"Imagen comprimida en {zip_name}")

# Descomprimir el archivo ZIP
with zipfile.ZipFile(zip_name,'r') as zipf:
    zipf.extractall("imagenes_descomprimidas")
    print(f"Imagenes descomprimidas en la carpeta 'imagenes_descomprimidas'")