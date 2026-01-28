import cataloglib

# Excepciones Personalizadas
class NoProductsFound(Exception): # Catalogo Vacío
    def __init__(self, message):
        super().__init__(message)

class CantBeZero(Exception): # No puede ser 0
    def __init__(self, message):
        super().__init__(message)
        
class IDNotFound(Exception): # ID no encontrada
    def __init__(self, message):
        super().__init__(message)
    

# Clase carrito
class ShoppingCart: 
    def __init__(self):
        self.products = []
        
    # 3. Agregar producto al carrito
    def add_to_cart(self, id, amount): 
        """
        Método para agregar uno o varios productos al carrito
        
        :param id: id del producto para agregar al carrito
        :param amount: cantidad del producto a agregar al carrito
        """
        # for self.index, self.product in enumerate(catalog, 1):
        #         print(f"{self.index}) {self.product["nombre"]} ({self.product["categoria"]}) CLP${self.product["precio"]:,}")
        try:
            if amount > 0:
                for i in range(amount):
                    self.products.append(cataloglib.catalog[int(id)-1])
            else:
                raise CantBeZero("Cannot add 0 products")
        except:
            raise
        else:
            return f"{cataloglib.catalog[int(id)-1]["nombre"]} (x{amount}) agregado con éxito al carrito."

# Base para admin y cliente
class User: 
    def __init__(self, name):
        self.name = name
        
    def log_out(self):
        print(f"Su sesión ha finalizado. ¡Gracias por visitar!")
        # queria poner el break aquí pero no funciona :'v
        
    def show_catalog(self): # Listar/Ver catálogo de productos
        """
        Muestra en consola el catalogo completo de productos guardados en la variable 'catalog' (diccionario).
        """
        
        try:
            print(" CATÁLOGO DE PRODUCTOS ".center(75,"="))
            if len(cataloglib.catalog) > 0: # si la longitud del catalogo es mayor a 1.. (osea, hay productos)
                for product in cataloglib.catalog: # Mostrar todos los productos del catálogo
                    print(f"- {product["nombre"]} ({product["categoria"]}) CLP${product["precio"]:,}")
            else: # ...y si no levantar un error.
                raise NoProductsFound("No products to show, catalog is empty")
            print("")
        except:
            raise
    
    # getter y setter de name para testear
    def get_name(self):
        return self.name
    
    def set_name(self, arg):
        self.name = arg

# Rol cliente
class Client(User, ShoppingCart): 
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()
    
    # 2. Buscar productos por nombre o categoría
    def search_catalog(self, search):
        """
        Método para buscar un producto en el catálogo por nombre o categoría.
        
        :param search: string a buscar en el catálogo.
        """
        self.search = search
        self.found_list = [] # Lista de los productos encontrados
        
        try:
            for self.product in cataloglib.catalog:
                    if self.search.lower() in self.product["nombre"].lower() or self.search.lower() in self.product["categoria"].lower(): # puse .lower en todas partes para que funcionara pero no sé cuales funcionan y cuales sobran xD
                        self.found_list.append(self.product["nombre"])
            if len(self.found_list) > 0:
                print(f"Se encontraron {len(self.found_list)} producto(s):")
            else:
                raise NoProductsFound(f"No products found, search returned {len(self.found_list)} items")
        except:
            raise
        else:
            for self.found in self.found_list:
                print("-", self.found)

# Admin hereda de Client y Client hereda de User
class Admin(Client): 
    def __init__(self, name):
        super().__init__(name)
        
    # Login y menú de Admin
    def log_in(self): 
        while True:
            choice = input(f"""
ADMIN PANEL 9000 (E-commerce Parque Placentero):

Sesión iniciada como: {self.name}

1) Listar productos del catálogo
2) Crear nuevo producto
3) Actualizar producto
4) Eliminar producto
5) Guardar catálogo en un archivo
0) Salir

Elija una opción: """)
            try:
                match choice:
                    case "1": # Listar productos del catálogo
                        while True:
                            self.show_catalog()
                            input("Presione cualquier tecla (y después ENTER) para volver...")
                            break
                    case "2": # Crear nuevo producto
                        id = input("Ingrese la ID: ")
                        name = input("Ingrese el nombre: ")
                        category = input("Ingrese la categoría: ")
                        price = input("Ingrese el precio: ")
                        
                        self.create_product(id, name, category, price)
                    case "3": # Actualizar producto
                        self.update_product()
                    case "4": # Eliminar producto
                        self.remove_product(int(input("Ingrese la id del producto a eliminar: ")))
                        # No elimina el producto de la id que se ingresa, se elimina desde el indice de la lista que se ingresa. Asi que si se pone eliminar "1", eventualmente se borrará todo el catálogo. Lo hice así para no complicarme la vida, y no romper más el código. (Lo hubieran visto antes como estaba D:) Pero me perdono porque soy beginner.-
                    case "5": # Guardar catálogo en un archivo
                        self.save_catalog_to_file()
                    case "0": # Salir
                        self.log_out()
                        break
                    case _:
                        raise IndexError("This option does not exist.")
            except:
                raise

    # Crear nuevo producto
    def create_product(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        
        new_product = {"id": self.id, "nombre": self.name, "categoria": self.category, "precio": self.price}
    
    # Necesito ayuda para acceder al valor de "id" (Diccionario dentro de lista) TypeError: argument of type 'int' is not a container or iterable
        try:
            #for self.product in cataloglib.catalog:
            for i in range(len(cataloglib.catalog)):
                if self.id != cataloglib.catalog[i]["id"]:
                    cataloglib.catalog.append(new_product)
                else:
                    raise IDNotFound("A product with this ID already exists in the catalog")
        except:
            raise
        else:
            print(f"Se agregó un nuevo producto al catálogo con éxito:\nID: {self.id} \nNombre: {self.name} \nCategoría: {self.category} \nPrecio: CLP${self.price:,}")
        

    def update_product(self, id, arg): # Actualizar producto
        """
        Docstring for update_product
        
        :param self: Description
        :param id: Description
        :param arg: Description
        """
        pass
    
    def remove_product(self, id): # Eliminar producto del catálogo
        """
        Eliminar un producto del catálogo.
        
        :param id: id del producto a eliminar
        """
        
        try:
            cataloglib.catalog.pop(id)
            print(f"Producto {id} eliminado con éxito.")
        except:
            raise IDNotFound(f"Product with ID {id} not found.")

# Guardar catálogo en un archivo
    def save_catalog_to_file(self):
        try:
            if len(cataloglib.catalog) > 0: # si la longitud del catalogo es mayor a 1.. (osea, hay productos)
                with open("catalog.txt", "w", encoding="utf-8") as catalog_file:
                    for product in cataloglib.catalog: 
                        catalog_file.write(f"- {product["nombre"]} ({product["categoria"]}) CLP${product["precio"]:,}\n")
            else: # y si no levantar un error.
                raise NoProductsFound("Cannot create file, catalog is empty")
        except:
            raise
        else:
            print("Successfully created a file with all products from the catalog.")
    
    # 4. Ver carrito y total
    # def cart_total(self): 
    #     while True:
    #         print(f"========== CARRITO DE COMPRAS ==========")
    #         cart_total_amount = 0
    #         if len(self.shopping_cart) == 0:
    #             print(f"Su carrito está vacío.", RESET)
    #         else:
    #             for product in shopping_cart:
    #                 print(f"- {product["nombre"]} (CLP${product['precio']})")
    #                 cart_total_amount += product["precio"]
    #         print(f"TOTAL: CLP${cart_total_amount}")
    #         if input(f"""0) Volver \nElija una opción: """) == "0": # volver al menú principal
    #                 show_error_message("reset")
    #                 break
    #         else:
    #             show_error_message("does_not_exist")
                
    # 5. Confirmar compra
    # def confirm_purchase(): 
    #     pass

# ** MENU PRINCIPAL WHILE **
while True:
    choice = input(f"""
E-commerce Parque Placentero:
Iniciar sesión como:
1) ADMINISTRADOR
2) Cliente
0) Salir

Elija una opción: """)
    try:
        match choice:
            case "1": # Admin
                user_admin = Admin(input("Ingrese su nombre: "))
                user_admin.log_in()
            case "2": # Cliente
                user_client = Client(input("Ingrese su nombre: "))
                user_client.log_in()
            case "0":
                print(f"Su sesión ha finalizado. ¡Gracias por visitar!")
                break
            case _:
                raise IndexError("This option does not exist.")
    except:
        raise