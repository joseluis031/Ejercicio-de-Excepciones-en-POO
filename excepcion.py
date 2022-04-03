from Clases.correo import Correoelectronico,re


while True:
    try:
        correo = input("Introduzca su correo para poder iniciar sesion: ")
        final = Correoelectronico(correo) 
        if correo in final.correos:
                final.search1()  #aqui llamo a la funcion de la clase si el correo se encuentra en la lista
        
    except:
        pass
    else:
        if re.search("@*.*com*", correo):
            if correo not in final.correos:
                print ("Cuenta bloqueada") #si no se encuentra pero tiene "@,.y com" automaticamente se bloquea la cuenta y se cierra el programa
            break
        elif re.search("@*.*com*",correo) == None: #mientras que el correo no tenga "@,.y com", el programa seguira pidiendo un correo valido
            print("Correo invalido")