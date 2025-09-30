# 12. Concatenar elementos de sub-listas em uma única lista

listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
lista_concatenada = [elemento for sublista in listas for elemento in sublista]
print(lista_concatenada)