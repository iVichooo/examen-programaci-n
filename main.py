from os import system

from funciones import * 






    
juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
        'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
        'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
        'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
        'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
        'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
    }

inventario = {
        'G001': [9990, 7],
        'G002': [19990, 0],
        'G003': [42990, 3],
        'G004': [14990, 5],
        'G005': [17990, 9],
        'G006': [39990, 2],
    }

programa_activo = True

while programa_activo == True:

        print("======= MENU PRINCIPAL =======")
        print("1. Stock por plataforma")
        print("2. Busqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()

    
        if opcion == 1:
            plataforma = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plataforma, juegos, inventario)

        
        elif opcion == 2:
            datos_validos = False
            while datos_validos == False:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        datos_validos = True
                    else:
                        print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, juegos, inventario)

       
        elif opcion == 3:
            respuesta = "s"
            while respuesta == "s":
                codigo = input("Ingrese codigo del juego: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                except ValueError:
                    nuevo_precio = -1

                if validar_precio(nuevo_precio) == True:
                    actualizado = actualizar_precio(codigo, nuevo_precio, inventario)
                    if actualizado == True:
                        print("Precio actualizado")
                    else:
                        print("El codigo no existe")
                else:
                    print("El precio ingresado no es valido")

                respuesta = input("Desea actualizar otro precio (s/n)?: ")

        
        elif opcion == 4:
            codigo = input("Ingrese codigo del juego: ")
            titulo = input("Ingrese titulo: ")
            plataforma = input("Ingrese plataforma: ")
            genero = input("Ingrese genero: ")
            clasificacion = input("Ingrese clasificacion: ")
            multiplayer_texto = input("Es multiplayer? (s/n): ")
            editor = input("Ingrese editor: ")

            try:
                precio = int(input("Ingrese precio: "))
            except ValueError:
                precio = -1

            try:
                stock = int(input("Ingrese stock: "))
            except ValueError:
                stock = -1

            codigo_valido = validar_texto(codigo) and buscar_codigo(codigo, inventario) == False
            titulo_valido = validar_texto(titulo)
            plataforma_valida = validar_texto(plataforma)
            genero_valido = validar_texto(genero)
            clasificacion_valida = validar_clasificacion(clasificacion)
            multiplayer_valido = validar_multiplayer(multiplayer_texto)
            editor_valido = validar_texto(editor)
            precio_valido = validar_precio(precio)
            stock_valido = validar_stock(stock)

            if codigo_valido == False:
                print("El codigo no es valido o ya existe")
            elif titulo_valido == False:
                print("El titulo no es valido")
            elif plataforma_valida == False:
                print("La plataforma no es valida")
            elif genero_valido == False:
                print("El genero no es valido")
            elif clasificacion_valida == False:
                print("La clasificacion no es valida")
            elif multiplayer_valido == False:
                print("El valor de multiplayer no es valido")
            elif editor_valido == False:
                print("El editor no es valido")
            elif precio_valido == False:
                print("El precio no es valido")
            elif stock_valido == False:
                print("El stock no es valido")
            else:
                if multiplayer_texto == "s":
                    multiplayer = True
                else:
                    multiplayer = False

                agregado = agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario)
                if agregado == True:
                    print("Juego agregado")
                else:
                    print("El codigo ya existe")

        
        elif opcion == 5:
            codigo = input("Ingrese codigo del juego a eliminar: ")
            eliminado = eliminar_juego(codigo, juegos, inventario)
            if eliminado == True:
                print("Juego eliminado")
            else:
                print("El codigo no existe")

    
        elif opcion == 6:
            programa_activo = False
            print("Programa finalizado.")



