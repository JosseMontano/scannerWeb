import subprocess #Permite ejecutar comandos del sistema operativo desde un programa Python
import os #


def technologies(url):
    if url:
        subprocess.call("py -m wad -u https://" + url+"> tecnologias.txt", shell=True) #executa un comando de python

        tecnologias =  [] 
        basedir = os.path.abspath(os.path.dirname(__file__)) # Obtiene el directorio absoluto del archivo actual.
        prop_file = os.path.join(basedir, '../tecnologias.txt') # Construye la ruta completa al archivo "tecnologias.txt" utilizando el directorio base obtenido en la línea anterior.
        with open(prop_file, "r") as file: #Abre el archivo "tecnologias.txt" en modo de lectura ("r") utilizando un bloque with, que garantiza que el archivo se cierre correctamente después de su uso.
            
           for i in file.readlines():
            #cada i es una linea
            row = i.replace(" ", "") #Elimina los espacios en blanco de cada línea.
            if(row.find("app")==1):
                #row = row.split("\n") #delete the \n
                row = row.replace('"app":',"") # --->  Elimina la subcadena '"app":' de la línea.
                row = row.replace(',\n',"") #Elimina la coma y el salto de línea al final de la línea.
                row = row.replace('"',"") 
                tecnologias.append(row)

        return "Las tecnologias son", tecnologias
    else:
        return "Ingrese una url", []