class Auto:
    #Atributos publicos
    color="Rojo"
    modelo="2010"
    marca="Vocho"
    encendido=False
    velocidad=0
    #Atributos privados
    __llave="123456"
    #Metodos publicos
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
vocho1=Auto()
#vocho1.__enciendeLuzFreno()
#print(vocho1.__llave)
vocho1.encender("123456")
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.frena()
print("Encendido=",vocho1.encendido," Velocidad=",vocho1.velocidad)
