import random

def db2html(database, filename):

    bgcolors = ['#FFCCFF','#FFFFCC','#CCFFCC','#CCFF99']

    html = '<HEAD>\n<TITLE>DINASTY Random Family Tree Generator</TITLE>\n</HEAD>\n'
    htmlfile = open(filename + '.html','w')

    html += '<TABLE WIDTH="50%>\n<TR>\n'
    html += '<TD align="center" bgcolor="BLACK">Relación de individuos</TD>\n'
    html += '</TR>\n'

    bg = random.choice(bgcolors)

    for persona in database:
        newbg = random.choice(bgcolors)
        while newbg == bg:
            newbg = random.choice(bgcolors)
        bg = newbg
        p = database[persona]
        t = '<p><b>' + p.name + ' ' + p.sur + ' (' + str(p.nac) + '-' + str(p.mue) + ')</b></p>\n'
        t += '<p>' + p.perso[0] + ', ' + p.perso[1] + ' y ' + p.perso[2] + '.</p>\n'
        t += '<p>' + p.fisico[0] + ', ' + p.fisico[1] + ' y ' + p.fisico[2] + '.</p>\n'
        html += '<TR><TD bgcolor="' + bg + '">'
        html += t
        html += '</TD>\n</TR>\n'

    html += '</TABLE>\n'

    htmlfile.write(html)
    htmlfile.close()
