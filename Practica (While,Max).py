#While y Max
import numpy as np

n_0 = int(input("Ingresa la longitud de la lista: "))
n = np.abs(n_0)
lista = []
for i in range(0,n):
    x_i = float(input(f'Ingresa el elemento en la posición {i}:'))
    lista.append(x_i)
print(lista)

max = np.max(lista)

i=0
while lista[i] < max:
    print(lista[i])
    i = i+1
