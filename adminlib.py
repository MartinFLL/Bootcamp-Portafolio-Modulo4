import clientlib, cataloglib, exceptionslib

class Admin(clientlib.Client): # Admin hereda de Client y Client hereda de User
    def __init__(self, __name):
        super().__init__(__name)

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
                if self.id not in cataloglib.catalog["id"][i]:
                    cataloglib.catalog.append(new_product)
                else:
                    raise exceptionslib.IDNotFound("A product with this ID already exists in the catalog")
        except:
            raise
        else:
            print(f"Se agregó un nuevo producto al catálogo con éxito:\nID: {self.id} \nNombre: {self.name} \nCategoría: {self.category} \nPrecio: CLP${self.price:,}")
            
    
# Actualizar producto
    def update_product(self, id, arg):
        pass
    
# Eliminar producto del catálogo
    def remove_product(self, id):
        pass
    
# Guardar catálogo en un archivo
    def save_catalog_to_file(self):
        try:
            if len(cataloglib.catalog) > 0: # si la longitud del catalogo es mayor a 1.. (osea, hay productos)
                with open("catalog.txt", "w", encoding="utf-8") as catalog_file:
                    for product in cataloglib.catalog: 
                        catalog_file.write(f"- {product["nombre"]} ({product["categoria"]}) CLP${product["precio"]:,}\n")
            else: # y si no levantar un error.
                raise exceptionslib.NoProductsFound("Cannot create file, catalog is empty")
        except:
            raise
        else:
            print("Successfully created a file with all products from the catalog.")
    
