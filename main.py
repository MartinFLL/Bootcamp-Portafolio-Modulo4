import adminlib, cataloglib, clientlib, exceptionslib, productlib, shopping_cartlib, userlib

ADMIN = adminlib.Admin("Gabe Newell")
CLIENTE = clientlib.Client("Tim Sweeney")

# ** MENU PRINCIPAL WHILE **
while True:
    choice = input(f"""
E-commerce Parque Placentero:
Iniciar sesión como:
1) ADMIN
2) Cliente
0) Salir

Elija una opción: """)
    try:
        match choice:
            case "1": # Admin
                ADMIN.log_in()
            case "2": # Cliente
                CLIENTE.log_in()
            case "0":
                print(f"Su sesión ha finalizado. ¡Gracias por visitar!")
                break
            case _:
                raise IndexError("This option does not exist.")
    except:
        raise
    
    