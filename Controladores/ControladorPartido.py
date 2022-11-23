from Repositorio.RepositorioPartido import RepositorioPartido
from Repositorio.RepositorioCandidatos import RepositorioCandidatos
from Modelos.Partido import Partido
from Modelos.Candidatos import Candidatos


class ControladorPartido():
    def __init__(self):
        self.RepositorioPartido = RepositorioPartido()
        self.RepositorioCandidatos = RepositorioCandidatos()
    def index(self):
        return self.RepositorioPartido.findAll()

    def create(self, infoPartido):
        if "nombre" not in infoPartido or infoPartido["nombre"] == "":
            return {"Error": "Ingrese nombre"}
        if "lema" not in infoPartido or infoPartido["lema"] == "":
            return {"Error": "Ingrese lema"}
        for i in infoPartido:
            if i != "nombre" and i !="lema":
                return {"Error": "Datos extra"}
        NuevoPartido = Partido(infoPartido)
        return self.RepositorioPartido.save(NuevoPartido)

    def show(self, id):
        partido = Partido(self.RepositorioPartido.findById(id))
        return partido.__dict__

    def update(self, id, infoPartido):
        if "nombre" not in infoPartido or infoPartido["nombre"] == "":
            return {"Error": "Ingrese nombre"}
        if "lema" not in infoPartido or infoPartido["lema"] == "":
            return {"Error": "Ingrese lema"}
        for i in infoPartido:
            if i != "nombre" and i !="lema":
                return {"Error": "Datos extra"}
        PartidoActual = Partido(self.RepositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.RepositorioPartido.save(PartidoActual)

    def delete(self, id):
        candidato = self.RepositorioCandidatos.findAll()
        lista =[]
        for i in candidato:
            for x, y in i.items():
                if x == "partido":
                    lista.append(y)
        for a in lista:
            for b, c in a.items():
                if c == id:
                    return {"msg": "Existen candidatos en el partido"}
        return self.RepositorioPartido.delete(id)
