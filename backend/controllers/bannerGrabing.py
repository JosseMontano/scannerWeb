import socket


def bannerGrabing(ip):
    if ip:
        port=21 #protocolo de transferencia de archivos
        s=socket.socket() #generar una conexion
        s.connect((ip, port))
        print(s.recv(1024))
    else:
        return "Ingrese una ip", ''