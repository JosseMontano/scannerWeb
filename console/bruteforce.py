import hashlib
import sys
import csv

def md5(palabra_encriptada, lista, user):
    for i in lista:
        cifrado = i.encode("utf-8")
        encrypted = hashlib.md5(cifrado).hexdigest()
        if palabra_encriptada == encrypted:
            #print("se encontro el hash: {}".format(i))
            print(f"Contraseña para {user}: es: " + i )


def sha256(palabra_encriptada, lista, user):
    for i in lista:
        cifrado = i.encode("utf-8")
        encrypted = hashlib.sha256(cifrado).hexdigest()
        if palabra_encriptada == encrypted:
            print(f"Contraseña para {user}: es: "+ i)


def sha512(palabra_encriptada, lista, user):
    for i in lista:
        cifrado = i.encode("utf-8")
        encrypted = hashlib.sha512(cifrado).hexdigest()
        if palabra_encriptada == encrypted:
             print(f"Contraseña para {user}: es: "+ i)


def main():
    datos = []
    with open('users.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)



    file = open("common_pass.txt", "r")
    lista = file.read().split("\n")
   



    # Iterar sobre cada fila (ignorando la primera fila que contiene los encabezados)
    for fila in datos[1:]:
    # Obtener el password de cada fila
        password = fila[2].strip()  # .strip() elimina espacios adicionales alrededor del password

        if len(password) == 32:
            md5(password, lista, fila[1])

        elif len(password) == 64:
            sha256(password, lista, fila[1])

        elif len(password) == 128:
            sha512(password, lista, fila[1])

        else:
            print("no se tiene ese metodo de hashing")

   





if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
