import socket
from datetime import datetime

def scannerPorts(ip, portStart, portEnd):
    if ip:
        portsOpen = []
        #http, SSH, https
        for port in range(portStart,portEnd):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #1: es que vamos usar ipv4, el 2 es para puertos tcp
            socket.setdefaulttimeout(1) # si no se conecta en un segundo se condisera muerto
            result = s.connect_ex((ip, port))

            if result == 0:
                portsOpen.append(format(port))

            s.close()

        msg = "la ip es: " +ip + " "+"Inicio de escaneo: "+ str(datetime.now())
        return msg, portsOpen
    else:
        return "Ingrese una ip", []