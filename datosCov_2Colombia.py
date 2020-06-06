import csv

direccion_url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&bom=true&format=true' # Dirección web del archivo
direccion_local= '/home/luise/Documents/programas/datosRecopilador/CovidColombia.csv' # Dirección local del archivo


# Parámetros formato de impresión

l=25
m=10
s=6
j = '.'

#  Quitar comentario para obtener la base de datos requerida y guardarla en disco local

##import requests
##datos_req = requests.get(direccion_url)
##try:
##    datos_req.raise_for_status()
##except Exception as exc:
##    print('Problema en la descarga: %s' % (exc))
##print(datos_req.status_code == requests.codes.ok)
##playFile = open('CovidColombia.csv', 'wb')
##for chunk in datos_req.iter_content(100000):
##    playFile.write(chunk)
##playFile.close()
  
# Funciones

def ajusteFechas(row):  # Toma formato de fechas del archivo, hace la partición en 'T' y devuelve el primer índice => 2020-06-05T00:00:00:00 => 2020-06-05
        fn = row['Fecha de notificación'].partition('T')   # Fecha de notificación
        fd = row['Fecha diagnostico'].partition('T')       # Fecha de diagnóstico
        fr = row['Fecha recuperado'].partition('T')        # Fecha recuperado
        fm = row['Fecha de muerte'].partition('T')         # Fecha de muerte
        return fn[0], fd[0], fr[0], fm[0]

def archivo(): # Importa el archivo local y crea el objeto para hacerle el DictReader y crear el csv como diccionario (keys = nombre columna, Values= fila/columna)
    exampleFile = open(direccion_local)
    exampleDictReader = csv.DictReader(exampleFile)
    return exampleDictReader

def formatoEimpresion(): #Establece los valores de las Keys que serán impresas y les da el formato para impresión más amigable.
    print(str(archivo().line_num).ljust(s,j),row['Ciudad de ubicación'].  #OJO CAMBIE exampleDictReader por llamada a archivo()
          ljust(l,j), row['atención'].ljust(l,j), row['Edad'].ljust(s,j),
          row['Sexo'].ljust(s,j), row['Tipo'].ljust(l,j),
          row['Estado'].ljust(l,j),  row['País de procedencia'].ljust(l,j),
          'Notificado: ', fechas[0].ljust(m,j), 'Diagnosticado: ',
          fechas[1].ljust(m,j),'Recuperado: ', fechas[2].ljust(m,j), 'Defunción: ', fechas[3].ljust(m,j))

#TODO
##def invitacion():
##    variable1 = pyip.inputMenu(['Ciudad de ubicación','Departamento o Distrito ','País de procedencia','Casa','Asintomático','Leve',\
##                                'Recuperado', 'Fallecido','Importado','F','M', 'Todas'], lettered= True)
##
##    if variable1 == 'Casa' or variable1=='Asintomático' or variable1=='Leve' or variable1=='Recuperado' or variable1=='Fallecido' \
##       or variable1=='Importado' or variable1=='F'or variable1=='M' or variable1=='Todas':
##        return variable1
##        
##
##    elif variable1 == 'Ciudad de ubicación':
##        variable2 = pyip.inputMenu(ciudades, blank=True, numbered=True)
##        return variable2
##        
##
##    elif variable1 == 'Departamento o Distrito ':
##        variable3 = pyip.inputMenu(departamento, blank=True, numbered=True)
##        return variable3
##        
##
##    else:
##
##        variable4 = pyip.inputMenu(paises, blank=True, numbered=True)
##        return variable4


print('''Variables que puede ingresar para hacer un filtro:   Ciudad, Departamento, país de procedencia, Casa, Asintomático,
      Leve, Recuperado, Fallecido, Importado, F (femenino), M (Masculino)\n\n''')

variable = input("Ingrese variable por la que requiere filtrar la información o escriba 'Todas' si quiere todo el consolidado:  ")

# TODO
#variable = invitacion()    
##
if variable == 'Todas':
 
    for row in archivo():
            fechas = list(ajusteFechas(row))
            formatoEimpresion()                            
##        
##        paraTodas()
##    
##
else:
    for row in archivo():
##         
        if row['Ciudad de ubicación'] == variable or row['Departamento o Distrito '] == variable \
           or row['País de procedencia'] == variable or row['atención'] == variable \
           or row['Estado'] == variable or row['Tipo']== variable or row['Sexo']== variable:
                fechas = list(ajusteFechas(row))
                formatoEimpresion()
##
        else:
            pass
##
##


'''
# Ciudades
ciudades = []
for row in archivo():
    if row['Ciudad de ubicación'] in ciudades:
        pass
    else:
        ciudades.append(row['Ciudad de ubicación'])
ciudades.sort()
#print(ciudades)

# Departamento
departamento= []
for row in archivo():
    if row['Departamento o Distrito '] in departamento:
        pass
    else:
        departamento.append(row['Departamento o Distrito '])
departamento.sort()
#print(departamento)

# Paises de procedencia
paises= []
for row in archivo():
    if row['País de procedencia'] in paises:
        pass
    else:
        paises.append(row['País de procedencia'])
paises.sort()
#print(paises)
'''
