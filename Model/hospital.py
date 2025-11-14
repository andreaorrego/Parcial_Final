from doctor import doctor

class hospital():
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
    
    @doctores.setter
    def doctores(self, valor):
        self.__doctor.append(doctor)

    def agregar_doctores(self, doctor):
        self.__doctores = doctor

    def __str__ (self):
        cadena = "Nombre del Hospital: {}".format(self.__hospital_name)
        return cadena
"""
    def buscar_dni (self, dni):
        for doc in self.__doctores:
            if doc.dni == dni:
                return doc
            return None 
        """
    
    