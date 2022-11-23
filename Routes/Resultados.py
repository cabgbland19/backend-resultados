from flask import jsonify,request,Blueprint
from Controladores.ControladorResultados import ControladorResultados

miControladorResultados = ControladorResultados()
Resultados=Blueprint('Resultados',__name__)

@Resultados.route("/Resultados", methods=['GET'])
def getResultado():
    json = miControladorResultados.index()
    return jsonify(json)

@Resultados.route("/Resultados/<string:id>", methods=['GET'])
def getResultados(id):
    json = miControladorResultados.show(id)
    return jsonify(json)

@Resultados.route("/Resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['POST'])
def crearResultados(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultados.create(data,id_mesa, id_candidato)
    return jsonify(json)

@Resultados.route("/Resultados/<string:id_resultados>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['PUT'])
def modificarResultados(id_resultado ,id_mesa,infoResultado ,id_candidato):
    data = request.get_json()
    json = miControladorResultados.update(id_resultado, id_mesa,infoResultado, id_candidato)
    return jsonify(json)


@Resultados.route("/Resultados/<string:id>", methods=['DELETE'])
def eliminarResultados(id):
    json = miControladorResultados.delete(id)
    return jsonify(json)
@Resultados.route("/votos-mesa/<string:id_candidato>", methods=['GET'])
def votosMesa(id_candidato):
    json = miControladorResultados.votosPorMesa(id_candidato)
    return jsonify(json)
