from Repositorio.RepositorioCandidatos import RepositorioCandidatos
from Repositorio.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
from Modelos.Candidatos import Candidatos
from flask import Response


class ControladorMesa():
    def __init__(self):
        self.RepositorioCandidatos = RepositorioCandidatos()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        for x in infoMesa:
            if x == "numero" or x == "cantidad_inscritos" :
                pass
            else:
                return {"msg":"Hay campos no permitidos"}
        try:
            if infoMesa["numero"]==True and infoMesa["cantidad_inscritos"]==True:
                pass
        except:
            return {"msg":"Faltan datos por llenar"}
        #info={"numero":0,"cantidad_inscritos":"0"}
        nuevaMesa = Mesa(infoMesa)
        #nuevaMesa.numero = infoMesa["numero"]
        #nuevaMesa.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        mesa = Mesa(self.repositorioMesa.findById(id))
        return mesa.__dict__

    def update(self, id, infoMesa):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActual)
    #def asignarcandidato(self, id, id_candidato,data):
     #   mesaActual = Mesa(self.repositorioMesa.findById(id))
     #   candidatoActual = Candidatos(self.RepositorioCandidatos.findById(id_candidato))
      #  mesaActual.candidato = candidatoActual
       # return self.repositorioMesa.save(mesaActual)
    def delete(self, id):
        return self.repositorioMesa.delete(id)

