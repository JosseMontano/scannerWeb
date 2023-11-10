from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers.subdominio import get_subdomines
from controllers.technologies import technologies
from controllers.bannerGrabing import bannerGrabing
from controllers.scannerPorts import scannerPorts


app = Flask(__name__)

CORS(app, resources={
     "*": {"origins": ["http://localhost:5173", "exp://192.168.1.13:19000"]}})


# Ruta para el método GET

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "hello"})


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


if __name__ == '__main__':
    app.run(debug=True)


#http://127.0.0.1:5000/api/technologies/unifranz.edu.bo