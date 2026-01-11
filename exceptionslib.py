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
        
