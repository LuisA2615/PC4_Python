import random  
from pyfiglet import Figlet  

# Instanciar el objeto Figlet  
figlet = Figlet()  

# Obtener la lista de fuentes disponibles  
fuentes_disponibles = figlet.getFonts()  

# Solicitar al usuario la fuente  
fuente_usuario = input("Ingrese el nombre de una fuente (o presione Enter para elegir una aleatoria): ")  

# Seleccionar fuente  
if fuente_usuario not in fuentes_disponibles or fuente_usuario == "":  
    fuente_seleccionada = random.choice(fuentes_disponibles)  
    print(f"Se ha seleccionado la fuente aleatoria: {fuente_seleccionada}")  
else:  
    fuente_seleccionada = fuente_usuario  

# Configurar la fuente  
figlet.setFont(font=fuente_seleccionada)  

# Solicitar el texto al usuario  
texto_imprimir = input("Ingrese el texto que desea imprimir: ")  

# Imprimir el texto usando la fuente seleccionada  
print(figlet.renderText(texto_imprimir))