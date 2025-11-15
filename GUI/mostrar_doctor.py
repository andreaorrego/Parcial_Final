from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont, QPalette, QColor

class Ventana_mostrar_doctor(QWidget):
    def __init__(self, doctor, hospital_name=None):
        super().__init__()
        self.doctor = doctor
        self.hospital_name = hospital_name
        self.inicializar_UI()

    def inicializar_UI(self):
        self.setWindowTitle("Doctor encontrado")
        self.setGeometry(250, 250, 350, 200)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("white"))
        self.setPalette(paleta)
        self.setAutoFillBackground(True)

        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(10)

        label_titulo = QLabel("Información del Médico")
        label_titulo.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        label_titulo.setStyleSheet("color: #0078d7;")  
        layout.addWidget(label_titulo)

        layout.addSpacing(10)

        label_nombre = QLabel(f"Nombre: {self.doctor.doctor_name}")
        label_nombre.setFont(QFont('Arial',12))
        label_nombre.setStyleSheet("color: black;")
        layout.addWidget(label_nombre)

        label_dni = QLabel(f"DNI: {self.doctor.dni}")
        label_dni.setFont(QFont('Arial',12))
        label_dni.setStyleSheet("color: black;")
        layout.addWidget(label_dni)

        label_especialidad = QLabel(f"Especialidad: {self.doctor.speciality}")
        label_especialidad.setFont(QFont('Arial',12))
        label_especialidad.setStyleSheet("color: black;")
        layout.addWidget(label_especialidad)

        if self.hospital_name:
            label_hospital = QLabel(f"Hospital: {self.hospital_name}")
            label_hospital.setFont(QFont('Arial',12))
            label_hospital.setStyleSheet("color: black;")
            layout.addWidget(label_hospital)

        self.setLayout(layout)
