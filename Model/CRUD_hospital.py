import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.hospital import Hospital
from Model.CRUD_model import CRUD_model as crud_model
from Model.CRUD import ICrud


class CRUD_hospital (ICrud):

    def create (self, **kwargs):
        nombre = kwargs.get("hospital_name")

        if not nombre:
            raise ValueError ("Debe de proporcionar un nombre")
        
        nuevo_hospital = Hospital(nombre)
        crud_model.lista_hospitales.append(nuevo_hospital)
        return nuevo_hospital
    
    def search_by (self, **kwargs):
        dni = kwargs.get ("dni")

        if dni is None:
            raise ValueError ("Debe proporcionar un DNI")
        
        for hospital in crud_model.lista_hospitales:
            for doctor in hospital.doctores:
                if doctor.dni == dni:
                    return {
                        "Hospital: ": hospital,
                        "Doctor: ": doctor,
                        "Especialidad: ": doctor.speciality
                    }
        return None

