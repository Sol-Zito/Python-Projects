from pathlib import Path, PureWindowsPath
import os

# Opcion para mac & windows
rutan = Path("C:/Users/solzi/IdeaProjects/PythonProyect/Dias/Dia4") / "archivodia6.txt"

ruta_window = PureWindowsPath(rutan) # invierte las barras
print(ruta_window)

# verificar la extensión de un archivo
print(f"suffix {rutan.suffix}")

# stem nombre o componente final de la ruta, sin su sufijo (extension)

if not rutan.exists():
    print("No existe archivo")
else:

    # Al utilizar el Path, no hace falta abrirlo para hacer uso del mismo
    print(rutan.read_text())

    # nombre del archivo
    elemento = os.path.basename(rutan)
    print(elemento)

    # ruta del directorio
    elemento1 = os.path.dirname(rutan)
    print(elemento1)



# Rutas relativas
guiaE = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")

# Rutas absoluta
base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")

print(f"Base: {base}")
print(f"guia: {guia}")
print(f"guia2: {guia2}")

#en_europa = guia.relative_to(Path("Europa"))
#en_españa = guia.relative_to(Path("Europa", "España"))

