import requests
import pyinputplus as pyip
import csv


# Parámetros formato de impresión
l=25
m=10
s=6
j = '.'

#datos_req= requests.get('https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data')



##datos_req = requests.get('https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&bom=true&format=true')
##
##try:
##    datos_req.raise_for_status()
##except Exception as exc:
##    print('Problema en la descarga: %s' % (exc))
##
##print(datos_req.status_code == requests.codes.ok)
##
##playFile = open('CovidColombia.csv', 'wb')
##
##for chunk in datos_req.iter_content(100000):
##    playFile.write(chunk)
##
##
##playFile.close()
#Para buscar por columnas específicas.  Método de diccionario

direccion_url = '/home/luise/Documents/programas/datosRecopilador/CovidColombia.csv'
csv_file =  open(direccion_url)
exampleDictReader = csv.DictReader(csv_file)

#csv_file =  open(')
#example_reader = csv.reader(csv_file)
##for row in example_reader:
##    j = 0
##    while j < 10:
##        print('Fila ' + str(example_reader.line_num) + ' ' + str(row))
##        j+=1
##    break



## Lista de países de procedencia, departamentos y ciudades


##global ciudades
##ciudades = []
##
##csv_file =  open('/Users/Dr.LuisEvelioRestrepoGarcia/pythonExercises/BoringStuff/CovidColombia.csv')
##exampleDictReader = csv.DictReader(csv_file)
##for row in exampleDictReader:
##    if row['Ciudad de ubicación'] in ciudades:
##        pass
##    else:
##        ciudades.append(row['Ciudad de ubicación'])
##ciudades.sort()
##
##
##
##
##global departamento
##departamento= []
##csv_file =  open('/Users/Dr.LuisEvelioRestrepoGarcia/pythonExercises/BoringStuff/CovidColombia.csv')
##exampleDictReader = csv.DictReader(csv_file)
##for row in exampleDictReader:
##    if row['Departamento o Distrito '] in departamento:
##        pass
##    else:
##        departamento.append(row['Departamento o Distrito '])
##departamento.sort()
##
##
##
##global paises
##paises= []
##csv_file =  open('/Users/Dr.LuisEvelioRestrepoGarcia/pythonExercises/BoringStuff/CovidColombia.csv')
##exampleDictReader = csv.DictReader(csv_file)
##for row in exampleDictReader:
##    if row['País de procedencia'] in paises:
##        pass
##    else:
##        paises.append(row['País de procedencia'])
##paises.sort()




# Funciones

def porVariable(variable):
    print((str(exampleDictReader.line_num).ljust(s,j),row['Ciudad de ubicación'].ljust(l,j), row['atención'].ljust(l,j), row['Edad'].ljust(s,j), row['Sexo'].ljust(s,j), row['Tipo'].ljust(l,j), row['Estado'].ljust(l,j),               \
    row['País de procedencia'].ljust(l,j), 'Notificado: ', fn[0].ljust(m,j), 'Diagnosticado: ', fd[0].ljust(m,j), 'Recuperado: ', fr[0].ljust(m,j), 'Defunción: ', fm[0].ljust(m,j))


def invitacion():
    variable1 = pyip.inputMenu(['Ciudad','Departamento','País de procedencia','Casa','Asintomático','Leve','Recuperado', 'Fallecido','Importado','F','M', 'Todas'], lettered= True)
    if variable1 == 'Casa' or variable1=='Asintomático' or variable1=='Leve' or variable1=='Recuperado' or variable1=='Fallecido' or variable1=='Importado' or variable1=='F'or variable1=='M' or variable1=='Todas':
        return variable1
        

    elif variable1 == 'Ciudad':
        variable2 = pyip.inputMenu(ciudades, blank=True, numbered=True)
        return variable2
        

    elif variable1 == 'Departamento':
        variable3 = pyip.inputMenu(departamento, blank=True, numbered=True)
        return variable3
        

    else:

        variable4 = pyip.inputMenu(paises, blank=True, numbered=True)
        return variable4


##print('Variables que puede ingresar para hacer un filtro:   Ciudad, Departamento, país de procedencia, Casa, Asintomático, Leve, Recuperado, Fallecido, Importado, F (femenino), M (Masculino)')
##print()
##print()
##variable = input("Ingrese variable por la que requiere filtrar la información o escriba 'Todas' si quiere todo el consolidado:  ")


variable = invitacion()    

if variable == 'Todas':

    for row in exampleDictReader:
        fn = row['Fecha de notificación'].partition('T')   # Fecha de notificación
        fd = row['Fecha diagnostico'].partition('T')       # Fecha de diagnóstico
        fr = row['Fecha recuperado'].partition('T')        # Fecha recuperado
        fm = row['Fecha de muerte'].partition('T')         # Fecha de muerte
        paraTodas()
    

else:
    for row in exampleDictReader:
        fn = row['Fecha de notificación'].partition('T')   # Fecha de notificación
        fd = row['Fecha diagnostico'].partition('T')       # Fecha de diagnóstico
        fr = row['Fecha recuperado'].partition('T')        # Fecha recuperado
        fm = row['Fecha de muerte'].partition('T')         # Fecha de muerte
 
        if row['Ciudad de ubicación'] == variable or row['Departamento o Distrito '] == variable or row['País de procedencia'] == variable or row['atención'] == variable or row['Estado'] == variable or row['Tipo']== variable or row['Sexo']== variable:
            porVariable(variable)

        else:
            pass
