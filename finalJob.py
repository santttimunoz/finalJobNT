import pandas as pd


datosFinalJob = pd.read_csv('./datosFinalJob.csv')

print(f"datos de la tabla:\n {datosFinalJob.head()}\n")
print(f"{datosFinalJob.info()}\n")
print(f"suma de los ID de empleados: {datosFinalJob['ID_Empleado'].sum()}\n")

print(f"Día mínimo: {datosFinalJob['Día'].min()}\n")

print(datosFinalJob.groupby('Departamento')['ID_Empleado'].count().reset_index())

