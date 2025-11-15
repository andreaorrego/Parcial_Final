import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.doctor import Doctor

class Hospital():
    
    def __init__(self, hospital_name):
        self.__hospital_name = hospital_name
        self.__doctores = []

    @property
    def hospital_name(self):
        return self.__hospital_name
    
    @hospital_name.setter
    def hospital_name(self, valor):
        if not valor:
            raise ValueError ("Debe de ingresar un nombre")
        self.__hospital_name = valor
    
    @property
    def doctores(self):
        return self.__doctores

    def agregar_doctores(self, doctor):
        self.__doctores.append(doctor)

    def __str__ (self):
        return f"Hospital: {self.__hospital_name}"
        

    