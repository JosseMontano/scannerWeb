import socket #libreria para tener una conexion con el servidor

def bannerGrabing(ip):
    if ip:
        port=21 #protocolo de transferencia de archivos
        s=socket.socket() # Crea un objeto de socket y lo asigna a la variable s.
        s.connect((ip, port)) # Establece una conexión con el servidor en la dirección IP especificada y en el puerto 21.
        ver = s.recv(1024) #  Recibe hasta 1024 bytes de datos del servidor
        ver = ver.decode('utf-8') # Decodifica los datos recibidos del servidor desde formato binario a formato de cadena de caracteres utilizando UTF-8.
        return ver
    else:
        return "Ingrese una ip"