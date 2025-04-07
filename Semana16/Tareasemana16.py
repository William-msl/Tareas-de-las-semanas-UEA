#nombre del archivo
file_name = "my_notes.txt"
#abrimos el archivo en modo lectura
archivo = open(file_name, "w")

#leer algunas lineas
archivo.write("linea 1: 1.-hoy tengo que estudiar para mi examen.\n")
archivo.write("linea 2: 2.-tengo muchas tareas que hacer :( \n")
archivo.write("linea 3: 3.-en la tarde tengo que salir tambien.\n")
archivo.write("linea 4: Esta linea es nueva \n")
archivo.write("linea 5: La linea 1 a la 3 son las notas antiguas.\n")
archivo.write("linea 6: las lineas 4 a la 6 son las nuevas usando el metodo write :D\n")
#cerrar archivo
archivo.close()

#metodo de apertura r
archivo = open(file_name, "r")

#metodo read(): lee el contenido del archivo
contenido = archivo.read()
print("Contenido leido por read()")
print(contenido)
