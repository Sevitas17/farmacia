#Agregar Producto
inventario= {}
ventas = []


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

def registrarVenta(inventario, ventas):
    if len(inventario) == 0:
        print("No existen productos")
        return

    cliente = input("Nombre del cliente: ")
    detalleVenta = []
    subtotal = 0

    while True:
        codigo = input("Ingrese el código del producto o escribir - para salir : ")
        if codigo == "-":
            break

        if codigo not in inventario:
            print("Error de codigo , intente de nuevo")
            continue

        producto = inventario[codigo]
        cantidadDisponible = producto["cantidad"]
        print(f"Disponible: {cantidadDisponible}, Precio unitario: {producto['precio']}")

        cantidadVendida = obtenerCantidad()

        if cantidadVendida > cantidadDisponible:
            print("No hay suficiente cantidad disponible para esa venta")
            continue

        totalproducto = cantidadVendida * producto["precio"]
        subtotal += totalproducto

        inventario[codigo]["cantidad"] -= cantidadVendida

        detalleVenta.append({
            "codigo": codigo,
            "nombre": producto["nombre"],
            "cantidad": cantidadVendida,
            "precioUnitario": producto["precio"],
            "totalproducto": totalproducto,
        })

        print("Producto agregado a la venta")

    if len(detalleVenta) == 0:
        print("Error no se seleccionaron productos")
        return

    valorIva = subtotal * 0.15
    total = subtotal + valorIva

    venta = {
        "cliente": cliente,
        "detalle": detalleVenta,
        "subtotal": subtotal,
        "iva": valorIva,
        "total": total,
    }
    ventas.append(venta)
    imprimirFactura(venta)


def imprimirFactura(venta):
    print("\n********* FACTURA ********")
    print("Cliente:", venta["cliente"])
    print("*************************")
    for item in venta["detalle"]:
        print(f"{item['nombre']} x {item['cantidad']}  =  ${item['totalproducto']:.2f}")
    print("----------------------------")
    print(f"Subtotal:  ${venta['subtotal']:.2f}")
    print(f"IVA (15%): ${venta['iva']:.2f}")
    print(f"TOTAL:     ${venta['total']:.2f}")
    print("*************************")

def consultarInventario(inventario):
    if len(inventario) == 0:
        print("No existe productos en inventario")
        return
    
    print("\n****Inventario*****")
    for codigo, productos in inventario.items():
        print("****************")
        print("Codigo: ", codigo)
        print("Nombre: ", productos["nombre"])
        print("Cantidad: ", productos["cantidad"])   
        if productos["cantidad"] == 0:
            print("AGOTADO")
        else:
            print("DISPONIBLE")

        
def reporteVentas(ventas):
    if len(ventas) == 0:
        print("No hay ventas registradas para generar el reporte.")
        return
    print("\n*****REPORTE DE VENTAS****")
    productos_vendidos = {}
    total_subtotal = 0
    total_iva = 0
    total_general = 0
    for venta in ventas:
        total_subtotal += venta["subtotal"]
        total_iva += venta["iva"]
        total_general += venta["total"]
        
        for item in venta["detalle"]:
            nombre = item["nombre"]
            cantidad = item["cantidad"]
            
            if nombre in productos_vendidos:
                productos_vendidos[nombre] += cantidad
            else:
                productos_vendidos[nombre] = cantidad
                
    print(f"Total de facturas emitidas: {len(ventas)}")
    print(f"Subtotal acumulado:  ${total_subtotal:.2f}")
    print(f"IVA (15%) acumulado: ${total_iva:.2f}")
    print(f"TOTAL RECAUDADO:     ${total_general:.2f}")
    
def salirMenu():
    print("\n****Gracias por usar el programa****")
    return False

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
    elif opciones==5:
        registrarVenta(inventario, ventas)
    elif opciones==6:
        consultarInventario(inventario)
    elif opciones == 7:
        reporteVentas(ventas)
    elif opciones == 8:
        salirMenu()
    else:
        print("\nOpcion no valida.")