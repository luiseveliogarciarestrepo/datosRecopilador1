# Parámetros formato de impresión

l=25
m=10
s=6
j = '.'

#  Quitar comentario para obtener la base de datos requerida
##
##import requests
##direccion_url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&bom=true&format=true'
##datos_req = requests.get(direccion_url)
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
##playFile.close()
  
#  Importar archivo csv a python

def ajusteDatos():
        fn = row['Fecha de notificación'].partition('T')   # Fecha de notificación
        fd = row['Fecha diagnostico'].partition('T')       # Fecha de diagnóstico
        fr = row['Fecha recuperado'].partition('T')        # Fecha recuperado
        fm = row['Fecha de muerte'].partition('T')         # Fecha de muerte
        return fn[0], fd[0], fr[0], fm[0]
    

import csv
exampleFile = open('/home/luise/Documents/programas/datosRecopilador/CovidColombia.csv')
exampleDictReader = csv.DictReader(exampleFile)

for row in exampleDictReader:
    #fecha = ajusteDatos()
    #fechas = list(fecha)
    fechas = list(ajusteDatos())
##    fn = row['Fecha de notificación'].partition('T')   # Fecha de notificación
##    fd = row['Fecha diagnostico'].partition('T')       # Fecha de diagnóstico
##    fr = row['Fecha recuperado'].partition('T')        # Fecha recuperado
##    fm = row['Fecha de muerte'].partition('T')         # Fecha de muerte
    print(str(exampleDictReader.line_num).ljust(s,j),row['Ciudad de ubicación'].
          ljust(l,j), row['atención'].ljust(l,j), row['Edad'].ljust(s,j),
          row['Sexo'].ljust(s,j), row['Tipo'].ljust(l,j),
          row['Estado'].ljust(l,j),  row['País de procedencia'].ljust(l,j),
          'Notificado: ', fechas[0].ljust(m,j), 'Diagnosticado: ',
          fechas[1].ljust(m,j),'Recuperado: ', fechas[2].ljust(m,j), 'Defunción: ', fechas[3].ljust(m,j))
   
