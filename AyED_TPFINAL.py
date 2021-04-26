Clave2 = "admin2021" #A) - Constante de clave.
CantRos, CantCBA, CantBA = 0, 0, 0 # Contadores para la cantidad de empresas por ciudad, tipo int.
option, option2, repeat, intentos = -1, -1, -1, 3 #Variables auxiliares para guardar datos de los menus.
while(1):
    print("MENU PRINCIPAL:\n\n1. Empresas\n2. Clientes\n0.Salir") #B)
    while(1): #bucle infinito con condicion de salida, simula un do-while (hacer mientras)
        try:
            option=int(input())
        except ValueError: #Para que no chrashee el programa si ingresan un valor que no pueda convertirse a entero.
            print("Por favor ingrese un numero entero")
        if option == 1 or option == 2 or option == 0: #condicion de salida del bucle
            break

    if option == 2: #C) - CLIENTES
        print("programa en proceso.")

    elif option == 1: #D) EMPRESAS
        while(1):
            if intentos > 0:
                Clave1 = input(f"Ingrese la clave, {intentos} intentos restantes.") #ingreso de datos
                intentos-=1 #CONTADOR DE INTENTOS FALLIDOS
            else:
                print("clave incorrecta, agotaste los intentos") #mensaje de error despues de fallar 3 veces
                input() #espera a que se toque un enter y luego cierra el programa.
                raise SystemExit #cierra el programa.
            if Clave1 == Clave2: #VALIDACION DE CLAVE, condicion de salida del bucle
                break

        while(1): #MENU DE EMPRESA (CLAVE ACEPTADA)
            print("MENU EMPRESAS DESARROLLADORAS :\n\n1. Alta de EMPRESAS \n2. .\n3. .\n0. Volver al menú principal")
            while(1):
                option2 = int(input())
                if option == 1 or option == 2 or option == 3 or option == 0: #condicion de salida del bucle
                    break

            if option2 == 1: #ALTA DE EMPRESAS
                while(1):
                    cod_emp =input("\nIngrese el codigo de la empresa\n")
                    nombre = input("\nIngrese el nombre de la empresa\n")
                    direccion = input("\nIngrese la direccion de la empresa\n")
                    mail = input("\nIngrese el mail de la empresa\n")
                    while(1):
                        try:
                            telefono = int(input("\nIngrese el telefono de la empresa\n"))
                            break
                        except ValueError:
                            print("\nEl numero no es valido\n")
                    while(1):
                        cod_ciudad = input("\nIngrese el codigo de ciudad de la empresa\n")
                        if cod_ciudad == "ROS" or cod_ciudad == "CBA" or cod_ciudad == "BA":
                            break
                        else:
                            print("codigo no valido")
                    print("\nDesea ingresar otra empresa?\n1. Si\n2. No\n")
                    if cod_ciudad == "ROS":
                        CantRos += 1
                    elif cod_ciudad == "CBA":
                        CantCBA += 1
                    elif cod_ciudad == "BA":
                        CantBA += 1
                    while(1):
                        repeat=int(input())
                        if repeat==1 or repeat==2: #condicion de salida del bucle
                            break
                    if(repeat==2): #condicion de salida del bucle
                        break
                print(f"\nRosario: {CantRos}\nCordoba: {CantCBA}\nBuenos Aires: {CantBA})
                #SELECCIONA LA CIUDAD CON MAS EMPRESAS
                if CantRos != CantCBA and CantRos!=CantBA and CantCBA != CantBA: #todos distintos
                    if CantRos > CantCBA:
                        if CantRos > CantBA:
                            print("Rosario es la ciudad con mas empresas")
                        else:
                            print("Buenos Aires es la ciudad con mas empresas")
                    elif CantCBA > CantBA:
                        print("Cordoba es la ciudad con mas empresas")
                    else:
                        print("Buenos Aires es la ciudad con mas empresas")
                elif CantRos == CantCBA and CantRos == CantBA: #todos iguales
                      print("Las 3 ciudades tienen la misma cantidad de empresas")
                else: #2 iguales
                      if CantRos == CantCBA:
                            if CantRos > CantBA:
                                print("Rosario y Cordoba tienen la mayor cantidad de empresas")
                            else:
                                print("Cordoba tiene la mayor cantidad de empresas")
                      elif CantCBA == CantBA:
                            if CantRos > CantCBA:
                                print("Rosario es la ciudad con mas empresas")
                            else:
                                print("Cordoba y Buenos Aires tienen la mayor cantidad de empresas")
                      else: #Rosario igual a BA
                            if CantCBA > CantBA:
                                print("Cordoba es la ciudad con mas empresas")
                            else:
                                print("Rosario y Buenos Aires tienen la mayor cantidad de empresas")             
            elif option2 == 2:
                pass
            elif option2 == 3:
                pass
            elif option2 == 0: #condicion de salida del bucle
                break
    intentos = 3 #Reset a los intentos para cuando vuela a ingresar la contraseña
    if option == 0: #Si se preciona 0 en el primer menu, sale del bucle principal, cerrando el programa.
        break
