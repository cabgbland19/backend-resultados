from Repositorio.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados
from bson import ObjectId




class RepositorioResultados(InterfaceRepositorio[Resultados]):

    def getListadoResultadosMesa(self,id_candidato):
        theQuery = {"candidato.$id":ObjectId(id_candidato)}
        return self.query(theQuery)
