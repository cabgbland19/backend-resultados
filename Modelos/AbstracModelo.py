from abc import ABCMeta
class AbstractModelo(metaclass=ABCMeta):#ABC meta crea la clase abstracta
    def __init__(self, data):# se crea el constructor
        for llave, valor in data.items():#se recorre las llaves y los valor y se cargan en la variable data
            setattr(self, llave, valor)#reemplaza en el diccionario
