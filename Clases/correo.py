import re #recibe una cadena y regresa un booleano indicando si es un correo electrónico válido o no
class Correoelectronico:
    def __init__(self,correo):
        self.correo = correo
        self.correos = ["flecha@gmail.com","rodri@gmail.com","jose@gmail.com"]

        
    def search1(self):
        if re.search("@*.*com*",self.correo):
            print("Bienvenido a la web")
        
        