def mi_funcion(funcion, texto):
    print('Hola')
    funcion = funcion(texto)
    print('Adios')


def decorar_saludos(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')

    return otra_funcion


def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludos(mayusculas)
minusculas_decorada = decorar_saludos(minusculas)

mayuscula_decorada("python")
