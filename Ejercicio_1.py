import requests  

def obtener_precio_bitcoin():  
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"  
    try:  
        respuesta = requests.get(url)  
        respuesta.raise_for_status()  # Lanza un error si la respuesta fue un error HTTP  
        datos = respuesta.json()  
        precio_bitcoin = datos['bpi']['USD']['rate_float']  # Obtiene el precio en USD  
        return precio_bitcoin  
    except requests.RequestException as e:  
        print(f"Error al consultar la API: {e}")  
        return None  

def main():  
    n = float(input("Ingrese la cantidad de bitcoins que posee: "))  
    precio_bitcoin = obtener_precio_bitcoin()  
    
    if precio_bitcoin is not None:  
        costo_total = n * precio_bitcoin  
        print(f"El costo actual de {n} Bitcoins es: ${costo_total:,.4f} USD")  

if __name__ == "__main__":  
    main()