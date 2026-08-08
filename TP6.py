# # a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
# # Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
# # notas, cantidad de faltas, cantidad de amonestaciones recibidas.
# # Recomendación: Para llevar un registro de estos dato se puede
# # utilizar un diccionario estructurado de la siguiente manera:

# # Donde cada alumno es otro diccionario estructurado de la
# # siguiente forma:

alumno1= {
        'Nombre': 'Ariel',
        'Apellido' : 'Bonadeo',
        'DNI' : 31081087,
        'Fec_nac': '24/07/1984',
        'Tutor' : 'Mama',
        'Notas' : [8,8,7,8]
        }
alumno2= {
        'Nombre': 'juan',
        'Apellido' : 'perez',
        'DNI' : 30123456,
        'Fec_nac': '1/07/1984',
        'Tutor' : 'Papa',
        'Notas' : [4,3,6,8]
        }
alumno3= {
        'Nombre': 'jose',
        'Apellido' : 'diaz',
        'DNI' : 30987654,
        'Fec_nac': '2/07/1984',
        'Tutor' : 'Tia',
        'Notas' : [2,5,6,4]
        }

# # En esta estructura:

Datos = { 'Alumnos' : [alumno1,alumno2,alumno3 ]}

# Para acceder por ejemplo al numero de DNI del tercer alumno
# Datos['Alumnos'][2]['DNI']

# print(Datos['Alumnos'][2]['DNI'])
      
# # b) Mostrar los datos de cada alumno
print('alumno1: ')
print(Datos['Alumnos'][0])

print('alumno2: ')
print(Datos['Alumnos'][1])

print('alumno3: ')
print(Datos['Alumnos'][2])

# # c) Modificar los datos de los alumnos

Datos['Alumnos'][1]['Tutor'] = 'Madre y Padre'

print('alumno2: ')
print(Datos['Alumnos'][1])

Datos['Alumnos'][2]['Notas'] = [4,3,7,8]

print('alumno3: ')
print(Datos['Alumnos'][2])

# # d) Agregar alumnos

alumno4= {
            'Nombre': 'maria',
            'Apellido' : 'magdalena',
            'DNI' : 100000000,
            'Fec_nac': '01/01/1900',
            'Tutor' : 'dios',
            'Notas' : [10]
            }
Datos['Alumnos'].append(alumno4)

alumno5= {
            'Nombre': 'ana',
            'Apellido' : 'bolena',
            'DNI' : 200000000,
            'Fec_nac': '01/01/1700',
            'Tutor' : 'mama',
            'Notas' : [10,9,8,7]
            }
Datos['Alumnos'].append(alumno5)

print(Datos['Alumnos'])

# # e) Expulsar alumnos

dni = int(input('Ingrese Dni para explusar: '))
cont=0
for i in Datos['Alumnos']:
    # print(Datos['Alumnos'][cont]['DNI'])
    # cont = cont+1
    if Datos['Alumnos'][cont]['DNI'] == dni :
        # print(Datos['Alumnos'][cont])
        Datos['Alumnos'][cont].pop
    cont = cont+1

print(Datos['Alumnos'])
