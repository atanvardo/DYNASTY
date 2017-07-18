__author__ = 'Alejandro'

import random

def int_to_roman(num):
    """
    Obtained from http://code.activestate.com/recipes/81611-roman-numerals/
    """
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i in range(len(ints)):
       count = int(num / ints[i])
       result += nums[i] * count
       num -= ints[i] * count
    return result

def getperso(persos):
    p1 = random.choice(persos)
    p2 = random.choice(persos)
    while p1 == p2:
        p2 = random.choice(persos)
    p3 = random.choice(persos)
    while (p1 == p3) or (p2 == p3):
        p3 = random.choice(persos)
    return [p1,p2,p3]

def getfisico(fisicos):
    p1 = random.choice(fisicos)
    p2 = random.choice(fisicos)
    while p1 == p2:
        p2 = random.choice(fisicos)
    p3 = random.choice(fisicos)
    while (p1 == p3) or (p2 == p3):
        p3 = random.choice(fisicos)
    return [p1,p2,p3]

def getid():
    i = ''
    for _ in range(8):
        i += random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMaaaeeeiiiooouuuAAAEEEIIIOOOUUU111222333444555666777888999000')
    return i

def getcromos():
    cromo = ''
    # El cromosoma está compuesto por los siguientes genes:
    # - 1 gen responsable del grupo sanguíneo (A/B/i) [0]
    cromo += random.choice('ABi')
    # - 10 genes responsables de la altura (T/S) [1:11]
    for _ in range(10):
        cromo += random.choice('TS')
    # - 10 genes responsables del peso (W/L) [11:21]
    for _ in range(10):
        cromo += random.choice('WL')
    # - 4 genes responsables de color del cabello [21] [22] [23] [24]
    cromo += random.choice('NM')
    cromo += random.choice('NR')
    cromo += random.choice('NNNA')
    cromo += random.choice('NNNP')
    return cromo

def getsiblingnames(progenitor,database,hsex):
    s = []
    for cony in database[progenitor].hijos:
        for hijo in database[progenitor].hijos[cony]:
            if database[hijo].sex == hsex:
                s.append(database[hijo].name)
    return s


def hayitemsrepetidos(lista):
    leidos = []
    for item in lista:
        if item in leidos:
            return True
        leidos.append(item)
    return False

def conyugeactual(database,persona):
    for conyuge in database[persona].conyuges:
        if conyuge[2] == 0:
            return conyuge[0]
    return None

def ageinyear(database,persona,year):
    return year - database[persona].nac
        #def ageinyear(self, year):
        #if not self.estavivo(year):
        #    return 0
        #else:
        #    return year - self.nac


def estacasado(database,persona):
    if len(database[persona].conyuges) == 0:
        return False
    for conyuge in database[persona].conyuges:
        if conyuge[2] == 0:
            return True
    return False
    #def estacasado(self):
    #    if len(self.conyuges) == 0:
    #        return False
    #    for conyuge in self.conyuges:
    #        if conyuge[2] == 0:
    #            return False  #(! Error)
    #    return False

def silabario(source,n):
    f = open(source,'r')
    maxsize = 0
    silabas = []
    ultimas = []
    iniciales = []
    for line in f:
        linea = line.split()
        if len(linea) > maxsize:
            maxsize = len(linea)
    f.close()
    f = open(source,'r')
    for line in f:
        linea = line.split()
        for i in range(len(linea)):
            linea[i] = linea[i].lower()
        noultimas = linea[1:-1]
        for silaba in noultimas:
            silabas.append(silaba)
        ultimas.append(linea[-1])
        iniciales.append(linea[0])
        for _ in range(maxsize - len(linea[1:-1])):
            silabas.append('')
    f.close()
    l = []
    for _ in range(n):
        p = ''
        while p == '':
            for _ in range(maxsize-2):
                p += random.choice(silabas)
        p = random.choice(iniciales) + p
        p += random.choice(ultimas)
        p = p.replace('aa','a')
        p = p.replace('ee','e')
        p = p.replace('ii','i')
        p = p.replace('oo','o')
        p = p.replace('uu','u')
        p = p.replace('nn','n')
        p = p.replace('ss','s')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.replace('aa','a')
        p = p.capitalize()
        l.append(p)
    return l


def getname(nlist):
    n = random.choice(nlist)
    if random.random() < 0.1:
        newn = random.choice(nlist)
        while n == newn:
            newn = random.choice(nlist)
        n += ' ' + newn
    return n

def familynames(database,padre,madre,sex):
    ns = []
    if sex == 'M':
        parent = padre
        oparent = madre
    else:
        parent = madre
        oparent = padre
    while not parent == 'personanula':
        if not database[parent].name in ns:
            ns.append(database[parent].name)
        h = getsiblingnames(parent,database,sex)
        for name in h:
            if not name in ns:
                ns.append(name)
        #
        if not oparent == 'personanula':
            u = getsiblingnames(oparent,database,sex)
            for name in u:
                if not name in ns:
                    ns.append(name)
        #
        if sex == 'M':
            parent = database[parent].padre
        else:
            parent = database[parent].madre
    return ns

def familynames2(database,persona,sex):
    lista = []
    if not database[persona].padre == 'personanula':
        if sex == 'M':
            lista.append(database[database[persona].padre].name)
        else:
            lista.append(database[database[persona].madre].name)
        if database[database[persona].padre].ismainfamily:
            hermanos = getsiblingnames(database[persona].padre,database,sex)
        else:
            hermanos = getsiblingnames(database[persona].madre,database,sex)
        for i in hermanos:
            lista.append(i)
        padrenames = familynames2(database,database[persona].padre,sex)
        for i in padrenames:
            lista.append(i)
        madrenames = familynames2(database,database[persona].madre,sex)
        for i in madrenames:
            lista.append(i)
    return lista

def gettitles(n,lista,nac,year):
    t = []
    d = silabario('files/paises.txt',n)
    for i in range(n):
        rango = random.choice(list(lista.keys()))
        denominacion = d[i]
        inicio = random.randrange(nac,year)
        fin = 0
        t.append([rango,denominacion,inicio,fin])
    t.sort()
    return t


def numberofbigbrothers(database,persona):
    if database[persona].padre == 'personanula':
        # No puede tener hermanos menores si se incorpora a la familia, ya que
        # las familias de los "pegados" no se generan
        return 0
    else:
        if database[database[persona].padre].ismainfamily:
            p = database[persona].padre
        else:
            p = database[persona].madre
        if len(database[p].hijos) == 0:
            # No debería, pero se incluye por si acaso
            print('Error en numberofbigbrothers',persona)
            return 0
        count = 0
        for conyuge in database[p].hijos:
            if len(database[p].hijos[conyuge]) > 0:
                for hijo in database[p].hijos[conyuge]:
                    if (database[hijo].nac < database[persona].nac) and (database[hijo].sex == database[persona].sex):
                        count += 1
        return count


def score(database,muerto,candidato):
##    print('\n#\n',muerto,candidato)
    # Debemos evitar que cuente a aquellos que no sean familia principal.
    # Para ello les asignamos una score muy alta
    if not database[candidato].ismainfamily:
        return 999999
    # Además, si el muerto no forma parte de la familia principal (es un
    # "pegado", jamás detectará un ancestro común. Así que debemos evaluar
    # a su cónyuge
    if not database[muerto].ismainfamily:
        muerto = database[muerto].conyuges[0][0]
    # Primero hacemos la lista de ancestros del muerto:
    ancestro = muerto
    ancestrosm = [muerto]
    while not database[ancestro].padre == 'personanula':
        if database[database[ancestro].padre].ismainfamily:
            ancestro = database[ancestro].padre
        else:
            ancestro = database[ancestro].madre
        ancestrosm.append(ancestro)
    # Ahora hacemos lo mismo con el candidato
    ancestro = candidato
    ancestrosc = [candidato]
    while not database[ancestro].padre == 'personanula':
        if database[database[ancestro].padre].ismainfamily:
            ancestro = database[ancestro].padre
        else:
            ancestro = database[ancestro].madre
        ancestrosc.append(ancestro)
    # Ahora averiguamos el objetivo. Evaluamos cada ancestros del
    # candidato, y el primero que aparezca en la lista de ancestros
    # del muerto será el ancestro común objetivo
    i = 0
    a = ancestrosc[0]
    while not a in ancestrosm:
        i += 1
        a = ancestrosc[i]
    # Ahora ya tenemos al ancestro común
    # Entonces empezamos calculando el score del muerto:
##    print(a)
    scorem = 1
##    print('scorem',scorem)
    i = 0
    b = ancestrosm[i]
    while not b == a:
        scorem += 1
##        print('scorem',scorem,'[saltogen]')
        scorem += numberofbigbrothers(database,b)
##        print('scorem',scorem,'[bigbrothers]')
        if database[b].sex == 'F':
            scorem *= 2
##            print('scorem',scorem,'[mujer]')
        i += 1
        b = ancestrosm[i]
##    print('scorem',scorem,'[DEF]')
    # Y lo mismo para el candidato
    scorec = 1
##    print('scorec',scorec)
    i = 0
    b = ancestrosc[i]
    while not b == a:
        scorec += 1
##        print('scorec',scorec,'[saltogen]')
        scorec += numberofbigbrothers(database,b)
##        print('scorec',scorec,'[bigbrothers]')
        if database[b].sex == 'F':
            scorec *= 2
##            print('scorec',scorec,'[mujer]')
        i += 1
        b = ancestrosc[i]
##    print('scorec',scorec,'[DEF]')
    return scorem + scorec


def nextv(v,maximo):
    if v == maximo - 1:
        return 0
    else:
        return v + 1

