import re #recibe una cadena y regresa un booleano indicando si es un correo electrónico válido o no
class Correoelectronico:
    def __init__(self,correo,):
        self.correo = correo
        
    def search1(self):
        if re.search("@",self.correo):
            print("Bienvenido a la web")
