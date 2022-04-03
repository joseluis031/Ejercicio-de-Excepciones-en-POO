# Ejercicio-de-Excepciones-en-POO
La direccion de GitHub de este repositorio es la siguiente: [GitHub](https://github.com/joseluis031/Ejercicio-de-Excepciones-en-POO.git)


## Ejercicio Excepciones
--El codigo es el siguiente:
```
import re #recibe una cadena y regresa un booleano indicando si es un correo electrónico válido o no
class Correoelectronico:
    def __init__(self,correo):
        self.correo = correo
        self.correos = ["flecha@gmail.com","rodri@gmail.com","jose@gmail.com"]

        
    def search1(self):
        if re.search("@*.*com*",self.correo):
            print("Bienvenido a la web")
```

--Código de excepciones:
```
from Clases.correo import Correoelectronico,re


while True:
    try:
        correo = input("Introduzca su correo para poder iniciar sesion: ")
        final = Correoelectronico(correo) 
        if correo in final.correos:
                final.search1() #aqui llamo a la funcion de la clase si el correo se encuentra en la lista
        
    except:
        pass
    else:
        if re.search("@*.*com*", correo):
            if correo not in final.correos:
                print ("Cuenta bloqueada") #si no se encuentra pero tiene "@,.y com" automaticamente se bloquea la cuenta y se cierra el programa
            break
        elif re.search("@*.*com*",correo) == None: #mientras que el correo no tenga "@,.y com", el programa seguira pidiendo un correo valido
            print("Correo invalido")
```
