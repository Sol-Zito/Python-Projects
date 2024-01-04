# Proyecto 3

texto = input("Ingrese texto: ")
letras = []

letras.append(input("Ingrese letra 1: "))
letras.append(input("Ingrese letra 2: "))
letras.append(input("Ingrese letra 3: "))

#Contar cuantas veces aparece c/letra

print("CANTIDAD DE LETRAS")
textoUpper = texto.upper()
letra1 = textoUpper.count(letras[0].upper())
letra2 = textoUpper.count(letras[1].upper())
letra3 = textoUpper.count(letras[2].upper())

print(f"Se encontro la letra: {letras[0]}, {letra1} veces, la letra: {letras[1]}, {letra2} veces, y por ultimo a la "
      f"letra: {letras[2]}, {letra3}  veces")

# Cantidad de palabras

oracion = texto.split()
print(f"Cantidad de palabras en el texto: {len(oracion)}")

# Letras de inicio y de Fin

print(f"El caracter inicial es: {texto[0]}, y el caracter final es: {texto[-1]}")

# Existe python en texto

existePython = "Python" in texto
print(f"Existe python en texto : {existePython}")