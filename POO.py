class Auto:
    #Atributos publicos
    color=""
    modelo=""
    marca=""
    encendido=False
    velocidad=0
    #Atributos privados
    __llave=""
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
            self.velocidad=self.velocidad+10
    def frena(self):
        if self.velocidad>0:
            self.velocidad=self.velocidad-10
            self.__enciendeLuzFreno()
    def apaga(self):
        if self.encendido==True:
            self.encendido=False
            self.velocidad=0
    #Metodos privados
    def __enciendeLuzFreno(self):
        print("Luz del freno encendida")
vocho1=Auto("LL123","Blanco","2010","Vocho")
vocho1.encender("LL123")
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
print("Encendido=",vocho1.encendido," Velocidad=",vocho1.velocidad," Color=",vocho1.color)

vocho2=Auto("LL111","Azul","2009","Vocho")
vocho2.encender("123")
vocho2.acelera()
vocho2.acelera()
vocho2.acelera()
print("Encendido=",vocho2.encendido," Velocidad=",vocho2.velocidad," Color=",vocho2.color)
'''
#vocho1.__enciendeLuzFreno()
#print(vocho1.__llave)
vocho1.encender("123456")
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.frena()
print("Encendido=",vocho1.encendido," Velocidad=",vocho1.velocidad)
'''