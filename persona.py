__author__ = 'Alejandro'

class Person:
    def __init__(self, nombre, nacyear, sexo, padre, madre, perso, fisico, ide, sur, cromos, ismainfamily, esteril):
        self.name = nombre # str
        self.nac = nacyear # int
        self.sex = sexo # str 'm'/'f'
        self.ide = ide # str
        self.sur = sur # str
        self.cromos = cromos # Lista de str ['cr1','cr2']
        if padre == 'personanula':
            self.padre = 'personanula' # str
        else:
            self.padre = padre # str
        if madre == 'personanula':
            self.madre = 'personanula' # str
        else:
            self.madre = madre # str
        self.mue = 0 # int (None antes de asignarlo)
        self.hijos = {} # Diccionario de conyuge:[hijo1,hijo2...]
        self.perso = perso # Lista de str ['atributo1,atributo2,atributo3']
        self.fisico = fisico # Lista de str ['atributo1,atributo2,atributo3']
        self.conyuges = [] # Lista de listas [id, añomatrimonio, añoviudez]
        self.titles = [] # Lista de listas:[rango,nombre,start,end]
        self.mote = '' # str
        self.causamuerte = ''
        self.marriages = []
        self.ismainfamily = ismainfamily
        self.esteril = esteril

    def __str__(self):
        s = self.ide + '\n'
        s += self.name + ' ' + self.sur + ' (' + str(self.nac) + '-' + str(self.mue) + ')\n'
        s += self.perso[0] + ', ' + self.perso[1] + ' y ' + self.perso[2] + '\n'
        s += self.fisico[0] + ', ' + self.fisico[1] + ' y ' + self.fisico[2] + '\n'
        s += 'Nº de cónyuges: ' + str(len(self.conyuges)) + '\n'
        return s


