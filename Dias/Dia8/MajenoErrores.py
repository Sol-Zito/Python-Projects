def suma():
    n1 = int(input("Number: "))
    n2 = int(input("Number: "))
    print(f"{n1+n2} \nGracia por sumar")

try:
    # Codigo a probar
    suma()
except ValueError:
    print("Ese no es un number")
    # Codigo a ejecutar si hay error
except TypeError:
    print("Estas intentando cancatenar distintos tipos")
else:
    # Codigo que se ejecuta si no hay error
    print("Salio todo bien")
finally:
    # Codigo a ejecutar de todos modos
    print("Eso fue todo")




def pedirNumero():

    while True:
        try:
            numero = int(input("Ingrese: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Gracias")

pedirNumero()