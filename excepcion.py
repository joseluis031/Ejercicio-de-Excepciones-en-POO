from Clases.correo import Correoelectronico,re
try:
    correo = input("Introduzca su correo para poder iniciar sesion: ")
    final = Correoelectronico(correo)
    print(final.search1())
except:
    pass
else:
    if re.search("@",correo) == None:
        print("Correo invalido")