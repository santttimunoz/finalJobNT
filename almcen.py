import pandas as pd
import matplotlib.pyplot as plt

coleccionUno = pd.read_csv('./datos/data2.csv')
coleccionDos = pd.read_csv('./datos/data2.csv')
coleccionTres = pd.read_csv('./datos/data3.csv')


print(f'coleccionUno: \n {coleccionUno}\n')
print(f'coleccionUno: \n {coleccionDos}\n')
print(f'coleccionUno: \n {coleccionTres}\n')

# 1. Imprime las primeras filas de cada colección
print(f'Primeras filas de coleccionUno:\n{coleccionUno.head()}\n')

# 2. Suma de una columna específica en coleccionDos
suma = coleccionDos['Suma de Precio'].sum()
print(f'Suma de la columna "Suma de Precio" en coleccionDos: {suma}\n')

# 3. Promedio de una columna específica en coleccionTres
promedio = coleccionTres['Suma de Cantidad'].mean()
print(f'Promedio de la columna "Suma de Cantidad" en coleccionTres: {promedio}\n')

# 4. Valor máximo de una columna específica en coleccionUno
maximo = coleccionUno['Suma de Precio'].max()
print(f'Valor máximo de la columna "Suma de Precio" en coleccionUno: {maximo}\n')

# 5. Valor mínimo de columna suma de precio en coleccionUno
minimo = coleccionUno['Suma de Precio'].min()
print(f'Valor máximo de la columna "Suma de Precio" en coleccionUno: {minimo}\n')

# 6. Contar valores únicos en coleccionDos
conteo_valores = coleccionDos['Nombre'].value_counts()
print(f'Conteo de valores únicos en "Nombre" de coleccionDos:\n{conteo_valores}\n')

# 7. Eliminar una columna en coleccionDos
coleccionDos = coleccionDos.drop(columns=['Descripcion'])
print(f'coleccionDos después de eliminar "Descripcion":\n{coleccionDos}\n')

#graficos

coleccionDos['Suma de Precio'].plot(kind='bar')
plt.show()

coleccionUno['Suma de Precio'].plot(kind='pie', autopct='%1.1f%%')
plt.title('Gráfico de Pastel')
plt.show()

coleccionUno['Suma de Precio'].plot(kind='line')
plt.title('Gráfico de Línea')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.show()

coleccionTres.plot(kind='scatter', x='Suma de Cantidad', y='Recuento de ExistenciaID')
plt.title('Diagrama de Dispersión')
plt.xlabel('Suma de Cantidad')
plt.ylabel('Recuento de ExistenciaID')
plt.show()








