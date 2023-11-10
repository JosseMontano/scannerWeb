from flask import Flask, request, jsonify
from controllers.subdominio import get_subdomines
from controllers.technologies import technologies
from controllers.bannerGrabing import bannerGrabing
from controllers.scannerPorts import scannerPorts

app = Flask(__name__)

# Ruta para el método GET
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