Clave2 = "admin2021" #A)
intentos = 3
CantRos = 0
CantCBA = 0
CantBA = 0
option=-1
option2=-1
repeat=-1
while(1):
    print("MENU PRINCIPAL:\n\n1. Empresas\n2. Clientes\n0.Salir") #B)
    while(1): #bucle infinito con condicion de salida, simula un do-while (hacer mientras)
        try:
            option=int(input())
        except ValueError:
            print("Por favor ingrese un numero entero")
        if option == 1 or option == 2 or option == 0: #condicion de salida del bucle
            break

    if option == 2: #C) - CLIENTES
        print("programa en proceso.")

    elif option == 1: #D) EMPRESAS
        while(1):
            if intentos > 0:
                Clave1 = input("Ingrese la clave, {} intentos restantes.".format(intentos)) #ingreso de datos
                intentos-=1 #CONTADOR DE INTENTOS FALLIDOS
            else:
                print("clave incorrecta, agotaste los intentos") #mensaje de error despues de fallar 3 veces
                input() #simplemente para que no spamee la consola con carteles.
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
                print("\nRosario: ",CantRos,"\nCordoba: ",CantCBA,"\nBuenos Aires: ",CantBA)
                if CantRos > CantCBA: #SELECCIONA LA CIUDAD CON MAS EMPRESAS
                    if CantRos > CantBA:
                        print("Rosario es la ciudad con mas empresas")
                    else:
                        print("Buenos Aires es la ciudad con mas empresas")
                elif CantCBA > CantBA:
                    print("Cordoba es la ciudad con mas empresas")
                else:
                    print("Buenos Aires es la ciudad con mas empresas")
            elif option2 == 2:
                pass
            elif option2 == 3:
                pass
            elif option2 == 0: #condicion de salida del bucle
                break
    intentos = 3
    if option == 0:
        break