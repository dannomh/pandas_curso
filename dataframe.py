import pandas as pd

data = {
    "nombre": ["Ana", "Luis", "Carla", "Pedro"],
    "edad": [23, 34, 29, 40],
    "ciudad": ["Quito", "Guayaquil", "Cuenca", "Quito"],
    "puntos": [88, 92, 95, 70]
}

df = pd.DataFrame(data)
#print(df["edad"])# muestra SOLO la columna edad

#print(df[["edad","nombre"]])

#print(df["nombre"][df["ciudad"]=="Quito"])

#print(df[(df["ciudad"]=="Quito") & (df["edad"] > 25)])

#print(df[(df["puntos"]>90) & (df["edad"]>30)])