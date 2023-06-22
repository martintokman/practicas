# Básicos dataframes

import pandas as pd


diccionario = {
                'Nombre' : ['Martin', 'Juan', 'Pedro', 'Jose', 'Julian', 'Mario', 'Miriam', 'Ernesto', 'Juana', 'Manolo'],
                'Apellido' : ['Tokman', 'Perez', 'Alfonso', 'Marán', 'Tatin', 'Fabuso', 'Camili', 'Gonzalez', 'Gimenez', 'Perez'],
                'Edad' : [47, 38, 71, 14, 24, 61, 81, 8, 27, 48],
                'Profesion' : ['Programador', 'Carpintero', 'Finanzas', 'Estudiante', 'Artista', 'Instructor de sky', 'Levantador de pesas', 'Alfarero', 'Programador', 'Carpintero']
}


df = pd.DataFrame(diccionario)

#Desempaquetado de la forma en dos variabels
rows, columns = df.shape

#Muestro todo el dataset
#print(df)

#Muestro solo las primeras filas
#print(df.head())

#Muestro las primeras 3 filas
#print(df.head(3))

#Muestro las últimas 5 filas
#print(df.tail())

#Muestro las últimas 2 filas
#print(df.tail(2))

#Muestro un rango de filas
#print(df[2:5])
#print(df[:-2])

#Muestro las columnas del df
#print(df.columns)

#Muestro una columna en particular
#print(df.Apellido)
#print(df['Apellido'])

#Muestro el tipo de datos
#print(type(df.Apellido))
#print(type(df['Apellido']))

#Muestro SOLo determinadas columnas
#print(df[['Nombre', 'Apellido', 'Edad']])

#Muestro el valor máximo en una columna numérica
#print(df['Edad'].max())

#Muestro el valor mínimo en una columna numérica
#print(df['Edad'].min())

#Muestro el valor promedio en una columna numérica
#print(df['Edad'].mean())

#Muestro la desviación estandard en una columna numérica
#print(df['Edad'].std())

#Muestro estadísticas de las comunas numéricas
#print(df.describe())

#Muestro todas las personas mayores de edad
#print(df[df.Edad > 18])

#Muestro la fila que tenga la máxima edad
#print(df[df.Edad == df['Edad'].max()])

#Muestro solo el nombre de la persona que tenga más edad
#print(df['Nombre'][df.Edad == df['Edad'].max()])

#Muestro el nombre y apellido de la persona que tenga menos edad
print(df[['Nombre','Apellido']][df.Edad == df['Edad'].max()])






