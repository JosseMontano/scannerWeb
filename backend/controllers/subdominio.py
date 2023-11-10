import requests #realziar consultas y peticiones a una app web
import os


def get_subdomines(domine):
    if domine:
        #start save subdomines in an array
        subdomines = []
        basedir = os.path.abspath(os.path.dirname(__file__))
        prop_file = os.path.join(basedir, 'static/subdominios.txt')
        with open(prop_file, "r") as file:
            for line in file.readlines():
                subdomines.append(line.split('\n'))

      
        datos_limpios = [elemento[0].strip() for elemento in subdomines]
        #end save subdomines in an array

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
