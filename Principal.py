from ManejadorAlumnos import ManejadorAlumnos
from Alumno import Alumno
import csv

def opcion0(lista):
    print("Adiós")

def mostrarFormato(lista):
    anio = input('Ingrese el año a mostrar: ')
    div = input('Ingrese la division a mostrar: ')
    if (anio.isdigit()) & (div != ''):
        if (div.isalpha()) & (len(div) == 1):
            lista.listarAlumnos(anio,div.upper())
        else:
            print('Division inválida.')
    else:
        print('Es inválido lo ingresado.')

def modificarInasPerm(lista):
    nuevaAsist = input('Ingrese el nuevo valor de inasistencias permitidas para los alumnos: ')
    if (nuevaAsist.isdigit()):
        Alumno.modificarInasistenciasPerm(nuevaAsist)
    else:
        print('Ese no es un valor válido.')

switcher = {
    0: opcion0,
    1: mostrarFormato,
    2: modificarInasPerm,
}

def switch(argument,listaAlumnos):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(listaAlumnos)

if __name__ == '__main__':
    archivo = open('alumnos.csv')
    reader = csv.reader(archivo, delimiter = ';')
    listaAlumnos = ManejadorAlumnos()
    for lista in reader:
        listaAlumnos.agregarAlumno(lista)
    archivo.close()

    bandera = False
    while not bandera:
        print("")
        print("0 Salir")
        print("1 Ingresar un año y división, y liste nombre y porcentaje de inasistencias de los alumnos cuya cantidad de inasistencias supera la cantidad máxima de inasistencias permitidas.")
        print("2 Modificar la cantidad máxima de inasistencias permitidas.")
        opcion= (input("Ingrese una opción: "))
        if (opcion.isdigit()):
            opcion = int(opcion)
            switch(opcion,listaAlumnos)
        else:
            print('Opcion incorrecta.')
            opcion = 1
        bandera = int(opcion)==0
