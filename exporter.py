__author__ = 'Alejandro'

from listas import *
import random

def fecha(n):
    if (n == '...') or (n == 0):
        return '...'
    else:
        date = str(n)
        if len(date) == 1:
            date = '000' + date
        elif len(date) == 2:
            date = '00' + date
        elif len(date) == 3:
            date = '0' + date
        return date

def readpersos(l,d,s):
    p = ''
    if s == 'M':
        for a in l:
            p += a + '\n'
    else:
        for a in l:
            p += d[a] + '\n'
    return p[:-1]

def readcromos(persona):
    cr1 = persona.cromos[0]
    cr2 = persona.cromos[1]

    genesgruposanguineo = cr1[0] + cr2[0]
    if genesgruposanguineo == 'ii':
        grupo = '0'
    elif genesgruposanguineo in ['AA','Ai','iA']:
        grupo = 'A'
    elif genesgruposanguineo in ['BB','Bi','iB']:
        grupo = 'B'
    elif genesgruposanguineo in ['AB','BA']:
        grupo = 'AB'
    else:
        grupo = 'ERROR'
    gru = '1 BLOODTYPE ' + grupo + '\n'

    genesaltura = cr1[1:11] + cr2[1:11]
    altura = 1.78
    for gen in genesaltura:
        if gen == 'T':
            altura += 0.03
        else:
            altura -= 0.04
    altura += (random.randrange(-10,11) / 100)
    alt = '1 HEIGHT ' + str(round(altura,2)) + 'm\n'

    genespeso = cr1[11:21] + cr2[11:21]
    peso = 76
    for gen in genespeso:
        if gen == 'W':
            peso += 1
        else:
            peso -= 1.5
    peso += random.randrange(-10,11)
    pes = '1 WEIGHT ' + str(peso) + 'kg\n'

    if cr1[22] == 'N' or cr2[22] == 'N':
        pelo = random.choice(['Negro', 'Oscuro', 'Castaño', 'Pardo'])
    elif cr1[21] == 'M' or cr2[21] == 'M':
        if cr1[24] == 'P' and cr2[24] == 'P':
            pelo = 'Pelirrojo'
        else:
            pelo = 'Castaño claro'
    elif cr1[23] == 'A' and cr2[23] == 'A':
        pelo = 'Albino'
    elif cr1[24] == 'P' and cr2[24] == 'P':
        pelo = 'Pelirrojo'
    else:
        pelo = 'Rubio'
    pel = '1 HAIRCOLOR ' + pelo + '\n'

    return gru + alt + pes + pel

def readtitles(lista,s,tregios,t):
    txt = ''
    if len(lista) == 0:
        return txt
    i = 0
    if len(lista) > 5:
        lista = lista[:4]
    if s == 'F':
        i = 1
    for title in lista:
        if title[0] in tregios:
            txt += tregios[title[0]][i] + ' de ' + title[1]
        else:
            txt += t[title[0]][i] + ' de ' + title[1]
        txt += ' (' + fecha(title[2]) + '-' + fecha(title[3]) + ')\n'
    return txt[:-1]

def gedperso(persona,i,royalids):

    t = '0 @' + str(i) + '@ INDI\n'
    if persona.ide in royalids:
        t += '1 NAME ' + persona.name.upper() + '/' + persona.sur + '\n'
        t += '1 DISPLAY\n2 COLORS\n3 GENDER\n4 SYMBOL #FF0000\n4 FILL #FF6400\n'
    else:
        t += '1 NAME ' + persona.name + '/' + persona.sur + '\n'
    t += '1 SEX ' + persona.sex.lower() + '\n'
    t += '1 BIRT\n2 DATE ' + fecha(persona.nac) + '\n'
    t += '1 DEAT\n2 DATE ' + fecha(persona.mue) + '\n'
    t += '1 PERSONALITY ' + readpersos(persona.perso,persosm2f,persona.sex) + '\n'
    t += '1 FISICO ' + readpersos(persona.fisico,fisicosm2f,persona.sex) + '\n'
    t += '1 TITLES ' + readtitles(persona.titles,persona.sex,titulosregios,titulos) + '\n'
    t += 'v: ' + fecha(persona.nac) + '-' + fecha(persona.mue) + '\n'
    t += readcromos(persona)
    t += '\n'

    return t

def db2gedcom(database,marriages,adulterios,royalids):
    ged = '0 HEAD\n1 SOUR Dinasty\n2 NAME Random family tree generator\n2 VERS 2\n2 CORP A. López\n'
    ged += '1 CHAR ANSI\n1 GEDC\n2 VERS 5.5\n2 FORM LINAGE-LINKED\n'
    ged += '0 GENOMAP\n'

    i = 1
    persona2code = {}

    for persona in database:
        persona2code[database[persona].ide] = str(i)
        ged += gedperso(database[persona],i,royalids)
        i += 1

    for m in marriages:
        if database[marriages[m][0]].sex == 'M':
            marido = marriages[m][0]
            mujer = marriages[m][1]
        else:
            marido = marriages[m][1]
            mujer = marriages[m][0]
        inicio = fecha(marriages[m][2])
        if database[marido].mue == '...' or database[mujer].mue == '...':
            fin = '...'
        else:
            fin = fecha(min(database[marido].mue,database[mujer].mue))
        ged += '0 @' + str(i) + '@ FAM\n'
        ged += '1 RELATION Marriage\n'
        ged += '1 HUSB @' + persona2code[marido] + '@\n'
        ged += '1 WIFE @' + persona2code[mujer] + '@\n'
        ged += '1 DISPLAYTEXT ' + inicio + '-' + fin + '\n'
        h = []
        if len(database[marido].hijos[mujer]) > 0:
            for hijo in database[marido].hijos[mujer]:
                ged += '1 CHIL @' + persona2code[hijo] + '@\n'
                h.append(persona2code[hijo])
        ged += '0 PEDIGREELINK\n'
        ged += '1 PEDIGREELINK Parent\n'
        ged += '1 FAMILY @' + str(i) + '@\n'
        ged += '1 INDIVIDUAL @' + persona2code[marido] + '@\n'
        ged += '0 PEDIGREELINK\n'
        ged += '0 PEDIGREELINK\n'
        ged += '1 PEDIGREELINK Parent\n'
        ged += '1 FAMILY @' + str(i) + '@\n'
        ged += '1 INDIVIDUAL @' + persona2code[mujer] + '@\n'
        ged += '0 PEDIGREELINK\n'
        for code in h:
            ged += '0 PEDIGREELINK\n'
            ged += '1 PEDIGREELINK Biological\n'
            ged += '1 FAMILY @' + str(i) + '@\n'
            ged += '1 INDIVIDUAL @' + code + '@\n'
            ged += '0 PEDIGREELINK\n'

        i += 1

    for a in adulterios:
        if database[adulterios[a][0]].sex == 'M':
            marido = adulterios[a][0]
            mujer = adulterios[a][1]
        else:
            marido = adulterios[a][1]
            mujer = adulterios[a][0]
        inicio = fecha(adulterios[a][2])
        ged += '0 @' + str(i) + '@ FAM\n'
        ged += '1 RELATION LoveAffair\n'
        ged += '1 HUSB @' + persona2code[marido] + '@\n'
        ged += '1 WIFE @' + persona2code[mujer] + '@\n'
        bastardo = adulterios[a][3]
        ged += '1 DISPLAYTEXT ' + inicio + '\n'
        ged += '1 CHIL @' + persona2code[bastardo] + '@\n'
        ged += '0 PEDIGREELINK\n'
        ged += '1 PEDIGREELINK Parent\n'
        ged += '1 FAMILY @' + str(i) + '@\n'
        ged += '1 INDIVIDUAL @' + persona2code[marido] + '@\n'
        ged += '0 PEDIGREELINK\n'
        ged += '1 PEDIGREELINK Parent\n'
        ged += '1 FAMILY @' + str(i) + '@\n'
        ged += '1 INDIVIDUAL @' + persona2code[mujer] + '@\n'
        ged += '0 PEDIGREELINK\n'
        ged += '1 PEDIGREELINK Foster\n'
        ged += '1 FAMILY @' + str(i) + '@\n'
        ged += '1 INDIVIDUAL @' + persona2code[bastardo] + '@\n'
        i += 1

    ged += '0 TLRL\n'

    return ged

