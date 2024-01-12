import shutil
import zipfile
import os

# CREO ARCHIVO .ZIP
# mi_arch = zipfile.ZipFile("archivo_comprimido.zip", 'w')
# os.rmdir("archivo_comprimido.zip") # carpeta
# os.remove("archivo_comprimido.zip") # file

# CREO LOS FILES PARA AGREGAR AL ARCHIVO
# archivo = open("mi_texto_a.txt", 'w')
# archivo.write(" archivo de texto prueba 1")
# archivo.close()

# archivo = open("mi_texto_b.txt", 'w')
# archivo.write(" archivo de texto prueba 2")
# archivo.close()

# AGREGO FILES AL ARCHIVO
# mi_arch = zipfile.ZipFile("archivo_comprimido.zip", 'w')

#deben exisitir los archivos para agregarlos a la carpeta zip
# mi_arch.write("mi_texto_a.txt")
# mi_arch.write("mi_texto_b.txt")

# SACAR DOC DEL ARCHIVO.ZIP
# zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", 'r')
# zip_abierto.extractall()

# SHUTIL

# COMPRIMO CARPETA
# carpeta_original = "C:\\Users\\solzi\\IdeaProjects\\PythonProyect\\Projects\\Recetas"
# archi_destino = "recetas_comprimidas"
# shutil.make_archive(archi_destino, "zip", carpeta_original)

# DESCOMPRIMO CARPETA
shutil.unpack_archive("archivo_comprimido.zip", "Recetas descomprimidas", 'zip')
