import subprocess 
import argparse
import sys
import json #library to convert string to json

#start get the data
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='indicar la url')
parser = parser.parse_args()
#end get the data

def main():
    if parser.target:
        
        subprocess.call("py -m wad -u " + parser.target+"> tecnologias.txt", shell=True) #execute cmd from cmd

        tecnologias = open("tecnologias.txt")
        tecnologias = tecnologias.read() #get the data
   
        
        tecnologias = tecnologias.replace(parser.target, "data") #data/
        tecnologias = tecnologias.replace("/", "") #data
        tecnologias = json.loads(tecnologias) #convert strin to object
        tecnologias = tecnologias['data'] #save only the array

        print(tecnologias)
    else:
        print("(-) Ingresa una URL")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: #finalizar con control c
        sys.exit()
