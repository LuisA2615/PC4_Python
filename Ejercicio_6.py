import os  

def contar_lineas_codigo(ruta_archivo):  
    # Verificar si la ruta es válida y si el archivo tiene extensión .py  
    if not os.path.isfile(ruta_archivo) or not ruta_archivo.endswith('.py'):  
        print("La ruta es inválida o el archivo no es un archivo .py.")  
        return  
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:  
        lineas_de_codigo = 0  
        for linea in archivo:  
            # Ignorar líneas en blanco y comentarios  
            if linea.strip() and not linea.strip().startswith('#'):  
                lineas_de_codigo += 1  

    print(f"Número de líneas de código (excluyendo comentarios y líneas en blanco): {lineas_de_codigo}")  

# Solicitar al usuario la ruta del archivo  
ruta_usuario = input("Ingrese la ruta del archivo .py: ")  
contar_lineas_codigo(ruta_usuario)