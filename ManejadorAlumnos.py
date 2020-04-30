from Alumno import Alumno

class ManejadorAlumnos:
    __listaAlumno = []

    def __init__(self):
        self.__listaAlumno =[]

    def agregarAlumno (self, alumno = []):
        if (alumno[0] != '') & (alumno[1] != '') & (alumno[2] != '') & (alumno[3].isdigit()):
            unAlumno = Alumno(alumno[0],alumno[1],alumno[2],int(alumno[3]))
            self.__listaAlumno.append(unAlumno)
        else:
            print('Error al cargar alumno')

    def mostrarLista (self):
        for lista in self.__listaAlumno:
            print(lista)

    def listarAlumnos(self, anio, division):
           inasistPerm = Alumno.getInasistPerm()
           print('Alumno       Porcentaje de Inasistencias')
           for alum in self.__listaAlumno:
               if (alum.getAnio() == anio) & (alum.getDivision() == division):
                   if (alum.getInasistencias() > int(inasistPerm)):
                       print('{:10}   {:10}%'.format(alum.getNombre(),float((alum.getInasistencias()*100)/inasistPerm)))
