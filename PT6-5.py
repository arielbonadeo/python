def alumno_nuevo():
        nombre = input('Ingrese Nombre: ')
        apellido = input('Ingrese Apellido: ')
        fecnac = input('Ingrese Fecha de Nacimiento: ')
        dni = int(input('Ingrese Dni: '))
        nomTut = input('Ingrese Nombre del Tutor: ')
        notas = input('Ingrese Notas: ')
        faltas = int(input('Ingrese Faltas: '))
        amonestac = int(input('Ingrese Amonestaciones: '))

        variable= {
                'Nombre': nombre,
                'Apellido': apellido,
                'DNI' : dni,
                'Fec_nac': fecnac,
                'Tutor' : nomTut,
                'Notas' : notas,
                'Faltas' : faltas,
                'Amonestaciones' : amonestac
                }

        return variable


Datos = { 'Alumnos' : []}

do  = int(input('Ingrese 1 agregar alumno - 2 modificar datos - 3 expulsar alumno - 4 mostrar alumnos - 0 para salir '))

while do != 0:
    if do ==1:
        Datos['Alumnos'].append(alumno_nuevo())
        do  = int(input('Ingrese 1 agregar alumno - 2 modificar datos - 3 expulsar alumno - 4 mostrar alumnos - 0 para salir '))
    elif do ==4:
        print(Datos['Alumnos'])
        break
