import os

ruta = os.getcwd()
#  current working directory

#  change directory
#ruta = os.chdir("C:\\Users\\solzi\\IdeaProjects\\PythonProyect\\Dias\\Dia4")

#  crea nuevo directory
#crearDir = os.makedirs("C:\\Users\\solzi\\IdeaProjects\\PythonProyect\\Dias\\Dia7")


# nombre del archivo con extension
ruta_archivo = "C:\\Users\\solzi\\IdeaProjects\\PythonProyect\\Dias\\Dia4\\archivodia6.txt"


elemento = os.path.basename(ruta_archivo)
print(elemento)

# ruta del directorio
elemento1 = os.path.dirname(ruta_archivo)
print(elemento1)

# borra carpeta
# os.rmdir("C:\\Users\\solzi\\IdeaProjects\\PythonProyect\\Dias\\Dia7")


