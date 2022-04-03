import re #recibe una cadena y regresa un booleano indicando si es un correo electrónico válido o no
class Correoelectronico:
    def __init__(self,correo,valido):
        self.correo = correo
        self.valido = valido
    def search1(self):
        valido = re.search("@",self.correo)
        if self.valido == True:
            print("hola")
        elif self.valido == False:
            print("Adios")    




correo = input("Introduzca su correo para poder iniciar sesion: ")
re.search("@",correo)
if re.search("@",correo):
    print("hola")
elif re.search("@",correo) == None:
    print("Adios")
