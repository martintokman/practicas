# 
import numpy as np

#armo un array con números del 0 al 49
array = np.array(range(int(50)))

#armo un array con valores unicode
array = np.array(['Juan', 48, '1e-7'], dtype='<U32')

#armo un array de tipo int64
array = np.array(range(50), dtype='int64')

#armo un array de tipo float64
array = np.array(range(50), dtype='float64')

#convierto el array a una lista
array2 = array.tolist()

#convierto la lista a un array y lo convierto a int64
array3 = np.array(array2, dtype = 'int64')

#muestro la suma del array
#print(sum(array3))

#muestro el valor máximo y mínimo del array
#print(max(array3), min(array3))

#muestro el segundo elemento del array
#print(array[1])

#muestro los ultimos 5 elementos del array
#print(array[-5:])

#armo una matrizde 3x3
matriz = np.array([
                    [1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12]
])

#muestro las dimensiones de la matriz
#print(matriz.ndim)

#muestro la cantidad de valores de la matriz
#print(matriz.size)

#muestro la composicion de filas y columnas de la matriz
#print(matriz.shape)

#muestro el tipo de datos dentro de la matriz
#print(matriz.dtype)


#redimensiono el array a la cantidad de filas y columnas 
array = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
#array.shape = (6,2) #6 filas, 2 columnas

#guardo el array en un archivo binario .npy
np.save('matriz.npy', array)

#creo un array a partir de un archivo .npy
array = np.load('matriz.npy')

#guardo un array en un archivo .csv
np.savetxt('matriz.csv', array, fmt='%.s')

nombre = 'martin tokman'
edad = 4
#print('%s tiene %3d años' %(nombre,edad))

print(nombre.count('t'))

lista = [1,2,3]
del lista[1]
print(lista)








