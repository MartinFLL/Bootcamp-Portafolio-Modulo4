import adminlib, clientlib

class User: # Base para admin y cliente
    def __init__(self, name):
        self.name = name
    
    # getter y setter de name para testear
    def get_name(self):
        return self.name
    
    def set_name(self, arg):
        self.name = arg
        
        


