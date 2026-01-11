# Colores de la terminal (Testeado en la terminal de Ubuntu 25.10 y en Windows 11. Sí funcionan los colores!!) (https://sentry.io/answers/print-colored-text-to-terminal-with-python/)
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[0m' # called to return to standard terminal text color

# ** VARIABLES **
error_message = "" # mensaje de error para el While si el usuario elije una opción que no existe
shop_active = True # Para el while del programa
shopping_cart = [] # Carrito de compras
catalog = [{
        "id": 1,
        "nombre": "GeForce RTX™ 3060 Ti VENTUS 2X 8G OCV1 LHR",
        "categoria": "Tecnología",
        "precio": 469990
    },
    {
        "id": 2,
        "nombre": "AMD Ryzen™ 7 9800X3D",
        "categoria": "Tecnología",
        "precio": 510500
    },
    {
        "id": 3,
        "nombre": "Logitech G502 Hero",
        "categoria": "Tecnología",
        "precio": 45990
    },
    {
        "id": 4, "nombre": "X870 AORUS ELITE WIFI7 ICE",
        "categoria": "Tecnología",
        "precio": 333990
    },
    {
        "id": 5, "nombre": "AORUS WATERFORCE II 360 ICE",
        "categoria": "Tecnología",
        "precio": 109900
    },
    {
        "id": 6,
        "nombre": "Cortina Roller Duo Zebra Día Y Noche 120 X 200 Cm Negro Guiza",
        "categoria": "Hogar",
        "precio": 17182
    },
    {
        "id": 7,
        "nombre": "Sabana 1800 Hotel Ultra Suave Com Funda Bordada 2 Plazas Color Blanco",
        "categoria": "Hogar",
        "precio": 18990
    },
    {
        "id": 8,
        "nombre": "Cubrecolchon. 2 Plazas Acolchado + 2 Fundas Para Almohada Color Blanco 100% Impermeable",
        "categoria": "Hogar",
        "precio": 9990
    },
    {
        "id": 9,
        "nombre": "Velador John Natural Form",
        "categoria": "Hogar",
        "precio": 119900
    },
    {
        "id": 10,
        "nombre": "Base De Cama Cambril Con Respaldo Zinus 2 Plazas 150x190x30cm Color Gris",
        "categoria": "Hogar",
        "precio": 139990
    },
    {
        "id": 11,
        "nombre": "iPhone 13",
        "categoria": "Tecnología",
        "precio": 759990
    }] # Catalogo de los productos

# ** FUNCIONES **
def show_error_message(arg): # Cambiar el mensaje del error (terminando el trabajo ni sé para que lo hice, pero lo dejo para que no se rompa el código)
    global error_message
    if arg == "does_not_exist":
        error_message = (f"{RED}Error: Esta opción no existe. Elija otra.{RESET}")
    elif arg == "reset":
        error_message = ""

# 1. Mostrar catálogo de productos
def show_catalog():
    global catalog
    while True:
        print(f"{BLUE}========== CATÁLOGO DE PRODUCTOS =========={RESET}")
        print(f"Nombre del producto - {YELLOW}Categoria{RESET} - {GREEN}Precio{RESET}")
        
        # Mostrar todos los productos del catálogo
        for product in catalog:
            print(f"- {product["nombre"]} {YELLOW}({product["categoria"]}){RESET} {GREEN}CLP${product["precio"]:,}{RESET}")
            
        if input(f"""0) Volver
Elija una opción: """) == "0": # volver al menú principal
            show_error_message("reset")
            break
        else:
            show_error_message("does_not_exist")

# 2. Buscar en el catálogo
def search_catalog():
    global catalog
    while True:
        found_list = [] # Lista de los productos encontrados
        search = input(f"""{YELLOW}Ingresa lo que quieres buscar. Escribe "0" para volver al menú principal.{RESET}\nBuscar: """).lower() # para que sea case insensitive
        
        # Mostrar todos los productos del catálogo
        if search == "0": # volver al menú principal
            break
        else:
            # Búsqueda por nombre o categoría
            for product in catalog:
                if search.lower() in product["nombre"].lower() or search.lower() in product["categoria"].lower(): # puse .lower en todas partes para que funcionara pero no sé cuales funcionan y cuales sobran xD
                    found_list.append(product["nombre"])
        
        if len(found_list) > 1:
            print(f"{GREEN}Se encontraron {len(found_list)} productos:{RESET}")
        elif len(found_list) == 1:
            print(f"{GREEN}Se encontró {len(found_list)} producto:{RESET}")
        else:
            print(f"{RED}No se encontró ningún producto.{RESET}")
        
        for found in found_list:
            print("-", found)
        print("")

# 3. Agregar producto al carrito
def add_to_cart():
    print(f"{BLUE}========== AÑADIR AL CARRITO =========={RESET}")
    print(f"{MAGENTA}Para agregar un producto al carrito, escriba el número correspondiente al producto.{RESET}")
    global shopping_cart
    global catalog
    for index, product in enumerate(catalog, 1):
            print(f"{index}) {product["nombre"]} {YELLOW}({product["categoria"]}){RESET} {GREEN}CLP${product["precio"]:,}{RESET}")
    user_selection = input(f"""0) Listo\n{error_message}\nElija una opción: """)
    
    while True:
        # Elegir que producto agregar al carro
        if user_selection ==  "0": # volver al menú principal
            show_error_message("reset")
            break
        else:
            add_to_cart_amount = int(input("¿Cuántos?: ")) # maña del paiton (?)
            
            for i in range(add_to_cart_amount):
                shopping_cart.append(catalog[int(user_selection)-1])
                
            print(f"{GREEN}{catalog[int(user_selection)-1]["nombre"]} (x{add_to_cart_amount}) agregado con éxito al carrito.{RESET}")
            break

# 4. Ver total del carrito
def cart_total():
    global shopping_cart
    while True:
        print(f"{BLUE}========== CARRITO DE COMPRAS =========={RESET}")
        cart_total_amount = 0
        if len(shopping_cart) == 0:
            print(f"{RED}Su carrito está vacío.", RESET)
        else:
            for product in shopping_cart:
                print(f"- {product["nombre"]} (CLP${product['precio']})")
                cart_total_amount += product["precio"]
        print(f"{GREEN}TOTAL: CLP${cart_total_amount}{RESET}")
            
            
        if input(f"""0) Volver \nElija una opción: """) == "0": # volver al menú principal
                show_error_message("reset")
                break
        else:
            show_error_message("does_not_exist")
            

# 5. Vaciar carrito
def empty_cart():
    global error_message
    shopping_cart.clear()
    error_message = (f"{GREEN}Su carrito se vació con éxito.{RESET}")



# ** MENU PRINCIPAL WHILE **

while shop_active == True:
    choice = input(f"""
¡Bienvenid@ a tu E-commerce!
{BLUE}1){RESET} Ver catálogo de productos
{BLUE}2){RESET} Buscar producto por nombre o categoría
{BLUE}3){RESET} Agregar producto al carrito
{BLUE}4){RESET} Ver carrito y total
{BLUE}5){RESET} Vaciar carrito
{BLUE}0){RESET} Salir
{error_message}
Elija una opción: """)
    match choice:
        case "1":
            show_catalog()
        case "2":
            search_catalog()
        case "3":
            add_to_cart()
        case "4":
            cart_total()
        case "5":
            empty_cart()
        case "0":
            print(f"{GREEN}Su sesión ha finalizado. ¡Gracias por visitar!")
            shop_active = False
        case _:
            show_error_message("does_not_exist")