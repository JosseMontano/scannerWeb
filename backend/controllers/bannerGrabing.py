import socket

def bannerGrabing(ip):
    if ip:
        port=21 #protocolo de transferencia de archivos
        s=socket.socket() #generar una conexion
        s.connect((ip, port))
        ver = s.recv(1024)
        ver = ver.decode('utf-8')
        return ver
    else:
        return "Ingrese una ip"