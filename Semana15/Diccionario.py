
#Imprimir el Diccionario Final:

#Imprime el diccionario resultante después de realizar todas las operaciones.}
print(" ")
print("******DICCIONARIO*******")
print(" ")

#Crea un diccionario
info_personal = {
    "nombre": "Josue",
    "edad": 28,
    "ciudad": "=== Quito ===",
    "profesión": "Diseñador Gráfico"
}

#Acceder_modificar
print("La información original es:", info_personal)
print(" ")

# Insertar
info_personal["ciudad"]= "=== Cuenca ==="
print("***Cambio de ciudad:", info_personal)
print(" ")

#Profesión_puesto
info_personal["profesión"]= "=== Direcctor en Marketing ==="
print("***El puesto de trabajo de su profesión es:", info_personal)
print(" ")

#Telefono
if "teléfono" not in info_personal:
    info_personal["teléfono"] = "=== 0987654321 ==="
    print("***Número de teléfono agregado:", info_personal)
    print(" ")

#Eliminar_edad
del info_personal["edad"]
print("***Edad eliminada:", info_personal)
print(" ")

#Diccionario_final
print("=== DICCIONARIO FINAL ===")
print(info_personal)
