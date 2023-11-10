import subprocess 
import json #library to convert string to json
import os


def technologies(url):
    if url:
        subprocess.call("py -m wad -u https://" + url+"> tecnologias.txt", shell=True) #execute cmd from cmd

        #tecnologias = open("tecnologias.txt")
        #tecnologias = tecnologias.read() #get the data


        #start save subdomines in an array
        tecnologias =  []
        basedir = os.path.abspath(os.path.dirname(__file__))
        prop_file = os.path.join(basedir, '../tecnologias.txt')
        with open(prop_file, "r") as file:
            
        
           for i in file.readlines():
            #cada i es una linea
            row = i.replace(" ", "")
            if(row.find("app")==1):
                #row = row.split("\n") #delete the \n
                row = row.replace('"app":',"") # ---> "PHP",\n
                row = row.replace(',\n',"") #remove this part
                row = row.replace('"',"") #remove the ""
                tecnologias.append(row)


        return "Las tecnologias son", tecnologias
    else:
        return "Ingrese una url", []