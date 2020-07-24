class Auto:
    #Atributos
    color="Rojo"
    modelo="2010"
    marca="Vocho"
    encendido=False
    velocidad=0
    #Metodos
    def encender(self):
        self.encendido=True
        print("El auto esta encendido")
    def acelera(self):
        if self.encendido==True:
            self.velocidad=self.velocidad+10
    def frena(self):
        if self.velocidad>0:
            self.velocidad=self.velocidad-10
    def apaga(self):
        if self.encendido==True:
            self.encendido=False
            self.velocidad=0

vocho1=Auto()
vocho1.acelera()
print("Encendido=",vocho1.encendido," Velocidad=",vocho1.velocidad)
vocho1.encender()
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
print("Encendido=",vocho1.encendido," Velocidad=",vocho1.velocidad)
vocho1.frena()
vocho1.frena()
vocho1.frena()
print("Encendido=",vocho1.encendido," Velocidad=",vocho1.velocidad)
vocho1.apaga()
print("Encendido=",vocho1.encendido," Velocidad=",vocho1.velocidad)



'''            
vocho1=Auto()
vocho1.color="Naranja"
print(vocho1.color,vocho1.modelo,vocho1.marca)
vocho2=Auto()
vocho2.color="Verde"
print(vocho2.color,vocho2.modelo,vocho2.marca)
beattle=Auto()
beattle.color="Gris"
beattle.marca="Beattle"
beattle.modelo="2015"
print(beattle.color,beattle.modelo,beattle.marca)
'''

