class Persona:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.dni = None

    def nombre(self):
        return self._nombre
    def nombre(self, valor):
        self._nombre = valor

    def edad(self):
        return self._edad
    def edad(self, valor):
        self._edad = valor
    
    def dni(self):
        return self._dni
    def dni(self, valor):
        self._dni = valor

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
persona = Persona()
persona.nombre = input("Nombre: ")
persona.edad = int(input("Edad: "))
persona.dni = int(input("DNI: "))

print(persona.mostrar_datos())
print("Mayor de edad: ", persona.es_mayor_de_edad())