import os
import shutil
#import send2trash

#print(os.getcwd())

# archivo = open("curso.txt", 'w')
# archivo.write("Texto de prueba")
# archivo.close()
#
# print(os.listdir())

#shutil.move("curso.txt", "C:\\Users\\solzi\\IdeaProjects\\PythonProyect\\Dias\\Dia8")

#send2trash.send2trash('curso.txt')

ruta = "C:\\Users\\solzi\\IdeaProjects\\PythonProyect\\Dias"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta:{carpeta}")
    print("Las subcarpetas son:")
    for subc in subcarpeta:
        print(f"\t{subc}")
    print("Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")
