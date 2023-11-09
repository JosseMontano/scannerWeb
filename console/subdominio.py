#detectar subdominios

import requests #realziar consultas y peticiones a una app web
from os import path  #determinar si una ruta existe 
import argparse #agregar parametros 
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', help='Indicar el do minio de la vicitima')
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt', 'r')
            wordlist = wordlist.read().split('\n') #leer por saltos de linea (ahora es una lista)

         

            for i in wordlist:
                url = "https://"+i+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                        pass 
                else:
                    print("(+) subdominio encontrado: " + url)

    else:
         print("(+) Ingresa un dominio")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: #finalizar con control c
        sys.exit()
