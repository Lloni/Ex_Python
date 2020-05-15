user1 = None
user2 = None
user3 = None
pass1 = None
pass2 = None
pass3 = None
option1 = 0
option2 = 0
phone = None
email = None
email_flag = None

print("BIENVENID@")
# SE EJECUTARÁ TODO EL CÓDIGO INDENTADO MIENTRAS EL USUARIO NO SELECCIONE LA OPCIÓN 3
while (option1 != 3):
    print("\nPor favor seleccione una opción")
    print("\t1) Iniciar sesión")
    print("\t2) Registrar usuario")
    print("\t3) Salir") 
    try:
        option1 = int(input("Ingrese su opción (1, 2 ó 3): "))
    except:
        print("\nERROR: DEBE ELEGIR UN NÚMERO")
    # SI SE INGRESA UN NÚMERO INCORRECTO
    if (option1 < 1 or option1 > 3):
        print("\nERROR: DEBE INGRESAR UN NÚMERO DEL 1 AL 3")
    
    # OPCIÓN REGISTRAR USUARIO NUEVO
    elif (option1 == 2):
        if (user1 == None):
            print("\nIngrese un nombre de usuario:")
            user1 = input()
            print("\nIngrese una contraseña:")
            pass1 = input()
        elif (user2 == None):
            print("\nIngrese un nombre de usuario:")
            user2 = input()
            print("\nIngrese una contraseña:")
            pass1 = input()
        elif (user3 == None):
            print("\nIngrese un nombre de usuario:")
            user3 = input()
            print("\nIngrese una contraseña:")
            pass3 = input()
        else:
            print("\nERROR: YA NO HAY MÁS USUARIOS DISPONIBLES")

    # OPCIÓN INICIAR SESIÓN    
    elif (option1 == 1):
        if (user1 == None and user2 == None and user3 == None):
            print("\nERROR: PRIMERO DEBE REGISTRAR UN USUARIO")
        else: 
            print("\nIngrese su nombre de usuario:")
            user_login = input()
            print("\nIngrese su contraseña:")
            pass_login = input()

            if ((user_login == user1 and pass_login == pass1) or (user_login == user2 and pass_login == pass2) or (user_login == user3 and pass_login == pass3)):
                print("\nBienvenid@,", user_login)

                # SE EJECUTARÁ TODO EL CÓDIGO INDENTADO MIENTRAS EL USUARIO NO SELECCIONE LA OPCIÓN 3
                while (option2 != 3):
                    print("\nPor favor seleccione una opción")
                    print("\t1) Realizar llamada")
                    print("\t2) Enviar correo electrónico")
                    print("\t3) Cerrar sesion")
                    try:
                        option2 = int(input("Ingrese su opción (1, 2 ó 3): "))
                    except:
                        print("\nERROR: DEBE ELEGIR UN NÚMERO")
                    if (option2 < 1 or option1 > 3):
                        print("\nERROR: DEBE INGRESAR UN NÚMERO DEL 1 AL 3")
                    
                    # OPCIÓN REALIZAR LLAMADA
                    elif (option2 == 1):                
                        print("\nIndique el número al cual llamar (8 dígitos sin espacios): ")
                        while (len(str(phone)) != 8):
                            try:
                                phone = int(input())
                            except:
                                print("\nERROR: DEBE INGRESAR UN NÚMERO (SIN ESPACIOS)")
                            if (len(str(phone)) != 8):
                                print("\nERROR: DEBE INGRESAR UN NÚMERO DE OCHO DÍGITOS")
                        print("\nGracias.\nConectaremos su llamada")
                    
                    # OPCIÓN ENVIAR CORREO
                    elif (option2 == 2):                
                        print("\nIndique la dirección de correo a ingresar: ")
                        while not(email_flag):
                            email = input()
                            email_flag = "@" in email #registra en un boolean si está presente la "@"
                            if not(email_flag):
                                print("\nERROR: DEBE INGRESAR UNA DIRECCIÓN DE CORREO VÁLIDA")
                        print("\nINGRESE SU MENSAJE: ")
                        email_message = input()
                        print("\nMuchas gracias. Se ha registrado el siguiente mensaje para el correo", email,":")
                        print("<<", email_message,">>\n")
                        email = None #Esto en caso de querer mandar otro correo
                    elif (option2 == 3)
                        print("\nUd. ha cerrado sesión.")
            else:
                print("ERROR: USUARIO Y/O CONTRASEÑA INCORRECTOS")

print("""\n           88                                  
           88                                  
           88                                  
 ,adPPYba, 88,dPPYba,  ,adPPYYba,  ,adPPYba,   
a8"     "" 88P'    "8a ""     `Y8 a8"     "8a  
8b         88       88 ,adPPPPP88 8b       d8  
"8a,   ,aa 88       88 88,    ,88 "8a,   ,a8"  
 `"Ybbd8"' 88       88 `"8bbdP"Y8  `"YbbdP"'   """)