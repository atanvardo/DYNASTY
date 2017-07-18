__author__ = 'Alejandro'

namesf = open('files/namesf.txt','r')
namesm = open('files/namesm.txt','r')
names = {'M':[line.strip() for line in namesm],'F':[line.strip() for line in namesf]}
namesf.close()
namesm.close()

persos = open('files/persos.txt','r')
persosm2f = {}
for line in persos:
    persosm2f[line.split(sep='\t')[0]] = line.split()[1].strip()
persos.close()

titulosregios = {1:['Emperador','Emperatriz'],2:['Rey','Reina'],
                 3:['Monarca','Monarca'],4:['Príncipe','Princesa']}

titulos = {5:['Virrey','Virreina'],6:['Archiduque','Archiduquesa'],
           7:['Duque','Duquesa'],8:['Autócrator','Autocratriz'],
           9:['Marqués','Marquesa'],10:['Conde','Condesa'],
           11:['Vizconde','Vizcondesa'],12:['Barón','Baronesa'],
           13:['Señor','Señora'],14:['Gobernador','Gobernadora'],
           15:['Hidalgo','Fijodalga']}

fisicos = open('files/fisicos.txt','r')
fisicosm2f = {}
for line in fisicos:
    fisicosm2f[line.split(sep='\t')[0]] = line.split()[1].strip()
fisicos.close()


