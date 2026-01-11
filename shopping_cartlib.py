import exceptionslib
import cataloglib

class ShoppingCart: # Clase carrito
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
                raise exceptionslib.CantBeZero("Cannot add 0 products")
        except:
            raise
        else:
            return f"{cataloglib.catalog[int(id)-1]["nombre"]} (x{amount}) agregado con éxito al carrito."