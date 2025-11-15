import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.hospital import Hospital
from Model.CRUD_doctor import CRUD_doctor

class Controller:
    def __init__(self):
        self.crud_doctor = CRUD_doctor()
        self.hospitales = {} 

    def obtener_hospital(self, hospital_name):
        if hospital_name not in self.hospitales:
            self.hospitales[hospital_name] = Hospital(hospital_name)
        return self.hospitales[hospital_name]
