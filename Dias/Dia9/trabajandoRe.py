import re

# txt = "Si necesitas ayuda llama al 8989"
# patron = "ayuda"
# busqueda = re.search(patron, txt)

# print(busqueda.start())

# clave = input("Clave: ")
# patron_clave = r'\D{1}\w{7}'

# chequear = re.search(patron_clave, clave)
# print(chequear)


texto = "No se atienden los lunes por la tarde"
# buscar_texto = re.search(r'lunes|martes', texto)
# print(buscar_texto)


tienden = re.search(r'.tienden', texto)
atienden = re.search(r'atienden', texto)
noDigito = re.search(r'^\D', texto)
# en caso de que sea numeral devulve none
#print(noDigito)



def verificar_email(email):
    patron = r".@.com"
    busqueda = re.search(patron, email)
    print(busqueda)
    if busqueda:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

def verificar_email1(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

# verificar_email1("usuario@hostcom")
# verificar_email("usuario@hostcom")

def verificar_saludo(frase):
    patron = re.search(r"^Hola", frase)
    print(patron)
    if patron:
        print("Ok")
    else:
        print("No has saludado")

# verificar_saludo("Buenas, Hola como va?")

gmal = r'@.+\.com$'
# @hshshs.com

def verificar_cp(cp):
    patron = re.search(r"\w{2}\d{4}", cp)
    if patron:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

#verificar_cp("XX5448")





get_five_numbers("XX54483")