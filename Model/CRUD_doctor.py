import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.doctor import Doctor
from Model.CRUD import ICrud
from Model.CRUD_model import CRUD_model

class CRUD_doctor:

    def __init__(self):
        self.ultimo_creado = None

    def create(self, **kwargs):
        nombre_doctor = kwargs.get("doctor_name")
        especialidad = kwargs.get("speciality")
        documento = kwargs.get("dni")

        if not nombre_doctor or not especialidad or not documento:
            raise ValueError("Debe proporcionar la información completa")

        if not documento.isdigit():
            raise ValueError("El DNI debe contener solo números")

        nuevo_doctor = Doctor(nombre_doctor, especialidad, documento)
        CRUD_model.lista_doctores.append(nuevo_doctor)
        self.ultimo_creado = nuevo_doctor

    def buscar_por_dni(self, dni):
        for doctor in CRUD_model.lista_doctores:
            if doctor.dni == dni:
                return doctor
        return None
