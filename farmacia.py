#Agregar Producto
inventario= {}


def agregarProducto(inventario):
    codigo=input("Codigo: ")
    if codigo in inventario:
        print("El producto ya existe")
    else:
        nombre=input("Ingrese el nombre del producto: ")
        precio=obtenerPrecio()
        cantidad=obtenerCantidad()
        inventario[codigo]={
            "nombre":nombre,
            "precio":precio,
            "cantidad":cantidad,
            }

def obtenerPrecio():
        while True:
            precios=float(input("Ingrese el precio: "))
            if precios>0:
                return precios
            else:
                print("Precio debe ser un valor positivo")
def obtenerCantidad():
    while True:
        cantidad=int(input("Cantidad: "))
        if cantidad>0:
            return cantidad
        else:
            print("La cantidad debe tener un valor positivo")

def mostrarProductos(inventario):
    if len(inventario)==0:
            print("No existe productos en inventario")
    else:
        print("\n****Inventario*****")
        for codigo, productos in inventario.items():
            print("****************")
            print("Codigo: ",codigo)
            print("Nombre: ", productos["nombre"])
            print("Precio: ", productos["precio"])
            print("Cantidad: ", productos["cantidad"])

def buscarProducto(inventario,codigo):
    if codigo in inventario:
        print(inventario[codigo])
        return True
    else:
        print("Codigo inexistente")
        return False

def actualizarProducto(inventario):
    codigo=input("Código para Actualizar: ")
    if buscarProducto(inventario,codigo):
        print("Escoja que desea actualizar")
        print("1.Actualizar Precio")
        print("2.Actualizar Cantidad")
        print("3.Actualizar Ambos")
        print("4. Salir")
        opciones=int(input("Escriba que desea actualizar: "))
        while True:
            if opciones==1:
                actualizarPrecio(inventario,codigo)
                return
            elif opciones==2:
                actualizarCantidad(inventario,codigo)
                return
            elif opciones==3:
                actualizarPrecio(inventario,codigo)
                actualizarCantidad(inventario,codigo)
                return
            elif opciones==4:
                return
            else:
                print("Escoja una opcion correcta")

    else:
        print("Adios")

def actualizarPrecio(inventario,codigo):
        nuevoPrecio=obtenerPrecio()
        inventario[codigo]["precio"]=nuevoPrecio
        print("Precio Actualizado")

def actualizarCantidad(inventario,codigo):
    nuevaCantidad=obtenerCantidad()
    inventario[codigo]["cantidad"]=nuevaCantidad
    print("Cantidad Actualizada")



def menu():
    print("\n*****MENU*******")
    print("1. Registrar Producto")
    print("2. Mostrar Productos")
    print("3. Buscar Producto")
    print("4. Actualizar informacion")
    print("5. Registrar Venta")
    print("6. Consultar Inventario")
    print("7. Reporte de Ventas")
    print("8. Salir")


while True:
    menu()
    opciones=int(input("Ingrese la opcion: "))
    if opciones==1:
        agregarProducto(inventario)
    elif opciones==8:
        break
    elif opciones==2:
        mostrarProductos(inventario)
    elif opciones==3:
        codigo=input("Código para buscar: ")
        buscarProducto(inventario,codigo)
    elif opciones==4:
        actualizarProducto(inventario)