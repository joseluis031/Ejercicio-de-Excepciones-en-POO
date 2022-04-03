import re
class Correoelectronico:
    def __init__(self,correo):
        self.correo = correo
    def search(self):
        return re.search(". * @. * \ .. *", tu_correo)
    
    
tu_correo = input("Introduzca su correo para poder iniciar sesion: ")