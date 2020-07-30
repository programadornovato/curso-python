class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
class Estudiante(Persona):
    def __init__(self,nombre,edad,clave,calificacion):
        Persona.__init__(self,nombre,edad)
        self.clave=clave
        self.calificacion=calificacion

juan=Persona("Juan",22)
print("juan.edad",juan.edad)
maria=Estudiante("Maria",23,"2222",10)
print("maria clave",maria.clave)