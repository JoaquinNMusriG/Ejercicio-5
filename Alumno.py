class Alumno:
    inasistenciasPerm = 10
    cantTotalClases = 50

    __nombreAlum = ''
    __Anio = ''
    __Division = ''
    __cantInasistencias = 0

    @classmethod
    def getCantTotClases (cls):
        return cls.cantTotalClases

    @classmethod
    def getInasistPerm (cls):
        return cls.inasistenciasPerm

    @classmethod
    def modificarInasistenciasPerm (cls, cant):
        cls.inasistenciasPerm = cant


    def __init__(self, nomb, anio, div, cantI):
        self.__nombreAlum = nomb
        self.__Anio = anio
        self.__Division = div
        self.__cantInasistencias = cantI

    def __str__(self):
        return '{:10}   {:10}   {:10}   {:<10} '.format(self.__nombreAlum,self.__Anio,self.__Division,self.__cantInasistencias)

    def getNombre(self):
        return self.__nombreAlum

    def getInasistencias(self):
        return self.__cantInasistencias

    def getAnio(self):
        return self.__Anio

    def getDivision(self):
        return self.__Division
