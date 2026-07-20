def validar_texto(texto):

    if texto.strip() == "":
        return False
    return True


def validar_clasificacion(clasificacion):
    if clasificacion == "E" or clasificacion == "T" or clasificacion == "M":
        return True
    return False


def validar_multiplayer(valor):
    if valor == "s" or valor == "n":
        return True
    return False


def validar_precio(precio):
    if precio > 0:
        return True
    return False


def validar_stock(stock):
    if stock >= 0:
        return True
    return False


def leer_opcion():
    opcion_valida = False
    opcion = 0
    while opcion_valida == False:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion >= 1 and opcion <= 6:
                opcion_valida = True
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")
    return opcion


def ordenar_por_titulo(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            titulo1 = lista[j]
            titulo2 = lista[j + 1]
            if titulo1 > titulo2:
                temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal
    return lista


def stock_plataforma(plataforma, juegos, inventario):
    total_stock = 0
    for codigo in juegos:
        plataforma_juego = juegos[codigo][1]
        if plataforma_juego == plataforma:
            stock_juego = inventario[codigo][1]
            total_stock = total_stock + stock_juego
    print(f"El total de stock disponibles es:", {total_stock})



def busqueda_precio(p_min, p_max, juegos, inventario):
    resultados = []
    for codigo in inventario:
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        if precio >= p_min and precio <= p_max and stock != 0:
            titulo = juegos[codigo][0]
            resultados.append(titulo + "--" + codigo)

    resultados = ordenar_por_titulo(resultados)

    if len(resultados) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        print("Los juegos encontrados son:", resultados)


def buscar_codigo(codigo, inventario):
    if codigo in inventario:
        return True
    return False


def actualizar_precio(codigo, nuevo_precio, inventario):
    if buscar_codigo(codigo, inventario) == True:
        inventario[codigo][0] = nuevo_precio
        return True
    return False


def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    if buscar_codigo(codigo, inventario) == True:
        return False
    juegos[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inventario[codigo] = [precio, stock]
    return True


def eliminar_juego(codigo, juegos, inventario):
    if buscar_codigo(codigo, inventario) == True:
        del juegos[codigo]
        del inventario[codigo]
        return True
    return False