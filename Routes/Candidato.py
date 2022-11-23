from flask import jsonify,request,Blueprint
from Controladores.ControladorCandidatos import ControladorCandidatos

miControladorCandidatos = ControladorCandidatos()
candidatos=Blueprint('candidatos',__name__)

@candidatos.route("/Candidatos", methods=['GET'])
def getCandidato():
    json = miControladorCandidatos.index()
    return jsonify(json)


@candidatos.route("/Candidatos", methods=['POST'])
def crearCandidatos():
    data = request.get_json()#
    json = miControladorCandidatos.create(data)
    return jsonify(json)


@candidatos.route("/Candidatos/<string:id>", methods=['GET'])
def getCandidatos(id):
    json = miControladorCandidatos.show(id)
    return jsonify(json)


@candidatos.route("/Candidatos/<string:id>", methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json = miControladorCandidatos.update(id, data)
    return jsonify(json)


@candidatos.route("/Candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidatos(id):
    json = miControladorCandidatos.delete(id)
    return jsonify(json)
@candidatos.route("/Candidatos/<string:id>/Partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id, id_partido):
    json=miControladorCandidatos.asignarPartido(id, id_partido)
    return jsonify(json)