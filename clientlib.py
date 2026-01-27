import userlib, shopping_cartlib, cataloglib, exceptionslib

# Rol cliente

class Client(userlib.User, shopping_cartlib.ShoppingCart): 
    def __init__(self, name):
        self.name = name
        self.shopping_cart = shopping_cartlib.ShoppingCart()
        
    # 1. Ver catálogo de productos
    def show_catalog(self):
        """
        Muestra en consola el catalogo completo de productos guardados en la variable 'catalog' (diccionario).
        """
        
        try:
            if len(cataloglib.catalog) > 0: # si la longitud del catalogo es mayor a 1.. (osea, hay productos)
                for product in cataloglib.catalog: # Mostrar todos los productos del catálogo
                    print(f"- {product["nombre"]} ({product["categoria"]}) CLP${product["precio"]:,}")
            else: # y si no levantar un error.
                raise exceptionslib.NoProductsFound("No products to show, catalog is empty")
        except:
            raise
    
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
                raise exceptionslib.NoProductsFound(f"No products found, search returned {len(self.found_list)} items")
        except:
            raise
        else:
            for self.found in self.found_list:
                print("-", self.found)

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