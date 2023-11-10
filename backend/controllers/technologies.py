import subprocess 
import json #library to convert string to json
import os

def technologies(url):
    if url:
        subprocess.call("py -m wad -u https://" + url+"> tecnologias.txt", shell=True) #execute cmd from cmd

        #tecnologias = open("tecnologias.txt")
        #tecnologias = tecnologias.read() #get the data


        #start save subdomines in an array
        tecnologias = []
        basedir = os.path.abspath(os.path.dirname(__file__))
        prop_file = os.path.join(basedir, '../tecnologias.txt')
        with open(prop_file, "r") as file:
            for i in file.readlines():
                tecnologias.append(i.split('\n'))

        #end save subdomines in an array


       
        print(tecnologias)
        
        tecnologias = tecnologias.replace(url, "data") #data/
        tecnologias = tecnologias.replace("/", "") #data
        tecnologias = json.loads(tecnologias) #convert strin to object
        tecnologias = tecnologias['data'] #save only the array

        print(tecnologias)
        return "Las tecnologias son", tecnologias
    else:
        return "Ingrese una url", []