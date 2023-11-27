import hashlib
import os #obtener informacion de un archivo

def md5(palabra_encriptada, lista, user):
    listaPasswordFound = []
    for i in lista:
        cifrado = i.encode("utf-8")
        encrypted = hashlib.md5(cifrado).hexdigest()
        if palabra_encriptada == encrypted:
            listaPasswordFound.append("Contraseña para " + user +" es: " + i )
    
    return listaPasswordFound


def sha256(palabra_encriptada, lista, user):
    listaPasswordFound = []
    for i in lista:
        cifrado = i.encode("utf-8")
        encrypted = hashlib.sha256(cifrado).hexdigest()
        if palabra_encriptada == encrypted:
            print("Contraseña para " + user +": es: " + i )
            listaPasswordFound.append("Contraseña para " + user +": es: " + i )



    return listaPasswordFound


def sha512(palabra_encriptada, lista, user):
    listaPasswordFound = []
    for i in lista:
        cifrado = i.encode("utf-8")
        encrypted = hashlib.sha512(cifrado).hexdigest()
        if palabra_encriptada == encrypted:
            print("Contraseña para " + user +": es: " + i )
            listaPasswordFound.append("Contraseña para " + user +": es: " + i )



    return listaPasswordFound



def bruteForce(datos):

    lista =  []

    basedir = os.path.abspath(os.path.dirname(__file__)) # Obtiene el directorio absoluto del archivo actual.
    prop_file = os.path.join(basedir, 'static/common_pass.txt') # Construye la ruta completa al archivo "subdominios.txt" utilizando el directorio base obtenido en la línea anterior.
    file = open(prop_file, "r")
    lista = file.read().split("\n")


    msgReturn = []

    # Iterar sobre cada fila (ignorando la primera fila que contiene los encabezados)
    for fila in datos[1:]:
    # Obtener el password de cada fila
        password = fila[2].strip()  # .strip() elimina espacios adicionales alrededor del password
        if len(password) == 32:
            msg = md5(password, lista, fila[1])
            if(msg != []):
                msgReturn.append(msg)
            
    
        elif len(password) == 64:
            msg = sha256(password, lista, fila[1])
            if(msg != []):
                msgReturn.append(msg)

        elif len(password) == 128:
            msg =  sha512(password, lista, fila[1])
            if(msg != []):
                msgReturn.append(msg)


        else:
            msgReturn.append("no se tiene ese metodo de hashing")


    return msgReturn

   

