class IDNotFound(Exception): # ID no encontrada
    def __init__(self, message):
        super().__init__(message)
        

catalog = [{
        "id": 1,
        "nombre": "GeForce RTX™ 3060 Ti VENTUS 2X 8G OCV1 LHR",
        "categoria": "tecnologia",
        "precio": 469990
    },
    {
        "id": 2,
        "nombre": "AMD Ryzen™ 7 9800X3D",
        "categoria": "tecnologia",
        "precio": 510500
    },
    {
        "id": 3,
        "nombre": "Logitech G502 Hero",
        "categoria": "tecnologia",
        "precio": 45990
    },
    {
        "id": 4,
        "nombre": "X870 AORUS ELITE WIFI7 ICE",
        "categoria": "tecnologia",
        "precio": 333990
    },
    {
        "id": 5,
        "nombre": "AORUS WATERFORCE II 360 ICE",
        "categoria": "tecnologia",
        "precio": 109900
    },
    {
        "id": 6,
        "nombre": "Cortina Roller Duo Zebra Día Y Noche 120 X 200 Cm Negro Guiza",
        "categoria": "hogar",
        "precio": 17182
    },
    {
        "id": 7,
        "nombre": "Sabana 1800 Hotel Ultra Suave Com Funda Bordada 2 Plazas Color Blanco",
        "categoria": "hogar",
        "precio": 18990
    },
    {
        "id": 8,
        "nombre": "Cubrecolchon. 2 Plazas Acolchado + 2 Fundas Para Almohada Color Blanco 100% Impermeable",
        "categoria": "hogar",
        "precio": 9990
    },
    {
        "id": 9,
        "nombre": "Velador John Natural Form",
        "categoria": "hogar",
        "precio": 119900
    },
    {
        "id": 10,
        "nombre": "Base De Cama Cambril Con Respaldo Zinus 2 Plazas 150x190x30cm Color Gris",
        "categoria": "hogar",
        "precio": 139990
    },
    {
        "id": 11,
        "nombre": "iPhone 13",
        "categoria": "tecnologia",
        "precio": 759990
    }]

class Test:
    def __init__(self):
        pass

    def create_product(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        
        new_product = {"id": self.id, "nombre": self.name, "categoria": self.category, "precio": self.price}
        
        try:
            if self.id not in catalog[self.id]["id"]:
                catalog.append(new_product)
            else:
                raise IDNotFound("A product with this ID already exists in the catalog")
        except:
            raise
        else:
            print(f"Se agregó un nuevo producto al catálogo con éxito:\nID: {self.id} \nNombre: {self.name} \nCategoría: {self.category} \nPrecio: CLP${self.price:,}")

print(catalog) 
xD = Test()

xD.create_product(2, "iPhone 500", "tecnologia", 99999)

# for i in catalog:
#     if self.id in i.values():
#         print("success")
#     else:
#         print("Not success :(")