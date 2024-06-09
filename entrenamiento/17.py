#1. Crear una clase Persona con atributos nombre, edad y género.

class Persona:
    def __init__(self,nombre,edad,genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def saludar(self):
        print("Mi nombre es:", self.nombre,"tengo", self.edad,"años y mi genero es", self.genero)

persona1 = Persona("Cristofer",19,"Masculino")
persona1.saludar()