from flask import jsonify,request,Blueprint
from Controladores.ControladorPartido import ControladorPartido

miControladorPartido = ControladorPartido()
Partido=Blueprint('Partido',__name__)

@Partido.route("/Partido", methods=['GET'])
def getPartido():
    json = miControladorPartido.index()
    return jsonify(json)


@Partido.route("/Partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)


@Partido.route("/Partido/<string:id>", methods=['GET'])
def getPartidos(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


@Partido.route("/Partido/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@Partido.route("/Partido/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)