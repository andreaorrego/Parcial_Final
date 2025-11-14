class doctor():
    def __init__(self, doctor_name, speciality, dni):
        self.__doctor_name = doctor_name
        self.__speciality = speciality
        self.__dni = dni

    @property
    def doctor_name(self):
        return self.__doctor_name
    
    @doctor_name.setter
    def doctor_name(self, valor):
        if not valor:
            raise ValueError ("Debe de ingresar un nombre")
        self.__doctor_name = valor

    @property
    def speciality(self):
        return self.__speciality
    
    @speciality.setter
    def speciality(self, valor):
        if not valor:
            raise ValueError ("Debe de ingresar un nombre")
        self.__speciality = valor

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        if not isinstance(valor, int):
            raise ValueError("El dni debe ser un número entero")
        self.__dni = valor
        
    def __str__ (self):
        cadena = "Nombre del Hospital: {}".format(self.__hospital_name)
        return cadena

    
