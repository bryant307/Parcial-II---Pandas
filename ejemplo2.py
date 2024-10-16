import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('C:/Users/torre/Desktop/parcial.csv')

# Mostrar las primeras filas del DataFrame
print(df)


#Agrupar los datos por Producto y sumar el total de ventas
venta_por_producto = df.groupby('Producto')['Total'].sum()
print(venta_por_producto)


# Filtrar las ventas donde el total sea mayor a 85
ventas_mayores_a_85 = df[df['Total'] > 85]

# Mostrar el resultado
print(ventas_mayores_a_85)



# Obtener estadísticas descriptivas
estadisticas = df.describe()

# Mostrar las estadísticas
print(estadisticas)

