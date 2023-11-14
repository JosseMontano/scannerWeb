from flask import Flask, request, jsonify #librerias necesarias de flask
from flask_cors import CORS # libreria para que se conecten desde otros dispositivos
from controllers.subdominio import get_subdomines # llamar a la funcion 
from controllers.technologies import technologies
from controllers.bannerGrabing import bannerGrabing
from controllers.scannerPorts import scannerPorts


app = Flask(__name__)

#indicar dominios permitidos
CORS(app, resources={
     "*": {"origins": ["http://localhost:5173", "exp://192.168.1.13:19000"]}})


# Ruta de prueba para el método GET
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "hello"})

# Ruta para el método 'Obtener subdominios'
@app.route('/api/subdomine/<string:domine>', methods=['GET'])
def GetSubdomines(domine):
    resFunction =  get_subdomines(domine)
    msg, data = resFunction
    return jsonify({"message": msg, "data": data})


@app.route('/api/technologies/<string:url>', methods=['GET'])
def GetTechnologies(url):
    resFunction =  technologies(url)
    msg, data = resFunction
    return jsonify({"message": msg, "data": data})

@app.route('/api/bannerGrabing/<string:ip>', methods=['GET'])
def BannerGrabing(ip):
    resFunction =  bannerGrabing(ip)
    return jsonify({"message": resFunction})

@app.route('/api/scannerPorts', methods=['POST'])
def ScannerPorts():
    new_resource = request.get_json()
    ip = new_resource["ip"]
    portStart = new_resource["portStart"]
    portEnd = new_resource["portEnd"]
  
    msg, data =  scannerPorts(ip, portStart, portEnd)
    return jsonify({"message": msg, "data": data})

#Correr la aplciacion
if __name__ == '__main__':
    app.run(debug=True)

