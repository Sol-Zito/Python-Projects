# Metodos de archivo (abrir, cerrar, modificar, crear, leer...)

# mi_archivo = open('Prueba.txt', 'r')
# modo de solo lectura, viene por defecto

# mi_archivo = open('Prueba.txt', 'w')
# modo de solo escritura, en caso de que no exista archivo, lo crea. En caso de existir reemplaza lo q tenia

# mi_archivo = open('Prueba.txt', 'a')
# modo de solo escritura, en caso de que no exista archivo, lo crea. En caso de existir, agrega al final del texto

# print(mi_archivo.read())  # metodo para leer archivo
# print(mi_archivo.readline())


mi_archivo = open('Prueba.txt')
todas = mi_archivo.readlines()
mi_archivo.close()
# es importante cerrar el archivo

#archivo = open('Prueba1.txt', 'w')
archivo = open('Prueba1.txt', 'r')
#archivo = open('Prueba1.txt', 'a')
#archivo.write('Soy un nuevo texto. \nEsta es la prueba2')

#archivo.writelines(['Hola Mundo', 'aca', 'estoy'])
# no sirve, es preferible en caso de querer escribir lista de palabra, utilizar un loop

print(archivo.read())
archivo.close()

# Ejercicio
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivom = open('registro.txt', 'a')
for i in registro_ultima_sesion:
    archivom.writelines([i, '\t'])
archivom.close()

archivo = open('registro.txt')
print(archivo.read())
archivo.close()