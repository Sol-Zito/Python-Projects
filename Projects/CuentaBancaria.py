
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, nro_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.nro_cuenta = nro_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta: ${self.balance}"

    #Depositar, que le va a permitir decidir cuánto dinero quiere agregar a su cuenta.

    def depositar(self, dinero):
        self.balance += dinero
        print("Se realizo deposito de dinero")

    # tercer método llamado Retirar, que le permita decidir cuánto dinero quiere sacar de su cuenta.

    def retirar(self, dinero):
        if self.balance >= dinero:
            self.balance -= dinero
            print("Se retiraro dinero")
        else:
            print("No cuenta con el saldo necesario")


def pedir_datos():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    nro_cuenta = input("Ingrese nro_cuenta: ")
    return nombre, apellido, nro_cuenta

def crear_cliente():
    deseaCrearUsuario = input("Desea crear cliente: ")
    if deseaCrearUsuario == 'si' or deseaCrearUsuario == 'Si':
        nombre, apellido, nro_cuenta = pedir_datos()
        nuevoCliente = Cliente(nombre, apellido, nro_cuenta)
        return nuevoCliente
    else:
        print("Adios")

def inicio():
    cliente = crear_cliente()
    getOut = True

    while getOut:
        print(cliente)
        print("Operaciones:\n"
              "[1] Depositar dinero\n"
              "[2] Retirar dinero\n"
              "[3] Finalizar operacion")
        operacion = input("Ingrese operacion a realizar:")
        match operacion:
            case '1':
                dinero = int(input("Ingrese monto: "))
                cliente.depositar(dinero)
            case '2':
                dinero = int(input("Ingrese monto: "))
                cliente.retirar(dinero)
            case '3':
                getOut = False
            case _:
                print("Operacion invalida")
    else:
        print("Gracias por operar en Banco Python")


inicio()