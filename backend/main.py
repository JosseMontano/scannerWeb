from flask import Flask, request, jsonify
from controllers.subdominio import get_subdomines
from controllers.technologies import technologies

app = Flask(__name__)

# Datos de ejemplo (podrías usar una base de datos en lugar de esto)
data = [
    {
        "a":"xd",
    },{
        "a":"xd2"
    }
]

# Ruta para el método GET
@app.route('/api/subdomine/<string:domine>', methods=['GET'])
def getSubdomines(domine):
    resFunction =  get_subdomines(domine)
    msg, data = resFunction
    return jsonify({"message": msg, "data": data})


@app.route('/api/technologies/<string:url>', methods=['GET'])
def get_technologies(url):
    resFunction =  technologies(url)
    msg, data = resFunction
    return jsonify({"message": msg, "data": data})

# Ruta para el método POST
@app.route('/api/resource', methods=['POST'])
def add_resource():
    new_resource = request.get_json()
    data.append(new_resource)
    return jsonify({"message": "Recurso agregado con éxito"})

if __name__ == '__main__':
    app.run(debug=True)


#http://127.0.0.1:5000/api/technologies/unifranz.edu.bo