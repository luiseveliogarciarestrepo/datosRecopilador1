import requests
import os
import csv


'''Dirección web del archivo a descargar'''
direccion_url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&bom=true&format=true'

'''Uncomment para definir el Path'''

direccion_local = '/home/luise/Documents/programas/datosRecopilador/CovidColombia.csv'     # En mi Compaq
# direccion_local = '/Users/Dr.LuisEvelioRestrepoGarcia/datosRecopilador/CovidColombia.csv'    # En mi Apple


'''Obtiene la base de datos actualizada y la guardar en disco local.'''

datos_req = requests.get(direccion_url)
try:
    datos_req.raise_for_status()
except Exception as exc:
    print('Problema en la descarga: %s' % (exc))
print(datos_req.status_code == requests.codes.ok)
playFile = open('CovidColombia.csv', 'wb')
for chunk in datos_req.iter_content(100000):
    playFile.write(chunk)
playFile.close()
