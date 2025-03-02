
# Definir una matriz 3x3
matriz = [
    [9, 2, 5],
    [8, 6, 1],
    [4, 7, 3]
]
#función para matriz ascendente
def bubble_sort(fila):
    n = len(fila)
    for i in range(n -1):
        for j in range(n -i -1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

#función mostrar matriz orignal
print("Matriz original:")
for fila in matriz:
    print(fila)

# poner la fila que se desea cambiar
while True:
    fila_ordenar = int(input("Ingrese el número de la fila que se desea ordenar de manera ascendente:"))
    if 0 <= fila_ordenar <= 2:
        break
    print("Digite bien el número por favor.")

# fila seleccionada
bubble_sort(matriz[fila_ordenar])

#función mostrar matriz ascendente
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
