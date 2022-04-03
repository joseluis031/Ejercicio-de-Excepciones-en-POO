import re #recibe una cadena y regresa un booleano indicando si es un correo electrónico válido o no
class Correoelectronico:
    def __init__(self,correo,):
        self.correo = correo
        
    def search1(self):
        if re.search("@",self.correo):
            print("Bienvenido a la web")
        elif re.search("@",self.correo) == None:
            print("Correo invalido")



correo = input("Introduzca su correo para poder iniciar sesion: ")
final = Correoelectronico(correo)
print(final.search1())
