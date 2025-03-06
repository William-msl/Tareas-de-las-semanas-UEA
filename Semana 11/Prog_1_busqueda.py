#hola
#matiz 3 x3

matriz = [
    [3,2,1],
    [8,7,6],
    [5,4,9]

]
def buscar_valor(matriz,valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==valor:
                return i,j #retonar
    return None

#valor a buscar
numero_buscar= 8

#funcio def
resultado = buscar_valor(matriz,numero_buscar)

if resultado:
    print(f"El número a encontrar es {numero_buscar} y esta en la posición {resultado[0]} {resultado[1]} ")

else:
    print("el número no esta en la matriz, digite otro número")



