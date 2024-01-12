# str
nombre: str = "Juan"
# int
edad: int = 25
# print(type(edad))
num1 = "7.5"
num2 = "10"
# print(float(num1) + int(num2))

# round --> redondea nros para arriba
valor = 97.5


# print(round(valor))

# Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.
# print(round(10/3,2))
# print(round(13/2,0))


# Formatear cadenas
auto_marca = "Chevrolet"
auto_color = "rojo"
auto_matricula = 256897

# Funcion Format Desventaja --> ilegible

print("Auto robado marca: {}, color: {}, matricula: {}" .format(auto_marca, auto_color, auto_matricula))

# Cadena literal

print(f"Quiero el auto {auto_marca}, color: {auto_color}")


# Con valores numericos

x = 7
y = 9
z = 2

print(f"La suma entre {x} y {y} da {x+y}")
print(f"La division al piso entre {x} y {z} da {x//z}")
print(f"La division  entre {x} y {z} da {x/z}")
print(f"{x} modulo de {z} da {x%z}")
print(f"La raiz cuadrada de {783} es {783**0.5}")


