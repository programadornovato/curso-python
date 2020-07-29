class Auto:
    #Atributos publicos
    encendido=False
    velocidad=0
    _alto=1.5
    _ancho=2.3
    _velocidadMaxima=100

    #Atributos privados
    #Metodos publicos
    def __init__(self,llave,color,modelo,marca):
        self.__llave=llave
        self.color=color
        self.modelo=modelo
        self.marca=marca

    def encender(self,llave):
        if self.__llave==llave:
            self.encendido=True
            print("El auto esta encendido")
        else:
            print("Humano ratero esa no es la llave")
    def acelera(self):
        if self.encendido==True:
            if self.velocidad<self._velocidadMaxima:
                self.velocidad=self.velocidad+10
    def frena(self):
        if self.velocidad>0:
            self.velocidad=self.velocidad-10
            self.__enciendeLuzFreno()
    def apaga(self):
        if self.encendido==True:
            self.encendido=False
            self.velocidad=0
            self.corneta(True)
    #Metodos privados
    def __enciendeLuzFreno(self):
        print("Luz del freno encendida")
    @staticmethod
    def corneta(precionar=False):
        if precionar==True:
            print("La corneta suena")
        else:
            print("La corneta no suena")
#Auto.corneta(True)
vocho1=Auto("1","rojo","2010","vocho")
vocho1.encender("1")
vocho1.corneta(True)
vocho1.apaga()

'''
Auto._alto=2
print(Auto._alto)
print(Auto._ancho)
print(Auto._velocidadMaxima)
vocho1=Auto("1","rojo","2010","vocho")
print(vocho1.color)
print(vocho1._alto)
'''