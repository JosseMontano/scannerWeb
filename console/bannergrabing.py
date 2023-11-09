import socket
import sys
import argparse

#start get the data
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='indicar la ip de la victima')
parser = parser.parse_args()
#end get the data

def banner(ip, port):
    s=socket.socket() #generar una conexion
    s.connect((ip, port))
    print(s.recv(1024))

def main():
    if parser.target:
        ip=parser.target
        port=21 #protocolo de transferencia de archivos
        banner(ip, port)
    else:
        print("(-) Inresa una ip")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: #finalizar con control c
        sys.exit()

        
