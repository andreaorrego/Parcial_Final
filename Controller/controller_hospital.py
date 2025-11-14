from Model.hospital import hospital
from Model.doctor import doctor

class controller_hospital():
    def __init__ (self):
        self.__Hospital = hospital("Hospital San Jorge")

        self.Hospital.agregar_doctor (doctor ("Ana Perez", "Cardiologia", 1001))
        self.Hospital.agregar_doctor (doctor ("Luis Gomez", "Pediatria", 1002))
        self.Hospital.agregar_doctor (doctor ("Carlos Ruiz", "Neurologia", 1003))

    def search_by_dni (self, dni):
        Doctor = self.Hospital.buscar_dni (dni)
        if Doctor:
            return {
                "Doctor: ":{
                    "Nombre: ": Doctor.doctor_name,
                    "Especialidad: ": Doctor.speciality,
                    "DNI: ": Doctor.dni
                },
                "Hospital: ": {
                    "Nombre: ": self.Hospital.hospital_name
                }
            }