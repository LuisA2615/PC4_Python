import os  

def guardar_tabla(n):  
    with open(f'tabla-{n}.txt', 'w') as f:  
        for i in range(1, 11):  
            f.write(f"{n} x {i} = {n * i}\n")  

def mostrar_tabla(n):  
    filename = f'tabla-{n}.txt'  
    if os.path.exists(filename):  
        with open(filename, 'r') as f:  
            print(f.read())  
    else:  
        print("El fichero no existe.")  

def mostrar_linea(n, m):  
    filename = f'tabla-{n}.txt'  
    if os.path.exists(filename):  
        with open(filename, 'r') as f:  
            lineas = f.readlines()  
            if 1 <= m <= len(lineas):  
                print(lineas[m - 1].strip())  
            else:  
                print("La línea solicitada no existe en el fichero.")  
    else:  
        print("El fichero no existe.")  

def main():  
    while True:  
        print("\nMenu:")  
        print("1. Guardar tabla de multiplicar")  
        print("2. Mostrar tabla de multiplicar")  
        print("3. Mostrar línea de la tabla")  
        print("4. Salir")  
        
        opcion = int(input("Elija una opción: "))  
        
        if opcion == 1:  
            n = int(input("Ingrese un número entre 1 y 10: "))  
            if 1 <= n <= 10:  
                guardar_tabla(n)  
                print(f"Tabla de multiplicar del {n} guardada en 'tabla-{n}.txt'.")  
            else:  
                print("Número fuera de rango.")  
        
        elif opcion == 2:  
            n = int(input("Ingrese un número entre 1 y 10: "))  
            if 1 <= n <= 10:  
                mostrar_tabla(n)  
            else:  
                print("Número fuera de rango.")  
        
        elif opcion == 3:  
            n = int(input("Ingrese un número entre 1 y 10: "))  
            if 1 <= n <= 10:  
                m = int(input("Ingrese la línea que desea mostrar: "))  
                mostrar_linea(n, m)  
            else:  
                print("Número fuera de rango.")  
        
        elif opcion == 4:  
            print("Saliendo del programa.")  
            break  
        
        else:  
            print("Opción no válida.")  

if __name__ == "__main__":  
    main()