from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"Name" : nombre})

@app.route("/usuarios/<int:id>")
def usaurio_by_id(id):
    return jsonify({"id": id})

@app.route("/<path:nombre>")
def no_hacer(nombre):
    return escape(nombre)

#GET todos lo recursos
@app.route("/recurso", methods = ['GET'])
def get_recursos():
    return jsonify({"Data" : " Lista de todos los items de este recurso"})

#POST nuevo recurso
@app.route("/recurso", methods =['POST'])
def post_recurso():
    print(request.get_json())
    body = request.get_json()
    name = body["name"]
    modelo = body["modelo"]
    #Insertar en la BD
    return jsonify({"Data": {
                    "name": name,
                    "modelo": modelo
                    }})

#GET recurso a traves de su ID
@app.route("/recurso/<int:id>", methods =['GET'])
def get_recurso_by_id(id):
    #busca en la BD un registro con ese id
    return jsonify({"recurso": {
        "name": " nombre correspondiente a ese ID",
        "modelo" : " Modelo correspondiente segun ese ID"
    }})





if __name__ == '__main__': #prevencion para problemas futuros en servidores
    app.run(debug=True, port=5000)