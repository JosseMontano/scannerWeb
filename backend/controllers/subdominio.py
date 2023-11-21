import requests #realizar consultas y peticiones a una app web
import os #obtener informacion de un archivo

def get_subdomines(domine):
    if domine:
        #guardar los subdominios en un array
        subdomines = []
        basedir = os.path.abspath(os.path.dirname(__file__)) # Obtiene el directorio absoluto del archivo actual.
        prop_file = os.path.join(basedir, 'static/subdominios.txt') # Construye la ruta completa al archivo "subdominios.txt" utilizando el directorio base obtenido en la línea anterior.
        with open(prop_file, "r") as file:
            for line in file.readlines():
                subdomines.append(line.split('\n'))

        #limpiar la cadena de texto para que este de forma entendible
        datos_limpios = [elemento[0].strip() for elemento in subdomines]

        #guardar en el vector urlList las urls que si existan
        urlList = []
        for i in datos_limpios:
            url = "https://"+i+"."+domine
            try:
                requests.get(url)
            except requests.ConnectionError:
                    pass 
            else:
                urlList.append(url)
            
    return "datos encontrados", urlList
