# # crea nuevo directory
import os
from pathlib import Path

#
# #La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
# #el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.

directorio_path = Path("C:\\Users\\solzi\\IdeaProjects\\PythonProyect\\Projects\\Recetas\\")

carpetas = os.chdir(directorio_path)
carpetas = os.listdir(carpetas)


def validando_eleccion(lista):
    eleccion = ''
    while eleccion not in lista:
        eleccion = input(f"Estas son nuestras opciones, \nElija una: {lista}: ")
    else:
        return eleccion


def recorrer_carpetas():
    recetas_total = []
    for i in carpetas:
        cant_recetas = Path(directorio_path, i)
        cant_recetas = os.listdir(cant_recetas)
        recetas_total.append(cant_recetas)
    return recetas_total


# # Recorre las recetas segun la carpeta que eligio el usuario
def recorrer_lista(eleccion):
    cant_recetas = Path(directorio_path, eleccion)
    cant_recetas = os.listdir(cant_recetas)
    return cant_recetas


# # Agarra la lista y le saca la extension
def tranformacion_lista(lista):
    nlista = recorrer_lista(lista)
    listan = []

    for i in nlista:
        sintxt = i.replace('.txt', '')
        listan.append(sintxt)
    return listan


# # Obtencion de receta

def obtencion_receta(carpeta, menu):
    menu = f'{menu}.txt'
    receta = Path(directorio_path, carpeta, menu)
    print(receta.read_text())


# obtencion_receta(recetaElegida)

# En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
# escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va a crear ese archivo en el lugar correcto.

def nueva_receta():
    print(f"La receta puede ser de: {carpetas}")
    tipo_recetaU = validando_eleccion(carpetas)
    print("tipo_recetaU", tipo_recetaU)
    nombre_menu = input("Ingrese el nombre de la nueva receta: ")
    detalles_menu = input("Ingrese los detalles de la nueva receta: ")
    nombre_menu = f"{nombre_menu}.txt"

    ruta_carpeta = os.chdir(Path(directorio_path, tipo_recetaU))
    crear_receta = open(nombre_menu, 'w')
    crear_receta.write(detalles_menu)
    crear_receta.close()
    print(f"Se creo nueva receta: {nombre_menu.lstrip('.txt')}")


# La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
# una carpeta nueva con ese nombre.

def crear_categoria():
    nueva_cat = ''
    isValida = False
    while not isValida:
        nueva_cat = input("Ingrese nueva categoria: ")
        if nueva_cat in carpetas:
            print("Ya existe esa categoria")
        else:
            isValida = True
    else:
        # ruta_carpeta = os.chdir(Path(directorio_path))
        Path.mkdir(nueva_cat)
        # carpeta = os.makedirs(nueva_cat)
        print("Se creo nueva categoria")


# La opción 4, hará lo mismo que la opción uno, pero en vez de leer la receta, la va
# a eliminar

def borrar_receta(carpeta, menu):
    menu = f'{menu}.txt'
    receta = Path(Path(directorio_path, carpeta, menu))
    Path(receta).unlink()
    print("Se ha borrado receta")

# La opción 5, le va a preguntar qué categoría quiere eliminar

def borrar_categoria(categoria):
    categoria_rm = Path(Path(directorio_path, categoria))
    Path(categoria_rm).unlink()
    print("Se ha borrado categoria")

# Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.

def inicio():
    opcionesValidas = ['1', '2', '3', '4', '5', '6']

    print("Menu:\n"
          "[1] - Leer receta\n[2] - Crear receta nueva\n[3] - Crear categoria nueva\n"
          "[4] - Eliminar receta\n[5] - Eliminar categoria\n[6] - Salir del programa")

    opcion = ''
    while opcion not in opcionesValidas:
        print("Ingrese una opcion valida")
        opcion = input("Ingrese su el nro de su opcion: ")

    else:
        return opcion


def volverInicio():
    print("Volver:a inicio\n")


def cocinaConmigo():
    nombreUser = input("Dime tu nombre: ")
    print(f"Hola {nombreUser},\nSea bienvenid@ de ver nuestras recetas\nRuta de acceso: {directorio_path}")

    opcion = inicio()

    match opcion:
        case "1":
            # le va a informar las recetas dentro de esa carpeta,
            print(f"Recetas de: {carpetas}")
            tipoDeReceta = validando_eleccion(carpetas)
            listaDeRecetas = tranformacion_lista(tipoDeReceta)
            recetaElegida = validando_eleccion(listaDeRecetas)
            obtencion_receta(tipoDeReceta, recetaElegida)
            volverInicio()
        case "2":
            nueva_receta()
            volverInicio()
        case "3":
            crear_categoria()
            volverInicio()
        case "4":
            tipoDeReceta = validando_eleccion(carpetas)
            listaDeRecetas = tranformacion_lista(tipoDeReceta)
            recetaElegida = validando_eleccion(listaDeRecetas)
            borrar_receta(tipoDeReceta, recetaElegida)
            volverInicio()
        case "5":
            Categoria = validando_eleccion(carpetas)
            borrar_categoria(Categoria)
            volverInicio()
        case "6":
            print("Finalizar programa")


cocinaConmigo()
