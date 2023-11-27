import sys 
import socket
from datetime import datetime

def main():
    target="199.231.166.226"
    print("-"*40)
    print("La ip es: " + target )

    print("Inicio de escaneo: "+ str(datetime.now()))
    print("-"*40)


    #http, SSH, https
    for port in range(1,81):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #1: es que vamos usar ipv4, el 2 es para puertos tcp
        socket.setdefaulttimeout(1) # si no se conecta en un segundo se condisera muerto
        result = s.connect_ex((target, port))

        if result == 0:
            print("el puerto esta abierto" + format(port))

        s.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: #finalizar con control c
        sys.exit()

        
