import re #recibe una cadena y regresa un booleano indicando si es un correo electrónico válido o no
class Correoelectronico:
    def __init__(self,correo):
        self.correo = correo
    def search1():
        return re.search("@",correo)
    def validacion():
        search1()
        if re.search == True:
            print("hola")
        elif re.search == False:
            print("Adios")



correo = input("Introduzca su correo para poder iniciar sesion: ")
ff= Correoelectronico(correo)
print(ff.validacion())