__author__ = 'Alejandro'

import random
from datetime import datetime

from auxiliar import *
from persona import *
from listas import *
from exporter import *
from html import *


##########################
#                        #
#       PARAMETROS       #
#                        #
##########################

NMAXIND = 500
# Este es el número máximo de individuos
# El script generará individuos hasta que se alcance este valor o no quede ninguno vivo.
GAMMA = 0.9
# Este es un parámetro que afecta a la probabilidad de casarse y tener hijos.
# El valor 1 no afecta para nada.
# Valores inferiores reducen el número de personas generadas y aumentan la
# probabilidad de que la familia se extinga.
# Valores superiores lo aumentan drásticamente, y pueden suponer un gran tiempo de
# cálculo y posiblemente un uso excesivo de memoria. Usar con cuidado.
PROBESTERIL = 0.9
# Este parámetro, pese a su nombre, indica la probabilidad de que cada hijo generado
# no sea estéril, es decir, que pueda tener a su vez hijos cuando alcance la edad
# adecuada. No se aplica a hijas bastardas, en las que siempre adopta el valor 0.5
PROBMALE = 0.5
# Este parámetro controla qué proporción de hijos poseerán sexo masculino.

##########################
#                        #
#     INICIALIZACIÓN     #
#                        #
##########################

fisicos = [key for key in fisicosm2f.keys()]
persos = [key for key in persosm2f.keys()]

probmorir = {0: 0.00962, 1: 0.00182, 2: 0.00182, 3: 0.00182, 4: 0.00182, 5: 0.00115, 6: 0.00115, 7: 0.00115, 8: 0.00115, 9: 0.00115, 10: 0.0014, 11: 0.0014, 12: 0.0014, 13: 0.0014, 14: 0.0014, 15: 0.00386, 16: 0.00386, 17: 0.00386, 18: 0.00386, 19: 0.00386, 20: 0.00677, 21: 0.00677, 22: 0.00677, 23: 0.00677, 24: 0.00677, 25: 0.00808, 26: 0.00808, 27: 0.00808, 28: 0.00808, 29: 0.00808, 30: 0.00876, 31: 0.00876, 32: 0.00876, 33: 0.00876, 34: 0.00876, 35: 0.00974, 36: 0.00974, 37: 0.00974, 38: 0.00974, 39: 0.00974, 40: 0.01348, 41: 0.01348, 42: 0.01348, 43: 0.01348, 44: 0.01348, 45: 0.02111, 46: 0.02111, 47: 0.02111, 48: 0.02111, 49: 0.02111, 50: 0.0357, 51: 0.0357, 52: 0.0357, 53: 0.0357, 54: 0.0357, 55: 0.053, 56: 0.053, 57: 0.053, 58: 0.053, 59: 0.053, 60: 0.08325, 61: 0.08325, 62: 0.08325, 63: 0.08325, 64: 0.08325, 65: 0.12955, 66: 0.12955, 67: 0.12955, 68: 0.12955, 69: 0.12955, 70: 0.19654, 71: 0.19654, 72: 0.19654, 73: 0.19654, 74: 0.19654, 75: 0.30213, 76: 0.30213, 77: 0.30213, 78: 0.30213, 79: 0.30213, 80: 0.45338, 81: 0.45338, 82: 0.45338, 83: 0.45338, 84: 0.45338, 85: 0.629, 86: 0.629, 87: 0.629, 88: 0.629, 89: 0.629, 90: 0.9, 91: 0.9, 92: 0.9, 93: 0.9, 94: 0.9, 95: 0.9, 96: 0.9, 97: 0.9, 98: 0.9, 99: 0.9, 100: 1, 101: 1}
probtenerhijosfemale = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0.010928962,13:0.007285974,14:0.010928962,15:0.025500911,16:0.02003643,17:0.023679417,18:0.030965392,19:0.036429872,20:0.074681239,21:0.034608379,22:0.058287796,23:0.063752277,24:0.089253188,25:0.0856102,26:0.06557377,27:0.069216758,28:0.061930783,29:0.080145719,30:0.080145719,31:0.061930783,32:0.069216758,33:0.06010929,34:0.067395264,35:0.061930783,36:0.052823315,37:0.045537341,38:0.049180328,39:0.038251366,40:0.047358834,41:0.032786885,42:0.023679417,43:0.018214936,44:0.009107468,45:0.007285974,46:0.014571949,47:0.007285974,48:0.010928962,49:0,50:0.001821494,51:0,52:0,53:0.001821494,54:0.001821494,55:0.001821494,56:0,57:0,58:0.001821494,59:0.001821494,60:0.001821494,61:0,62:0.001821494,63:0,64:0.001821494,65:0,66:0.001821494,67:0,68:0,69:0.001821494,70:0,71:0,72:0,73:0,74:0,75:0,76:0,77:0,78:0,79:0,80:0,81:0,82:0,83:0,84:0,85:0,86:0,87:0,88:0,89:0,90:0,91:0,92:0,93:0,94:0,95:0,96:0,97:0,98:0,99:0,100:0,101:0}
probtenerhijosmale = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0.002747253,15:0.010989011,16:0.010989011,17:0.006868132,18:0.01510989,19:0.019230769,20:0.027472527,21:0.026098901,22:0.024725275,23:0.027472527,24:0.037087912,25:0.06043956,26:0.056318681,27:0.043956044,28:0.052197802,29:0.075549451,30:0.070054945,31:0.067307692,32:0.065934066,33:0.049450549,34:0.065934066,35:0.063186813,36:0.06043956,37:0.042582418,38:0.050824176,39:0.042582418,40:0.057692308,41:0.034340659,42:0.046703297,43:0.032967033,44:0.019230769,45:0.028846154,46:0.028846154,47:0.021978022,48:0.010989011,49:0.012362637,50:0.010989011,51:0.012362637,52:0.008241758,53:0.002747253,54:0,55:0.004120879,56:0.001373626,57:0.009615385,58:0.006868132,59:0.004120879,60:0.004120879,61:0.002747253,62:0.002747253,63:0,64:0.002747253,65:0.002747253,66:0.001373626,67:0,68:0,69:0,70:0.001373626,71:0,72:0.001373626,73:0,74:0,75:0,76:0,77:0,78:0.001373626,79:0,80:0,81:0,82:0,83:0,84:0,85:0.001373626,86:0,87:0,88:0,89:0,90:0,91:0,92:0,93:0,94:0,95:0,96:0,97:0,98:0,99:0,100:0,101:0}
probtenerhijos = {'M':probtenerhijosmale,'F':probtenerhijosfemale}
probtenerhijosc = {'M':{},'F':{}}
for sex in probtenerhijos:
    for age in probtenerhijos[sex]:
        if age > 50:
            probtenerhijosc[sex][age] = probtenerhijos[sex][age] * ((-0.02 * age) + 2)
        else:
            probtenerhijosc[sex][age] = probtenerhijos[sex][age] * ((-0.04 * age) + 3)
##        if age < 50:
##            probtenerhijosc[sex][age] = probtenerhijos[sex][age]
##        else:
##            probtenerhijosc[sex][age] = (probtenerhijos[sex][age] * (-0.02)) + 2

database = ''

##########################
#                        #
#         SCRIPT         #
#                        #
##########################

while (len(database) < 25):

    print('.',len(database))

    log = 'DINASTY\nGenerador de Árboles Genealógicos Aleatorios\nCreado por Alejandro López\n\n'

    database = {}
    usedids = []
    usedsurs = []
    vivos = []
    marriages = {} #dict de lists [conyuge1,conyuge2,año]
    adulterios = {} #dict de lists [conyuge1,conyuge2,año,bastardo]
    bastardos = []
    hijosdebastardos = []
    amantes = []
    usedmarriageids = []
    usednames = {'M':[],'F':[]}

    surnames = silabario('files/apellidos.txt',15)
    lugares = silabario('files/paises.txt',15)
    genericsur = ['Expósito'] * 15 + ['de ' + i for i in lugares]

    firstid = getid()
    usedids.append(firstid)
    database[firstid] = Person(getname(names['M']), random.randint(100,1750), 'M', 'personanula', 'personanula',
                   getperso(persos), getfisico(fisicos), firstid, random.choice(surnames), [getcromos(),getcromos()], True, False)
    usedsurs.append(database[firstid].sur)
    vivos.append(firstid)
    usednames['M'].append(database[firstid].name)
    firstyear = database[firstid].nac + random.randrange(15,25)
    firsttitles = gettitles(1,titulosregios,random.randrange(database[firstid].nac,firstyear-1),firstyear)
    database[firstid].titles = firsttitles

    log += 'Año inicial = ' + str(database[firstid].nac) + '\n'

    year= firstyear

    while (len(vivos) > 0) and (len(database) < NMAXIND):

        print(year,len(database),len(vivos))
        
        noconsiderar = [] # Aquí ponemos a los cónyuges de los vivos que evaluemos, para no volver a evaluarlos
        for vivo in vivos:
            if random.random() < probmorir[ageinyear(database,vivo,year)]:
                if not ((vivo == firstid) and ageinyear(database,vivo,year) < 50):
                    # Muere
                    database[vivo].mue = year
                    vivos.remove(vivo)
                    if estacasado(database,vivo):
                        for marriage in database[vivo].marriages:
                            if marriage[3] == 0:
                                marriage[3] = year
                        viudo = conyugeactual(database,vivo)
                        for conyuge in database[viudo].conyuges:
                            if conyuge[0] == vivo:
                                conyuge[2] = year
                            for marriage in database[viudo].marriages:
                                if marriage[3] == 0:
                                    marriage[3] = year
                    for conyuge in database[vivo].conyuges:
                        if conyuge[2] == 0:
                            conyuge[2] = year
                    for title in database[vivo].titles:
                        title[3] = year
                    if (len(database[vivo].titles) > 0) and (len(vivos) > 0):
                        database[vivo].titles.sort()
                        scoresycandidatos = []
                        for can in vivos:
                            if not can in hijosdebastardos:
                                s = score(database,vivo,can)
                                if s < 999999:
                                    scoresycandidatos.append([s,can])
                        if len(scoresycandidatos) == 0:
                            # Probamos con los bastardos
                            for can in vivos:
                                s = score(database,vivo,can)
                                if s < 999999:
                                    scoresycandidatos.append([s,can])
                        scoresycandidatos.sort()
                        if len(scoresycandidatos) > 0:
                            maxc = len(scoresycandidatos)
                            v = 0
                            for title in database[vivo].titles:
                                heredero = scoresycandidatos[v][1]
                                rango = title[0]
                                nombre = title[1]
                                start = year
                                end = 0
                                database[heredero].titles.append([rango,nombre,start,end])
                                database[heredero].titles.sort
                                v = nextv(v,maxc)
            else:
                if conyugeactual(database,vivo):
                    c = conyugeactual(database,vivo)
                    noconsiderar.append(c)
                if (not vivo in noconsiderar) and database[vivo].ismainfamily and (not database[vivo].esteril):
                    if not estacasado(database,vivo) and probtenerhijosc[database[vivo].sex][ageinyear(database,vivo,year)] > random.random() / GAMMA and ageinyear(database,vivo,year) > 15:
                        # Se casa
                        conyugeid = getid()
                        while conyugeid in usedids:
                            conyugeid = getid()
                        usedids.append(conyugeid)
                        noconsiderar.append(conyugeid)
                        conyugesex = 'M'
                        if database[vivo].sex == 'M':
                            conyugesex = 'F'
                        conyugeage = random.randint(15,100)
                        while probtenerhijosc[conyugesex][conyugeage] < random.random():
                            conyugeage = random.randint(15,100)
                        conyugenac = year - conyugeage
                        if (random.random() > 0.5) or (len(usednames[conyugesex]) == 0):
                            conyugename = getname(names[conyugesex])
                        else:
                            conyugename = random.choice(usednames[conyugesex])
                        if not conyugename in usednames[conyugesex]:
                            usednames[conyugesex].append(conyugename)
                        marriageid = getid()
                        while marriageid in usedmarriageids:
                            marriageid = getid()
                        marriages[marriageid] = [database[vivo].ide,conyugeid,year]
                        database[conyugeid] = Person(conyugename,conyugenac,conyugesex,'personanula','personanula',
                                                     getperso(persos),getfisico(fisicos),conyugeid,random.choice(surnames),
                                                     [getcromos(),getcromos()], False, False)
                        if not database[conyugeid].sur in usedsurs:
                            usedsurs.append(database[conyugeid].sur)
                        database[vivo].conyuges.append([conyugeid,year,0])
                        database[vivo].marriages.append(marriageid)
                        database[conyugeid].conyuges.append([vivo,year,0])
                        database[conyugeid].marriages.append(marriageid)
                        database[vivo].hijos[conyugeid] = []
                        database[conyugeid].hijos[vivo] = []
                        database[conyugeid].titles = gettitles(random.randrange(1,4),titulos,random.randrange(conyugenac,year-1),year)
                        vivos.append(conyugeid)
                    elif estacasado(database,vivo) and ((probtenerhijosc[database[vivo].sex][ageinyear(database,vivo,year)] + probtenerhijosc[database[conyugeactual(database,vivo)].sex][ageinyear(database,conyugeactual(database,vivo),year)])/ 2) > random.random() / GAMMA:
                        # Tiene un hijo
                        otropadre = conyugeactual(database,vivo)
                        hijosex = 'M'
                        if random.random() > PROBMALE:
                            hijosex = 'F'
                        hermanos = getsiblingnames(vivo,database,hijosex)
                        # Iniciamos loop de elección de nombre
                        if database[vivo].sex == hijosex:
                            pn = database[vivo].name
                        else:
                            pn = database[otropadre].name
                        posiblesnombres = [pn] + familynames2(database,vivo,hijosex) + familynames2(database,otropadre,hijosex)
                        if (random.random() > 0.25) and (len(posiblesnombres) > 0):
                            hijoname = random.choice(posiblesnombres)
                        else:
                            if random.random() > 0.5:
                                hijoname = random.choice(usednames[hijosex])
                            else:
                                hijoname = getname(names[hijosex])
                        while hijoname in hermanos:
                            # Segundo loop de elección de nombre
                            if (random.random() > 0.25) and (len(posiblesnombres) > 0):
                                hijoname = random.choice(posiblesnombres)
                            else:
                                if random.random() > 0.5:
                                    hijoname = random.choice(usednames[hijosex])
                                else:
                                    hijoname = getname(names[hijosex])
                        if not hijoname in usednames[hijosex]:
                            usednames[hijosex].append(hijoname)
                        hijoid = getid()
                        while hijoid in usedids:
                            hijoid = getid()
                        usedids.append(hijoid)
                        hijoperso = [random.choice(database[vivo].perso),random.choice(database[otropadre].perso),random.choice(persos)]
                        while hayitemsrepetidos(hijoperso):
                            hijoperso = [random.choice(database[vivo].perso),random.choice(database[otropadre].perso),random.choice(persos)]
                        hijofisico = [random.choice(database[vivo].fisico),random.choice(database[otropadre].fisico),random.choice(fisicos)]
                        while hayitemsrepetidos(hijofisico):
                            hijofisico = [random.choice(database[vivo].fisico),random.choice(database[otropadre].fisico),random.choice(fisicos)]
                        hijocromos = [random.choice(database[vivo].cromos),random.choice(database[otropadre].cromos)]
                        hijoesteril = False
                        if random.random() > PROBESTERIL:
                            hijoesteril = True
                        if database[vivo].sex == 'M':
                            hijosur = database[vivo].sur
                            database[hijoid] = Person(hijoname,year,hijosex,vivo,otropadre,hijoperso,hijofisico,
                                                      hijoid,hijosur,hijocromos,True,hijoesteril)
                        else:
                            hijosur = database[otropadre].sur
                            database[hijoid] = Person(hijoname,year,hijosex,otropadre,vivo,hijoperso,hijofisico,
                                                      hijoid,hijosur,hijocromos,True,hijoesteril)
                        vivos.append(hijoid)
                        if otropadre in database[vivo].hijos:
                            database[vivo].hijos[otropadre].append(hijoid)
                        else:
                            database[vivo].hijos[otropadre] = [hijoid]
                        if vivo in database[otropadre].hijos:
                            database[otropadre].hijos[vivo].append(hijoid)
                        else:
                            database[otropadre].hijos[vivo] = [hijoid]
                        if (vivo in hijosdebastardos) or (otropadre in hijosdebastardos):
                            hijosdebastardos.append(hijoid)
                    elif (random.random() > 0.95) and (probtenerhijosc[database[vivo].sex][ageinyear(database,vivo,year)] > random.random()) and ageinyear(database,vivo,year) > 15:
                        #Tiene una aventurilla
                        amantesex = 'F'
                        if database[vivo].sex == 'F':
                            amantesex = 'M'
                        amantename = random.choice(names[amantesex])
                        # No lo añadimos a los usados
                        amanteage = random.randint(15,100)
                        while probtenerhijosc[amantesex][amanteage] < random.random():
                            amanteage = random.randint(15,100)
                        amantenac = year - amanteage
                        amanteid = getid()
                        while amanteid in usedids:
                            amanteid = getid()
                        usedids.append(amanteid)
                        amantesur = random.choice(['(criado)','(caballerizo)','(cocinero)','(mayordomo)','(campesino)',
                                                   '(porquerizo)','(soldado)','(noble)','(sacerdote)','(amante)'])
                        if amantesex == 'F':
                            amantesur = random.choice(['(criada)','(prostituta)','(cocinera)','(institutriz)','(campesina)',
                                                       '(monja)','(amante)','(noble)'])
                        amantecromos = [getcromos(),getcromos()]
                        database[amanteid] = Person(amantename,amantenac,amantesex,'personanula','personanula',
                                                   getperso(persos),getfisico(fisicos),amanteid,amantesur,amantecromos,
                                                   False,True) # Ponemos que es estéril para que no tenga más hijos
                                                                # (suponemos que el adúltero no reincide)
                        vivos.append(amanteid)
                        amantes.append(amanteid)
                        bastardosex = 'M'
                        if random.random() > PROBMALE:
                            bastardosex = 'F'
                        if random.random() > 0.5:
                            if (database[vivo].sex == 'M') and (bastardosex == 'M'):
                                bastardoname = database[vivo].name
                            elif (database[vivo].sex == 'F') and (bastardosex == 'M') and (estacasado(database,vivo)):
                                n = database[conyugeactual(database,vivo)].name
                                if not n in getsiblingnames(vivo,database,'M'):
                                    bastardoname = n
                                else:
                                    bastardoname = random.choice(names['M'])
                            else:
                                bastardoname = random.choice(names[bastardosex])
                        else:
                            bastardoname = random.choice(names[bastardosex])
                        bastardocromos = [random.choice(database[vivo].cromos),random.choice(database[amanteid].cromos)]
                        bastardoid = getid()
                        while bastardoid in usedids:
                            bastardoid = getid()
                        bastardoperso = [random.choice(database[vivo].perso),random.choice(database[amanteid].perso),random.choice(persos)]
                        while hayitemsrepetidos(bastardoperso):
                            bastardoperso = [random.choice(database[vivo].perso),random.choice(database[amanteid].perso),random.choice(persos)]
                        bastardofisico = [random.choice(database[vivo].fisico),random.choice(database[amanteid].fisico),random.choice(fisicos)]
                        while hayitemsrepetidos(bastardofisico):
                            bastardofisico = [random.choice(database[vivo].fisico),random.choice(database[amanteid].fisico),random.choice(fisicos)]
                        bastardoesteril = False
                        if bastardosex == 'M':
                            if random.random() > PROBESTERIL:
                                bastardoesteril = True
                        else:
                            if random.random() > 0.25:
                                bastardoesteril = True
                        if database[vivo].sex == 'M':
                            if random.random() < 0.6:
                                bastardosur = database[vivo].sur
                            else:
                                bastardosur = random.choice(genericsur)
                            database[bastardoid] = Person(bastardoname,year,bastardosex,vivo,amanteid,bastardoperso,
                                                          bastardofisico,bastardoid,bastardosur,bastardocromos,True,
                                                          bastardoesteril)
                        else:
                            c = random.random()
                            if c < 0.5:
                                if conyugeactual(database,vivo):
                                    cornudo = conyugeactual(database,vivo)
                                    bastardosur = database[cornudo].sur
                                else:
                                    bastardosur = random.choice(genericsur)
                            elif c < 0.35:
                                bastardosur = random.choice(genericsur)
                            else:
                                bastardosur = amantesur.replace('(','').replace(')','').capitalize()
                            database[bastardoid] = Person(bastardoname,year,bastardosex,amanteid,vivo,bastardoperso,
                                                          bastardofisico,bastardoid,bastardosur,bastardocromos,True,
                                                          bastardoesteril)
                        bastardos.append(bastardoid)
                        hijosdebastardos.append(bastardoid)
                        adulterioid = getid()
                        while adulterioid in usedids:
                            adulterioid = getid()
                        usedids.append(adulterioid)
                        adulterios[adulterioid] = [vivo,amanteid,year,bastardoid]
                        vivos.append(bastardoid)

        year += 1


#########################
#                       #
#     POSTPROCESADO     #
#                       #
#########################

filename = datetime.today().strftime('%Y%m%d_%H%M%S') + '_'
filename += database[firstid].name + '_' + database[firstid].sur + '_' + database[firstid].ide

maxyear = year

for persona in database:
    database[persona].titles.sort()
    if database[persona].mue == 0:
        database[persona].mue = '...'

for tit in firsttitles:
    if 0 < tit[0] < 5:
        royaltitle = tit[1]
royals = [] # lista de listas [firstyear,id]
royalids = []
for persona in database:
    if len(database[persona].titles) > 0:
        for title in database[persona].titles:
            if title[1] == royaltitle:
                royals.append([title[2],persona])
                royalids.append(persona)
royals.sort()
royalnames = []
rf = open(filename + '.txt','w')
r = ''
for rey in royals:
    name = database[rey[1]].name
    royalnames.append(name)
    numero = royalnames.count(name)
    database[rey[1]].name = name + ' ' + int_to_roman(numero)
    inicio = rey[0]
    for tit in database[rey[1]].titles:
        if tit[1] == royaltitle:
            fin = tit[3]
            if inicio != tit[2]:
                print('ERROR FECHA DE INICIO')
    if fin == 0:
        fin = '...'
    r += name + ' ' + int_to_roman(numero) + ' ' + database[rey[1]].sur + ' (' + str(inicio) + '-' + str(fin) + ')\n'
rf.write(r)
rf.close()

r += '\n\nLast year = ' + str(maxyear) + '\n'
g = open(filename + '.ged','w')
ged = db2gedcom(database,marriages,adulterios,royalids)
ged += '0 LABEL \n1 POSITION -100,0 \n2 WIDTH 250 \n2 HEIGHT 200 \n'
ged += '1 TEXT ' + r + ' \n2 PADDING 10 \n'
ged += '1 DISPLAY \n2 COLOR \n3 TEXT #000000\n3 FILL #C8C8FF\n'
ged += '3 BORDER #000080\n'
g.write(ged)
g.close()

db2html(database, filename)

print(len(database))
print(len(bastardos))


a = input()
