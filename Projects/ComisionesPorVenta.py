# Proyecto 2

def comisionSobreVentas(ventas: int):
    return round(ventas * 0.13, 2)

nombreUsuario = input("Nombre de Usuario: ")
ventasTotales = int(input("Ventas Totales del mes: "))

print(f"Hola {nombreUsuario}, la comision de este mes es de: ${comisionSobreVentas(ventasTotales)}")