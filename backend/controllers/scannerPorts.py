import socket #proporciona funciones para la creación y manipulación de sockets, necesarios para la comunicación a nivel de red.
from datetime import datetime

def scannerPorts(ip, portStart, portEnd):
    if ip:
        portsOpen = []
        #http, SSH, https
        for port in range(portStart,portEnd):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #1: es que vamos usar ipv4, el 2 es para puertos tcp
            socket.setdefaulttimeout(1) # si no se conecta en un segundo se condisera muerto
            result = s.connect_ex((ip, port)) #Intenta establecer una conexión al puerto en la dirección IP proporcionada y devuelve el código de resultado

            if result == 0:
                portsOpen.append(format(port))

            s.close() #Cierra la conexión del socket.

        msg = "la ip es: " +ip + " "+"Inicio de escaneo: "+ str(datetime.now())
        return msg, portsOpen
    else:
        return "Ingrese una ip", []