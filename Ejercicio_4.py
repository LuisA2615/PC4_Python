import pandas as pd  

# Leer el fichero CSV  
df = pd.read_csv('temperaturas.txt', header=None, names=['fecha', 'temperatura'])  

# Calcular estadísticas  
temperatura_promedio = df['temperatura'].mean()  
temperatura_maxima = df['temperatura'].max()  
temperatura_minima = df['temperatura'].min()  

# Crear un nuevo dataframe con los resultados  
resultado = pd.DataFrame({  
    'Estadística': ['Promedio', 'Máxima', 'Mínima'],  
    'Valor': [temperatura_promedio, temperatura_maxima, temperatura_minima]  
})  

# Escribir los resultados en un nuevo fichero  
resultado.to_csv('resumen_temperaturas.txt', index=False)