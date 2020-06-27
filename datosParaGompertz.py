import subprocess
import os
import csv
import pyinputplus as pyip

'''Uncomment regions para definir el Path'''
direccion_local = '/home/luise/Documents/programas/datosRecopilador/CovidColombia.csv'     # En mi Compaq
# direccion_local = '/Users/Dr.LuisEvelioRestrepoGarcia/datosRecopilador/CovidColombia.csv'    # En mi Apple

# Parámetros formato de impresión

l = 25
m = 15
s = 6
j = '.'

'''Funciones'''


def ajusteFechas(row):  # Toma formato de fechas del archivo, hace la partición en 'T' y devuelve el primer índice => 2020-06-05T00:00:00:00 => 2020-06-05
    fn = row['Fecha de notificación'].partition('T')   # Fecha de notificación
    fd = row['Fecha diagnostico'].partition('T')       # Fecha de diagnóstico
    fr = row['Fecha recuperado'].partition('T')        # Fecha recuperado
    fm = row['Fecha de muerte'].partition('T')         # Fecha de muerte
    return fn[0], fd[0], fr[0], fm[0]


def archivo():  # Importa el archivo local y crea el objeto para hacerle el DictReader y crear el csv como diccionario (keys = nombre columna, Values= fila/columna)
    exampleFile = open(direccion_local)
    exampleDictReader = csv.DictReader(exampleFile)
    return exampleDictReader


def escribirArchivos(row, file, count):
    if count == 0:
        primeraLinea = ['Fecha de notificación']
        file.writerow(primeraLinea)
        linea = [fechas[0]]
        file.writerow(linea)

    else:
        linea = [fechas[0]]
        file.writerow(linea)

    print('Archivo guardado')


# Establece los valores de las Keys que serán impresas y les da el formato para impresión más amigable.
def formatoEimpresion():
    print(str(archivo().line_num).ljust(s, j), row['Ciudad de ubicación'].
          ljust(l, j), row['Departamento o Distrito '].ljust(
              l, j), row['atención'].ljust(l, j), row['Edad'].ljust(s, j),
          row['Sexo'].ljust(s, j), row['Tipo'].ljust(l, j),
          row['Estado'].ljust(l, j),  row['País de procedencia'].ljust(l, j),
          'Notificado: ', fechas[0].ljust(m, j), 'Diagnosticado: ',
          fechas[1].ljust(m, j), 'Recuperado: ', fechas[2].ljust(m, j), 'Defunción: ', fechas[3].ljust(m, j))


def variableIngresada():  # Para permitir que el usuario seleccione correctamente la ciudad, departamento, país al desplegarse listado.  Demás variables tal cual.
    variable1 = pyip.inputMenu(['Ciudad de ubicación', 'Departamento o Distrito',
                                'País de procedencia', 'Estado', 'Tipo', 'atención', 'F', 'M', 'Todas'], lettered=True)

    if variable1 == 'F' or variable1 == 'M' or variable1 == 'Todas':
        return variable1

    elif variable1 == 'Ciudad de ubicación':
        variable2 = pyip.inputMenu(ciudades, blank=True, numbered=True)
        return variable2

    elif variable1 == 'Departamento o Distrito':
        variable3 = pyip.inputMenu(departamento, blank=True, numbered=True)
        return variable3

    elif variable1 == 'Estado':
        variable3 = pyip.inputMenu(estados, blank=True, numbered=True)
        return variable3

    elif variable1 == 'Tipo':
        variable3 = pyip.inputMenu(tipos, blank=True, numbered=True)
        return variable3

    elif variable1 == 'atención':
        variable3 = pyip.inputMenu(atenciones, blank=True, numbered=True)
        return variable3

    else:

        variable4 = pyip.inputMenu(paises, blank=True, numbered=True)
        return variable4


# Construye listado de variables que están en la base de datos.  Los que empiezan por letra tildada, quedan al final.
ciudades = []
for row in archivo():
    if row['Ciudad de ubicación'] in ciudades:
        pass
    else:
        ciudades.append(row['Ciudad de ubicación'])
ciudades.sort()
# print(ciudades)

# Construye listado de Departamentos que están en la base de datos
departamento = []
for row in archivo():
    if row['Departamento o Distrito '] in departamento:
        pass
    else:
        departamento.append(row['Departamento o Distrito '])
departamento.sort()
# print(departamento)

# Construye listado de Países de procedencia que están en la base datos
paises = []
for row in archivo():
    if row['País de procedencia'] in paises:
        pass
    else:
        paises.append(row['País de procedencia'])
paises.sort()
# print(paises)
##

# Construye listado de los Estados que están en la base datos:  Asintomático, leve, moderado, grave o fallecido.
estados = []
for row in archivo():
    if row['Estado'] in estados:
        pass
    else:
        estados.append(row['Estado'])
estados.sort()
# print(estados)

# Construye listado de los Tipos que están en la base datos:  En estudio, importado o relacionado.
tipos = []
for row in archivo():
    if row['Tipo'] in tipos:
        pass
    else:
        tipos.append(row['Tipo'])
tipos.sort()
# print(tipos)

# Construye listado de la atención recibida que está en la base datos:  Casa, hospital, hospital UCI, recuperado o fallecido.
atenciones = []
for row in archivo():
    if row['atención'] in atenciones:
        pass
    else:
        atenciones.append(row['atención'])
tipos.sort()
# print(atenciones)

# Programa principal

print('''Información actualizada desde la base de datos del Instituto Nacional de Salud Colombiano.

 Elaborado por LUIS EVELIO GARCÍA RESTREPO, MD., MAS., EF.
               DANIEL GARCÍA VÁSQUEZ  Ingenieurwesen Studierende

 Variables agrupadas:

         Estados:  Asintomático, leve, moderado, grave o fallecido.
         Tipos:    En estudio, importado o relacionado.
         Atención: Casa, hospital, hospital UCI, recuperado o fallecido.

 Género:

         'F': Femenino     'M': Masculino


 Por favor seleccione la opción...escribiendo la letra o el número que la antecede, según el caso:\n\n''')

variable = variableIngresada()
cuenta = 0
print(variable)
print()
nombre_archivo = variable + 'datosGompertz' + '.csv'
archivoCsv = open(nombre_archivo, 'w', newline='')

nuevoCsv = csv.writer(archivoCsv)

if variable == 'Todas':

    for row in archivo():
        fechas = list(ajusteFechas(row))
        escribirArchivos(row, nuevoCsv, cuenta)
        formatoEimpresion()
        cuenta += 1

else:
    for row in archivo():

        if row['Ciudad de ubicación'] == variable or row['Departamento o Distrito '] == variable \
           or row['País de procedencia'] == variable or row['atención'] == variable \
           or row['Estado'] == variable or row['Tipo'] == variable or row['Sexo'] == variable:
            fechas = list(ajusteFechas(row))
            escribirArchivos(row, nuevoCsv, cuenta)
            formatoEimpresion()
            cuenta += 1

        else:
            pass

print('\n')
print('Número de casos con la variable ' + '\"' + variable + '\"' + ' es de ' + str(cuenta) + '.')

archivoCsv.close()

# Para convertir el archivo csv a libreoffice .ods
# subprocess.run(['ssconvert', variable + 'datosGompertz' + '.csv', variable + '20'+'.ods'])
subprocess.run(['ssconvert', nombre_archivo, variable + 'Gompertz' + '.ods'])
subprocess.run(['rm', nombre_archivo])
subprocess.run(['libreoffice', variable + 'Gompertz' + '.ods'])

print("Si quiere abrir el nuevo archivo en una hoja de cálculo, escriba 'SI'.  De lo contrario escriba 'NO'")
a = input()
if a == 'SI':
    subprocess.run(['libreoffice', variable + '.ods'])
else:
    print ('Ha sido un placer.  Chiao')
