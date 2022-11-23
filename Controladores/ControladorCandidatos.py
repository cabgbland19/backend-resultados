from Repositorio.RepositorioCandidatos import RepositorioCandidatos
from Repositorio.RepositorioPartido import RepositorioPartido
from Modelos.Candidatos import Candidatos
from Modelos.Partido import Partido


class ControladorCandidatos():
    def __init__(self):
        self.RepositorioCandidatos = RepositorioCandidatos()
        self.RepositorioPartido = RepositorioPartido()

    def index(self):
        return self.RepositorioCandidatos.findAll()

    def create(self, infoCandidato):
        if "nombre" not in infoCandidato or infoCandidato["nombre"] == "":
            return {"Error": "Ingrese nombre"}
        if "apellido" not in infoCandidato or infoCandidato["apellido"] == "":
            return {"Error": "Ingrese apellido"}
        if "cedula" not in infoCandidato or infoCandidato["cedula"] == "":
            return {"Error": "Ingrese cedula"}
        if "numero_resolucion" not in infoCandidato or infoCandidato["numero_resolucion"] == "":
            return {"Error": "Ingrese numero de resolucion"}
        for i in infoCandidato:
            if i != "nombre" and i != "apellido" and i != "cedula" and i != "numero_resolucion":
                return {"Error": "Datos extra"}
        NuevoCandidato = Candidatos(infoCandidato)
        return self.RepositorioCandidatos.save(NuevoCandidato)
    def show(self, cedula):
        Candidato = Candidatos(self.RepositorioCandidatos.findById(cedula))
        return Candidato.__dict__

    def update(self, cedula, infoCandidato):
        if "nombre" not in infoCandidato or infoCandidato["nombre"] == "":
            return {"Error": "Ingrese nombre"}
        if "apellido" not in infoCandidato or infoCandidato["apellido"] == "":
            return {"Error": "Ingrese apellido"}
        if "cedula" not in infoCandidato or infoCandidato["cedula"] == "":
            return {"Error": "Ingrese cedula"}
        if "numero_resolucion" not in infoCandidato or infoCandidato["numero_resolucion"] == "":
            return {"Error": "Ingrese numero de resolucion"}
        for i in infoCandidato:
            if i != "nombre" and i != "apellido" and i != "cedula" and i != "numero_resolucion":
                return {"Error": "Datos extra"}
        CandidatosActual = Candidatos(self.RepositorioCandidatos.findById(cedula))
        CandidatosActual.nombre = infoCandidato["nombre"]
        CandidatosActual.apellido = infoCandidato["apellido"]
        CandidatosActual.cedula = infoCandidato["cedula"]
        CandidatosActual.numero_resolucion = infoCandidato["numero_resolucion"]
        return self.RepositorioCandidatos.save(CandidatosActual)
    def delete(self, cedula):
        return self.RepositorioCandidatos.delete(cedula)

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidatos(self.RepositorioCandidatos.findById(id))
        partidoActual= Partido(self.RepositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.RepositorioCandidatos.save(candidatoActual)
