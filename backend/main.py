from flask import Flask, request, jsonify, send_file, make_response  # librerias necesarias de flask
from flask_cors import CORS  # libreria para que se conecten desde otros dispositivos
from controllers.subdominio import get_subdomines  # llamar a la funcion
from controllers.technologies import technologies
from controllers.bannerGrabing import bannerGrabing
from controllers.scannerPorts import scannerPorts
from controllers.bruteForce import bruteForce
from controllers.nmap import nmap

import csv
import os #obtener informacion de un archivo
import json       
app = Flask(__name__)

# indicar dominios permitidos
CORS(
    app,
    resources={"*": {"origins": ["http://localhost:5173", "exp://192.168.1.13:19000"]}},
)


# Ruta de prueba para el método GET
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "hello"})


# Ruta para el método 'Obtener subdominios'
@app.route("/api/subdomine/<string:domine>", methods=["GET"])
def GetSubdomines(domine):
    resFunction = get_subdomines(domine)
    msg, data = resFunction
    return jsonify({"message": msg, "data": data})


@app.route("/api/technologies/<string:url>", methods=["GET"])
def GetTechnologies(url):
    resFunction = technologies(url)
    msg, data = resFunction
    return jsonify({"message": msg, "data": data})


@app.route("/api/bannerGrabing/<string:ip>", methods=["GET"])
def BannerGrabing(ip):
    resFunction = bannerGrabing(ip)
    return jsonify({"message": resFunction})


@app.route("/api/scannerPorts", methods=["POST"])
def ScannerPorts():
    new_resource = request.get_json()
    ip = new_resource["ip"]
    portStart = new_resource["portStart"]
    portEnd = new_resource["portEnd"]

    msg, data = scannerPorts(ip, portStart, portEnd)
    return jsonify({"message": msg, "data": data})


@app.route("/api/scannerNnmap", methods=["POST"])
def ScannerNmap():
    new_resource = request.get_json()
    ip = new_resource["ip"]
    msg, nameFile = nmap(ip)
    return jsonify({"data":msg, "nameFile":nameFile}), 200
   

@app.route("/api/downloadScanner", methods=["POST"])
def DownloadScanner():
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    new_resource = request.get_json()
    nameFile = new_resource["nameFile"]

    nameFile = './' +nameFile

    prop_file = os.path.join(basedir, nameFile) 
    return send_file(prop_file)
   

@app.route("/api/bruteForce", methods=["POST"])
def BruteForce():
    datos_vector = []
    if "archivo" not in request.files:
        return jsonify({"error": "No se proporcionó ningún archivo"}), 400

    archivo = request.files["archivo"]

    if archivo.filename == "":
        return jsonify({"error": "Nombre de archivo no válido"}), 400

    if archivo and allowed_file(archivo.filename):
        # Leer el archivo CSV y almacenar los datos en el vector
        try:
            datos = leer_csv(archivo)
            datos_vector.extend(datos)

            msg = bruteForce(datos)

            return jsonify({"mensaje": msg}), 200

        except Exception as e:
            return jsonify({"error": f"Error al leer el archivo: {str(e)}"}), 500
    else:
        return jsonify({"error": "Formato de archivo no permitido"}), 400


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() == "csv"


def leer_csv(archivo):
    datos = []
    contenido = archivo.read().decode("utf-8").splitlines()

    lector_csv = csv.reader(contenido)
    for fila in lector_csv:
        datos.append(fila)

    return datos


# Correr la aplciacion
if __name__ == "__main__":
    app.run(debug=True)
