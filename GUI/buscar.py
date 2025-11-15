import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QMessageBox,
    QVBoxLayout, QHBoxLayout
)
from PyQt6.QtGui import QFont, QPalette, QColor
from mostrar_doctor import Ventana_mostrar_doctor

class Ventana_buscar (QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.inicializar_UI()

    def inicializar_UI(self):
        self.setWindowTitle("Buscar médico por DNI")
        self.setGeometry(200,200,400,180)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window,QColor("white"))
        self.setPalette(paleta)
        self.setAutoFillBackground(True)

        layout = QVBoxLayout()
        layout.setContentsMargins(30,30,30,30)
        layout.setSpacing(20)

        label_titulo = QLabel("Buscar Médico")
        label_titulo.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        label_titulo.setStyleSheet("color: #0078d7;") 
        layout.addWidget(label_titulo)

        layout.addSpacing(10)

        fila_dni = QHBoxLayout()
        label_dni = QLabel("DNI:")
        label_dni.setFont(QFont('Arial',12))
        label_dni.setStyleSheet("color: black;")
        self.input_dni = QLineEdit()
        self.input_dni.setFont(QFont('Arial',12))
        self.input_dni.setStyleSheet("background-color: white; color: black;")
        fila_dni.addWidget(label_dni)
        fila_dni.addWidget(self.input_dni)
        layout.addLayout(fila_dni)

        boton_buscar = QPushButton("Buscar")
        boton_buscar.setFont(QFont('Arial',12))
        boton_buscar.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0; color: black;
                border: 2px solid #0078d7; border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover { background-color: #e1f0ff; }
            QPushButton:pressed { background-color: #cce0ff; }
        """)
        boton_buscar.clicked.connect(self.buscar_doctor)
        layout.addWidget(boton_buscar)

        boton_volver = QPushButton("Volver")
        boton_volver.setFont(QFont('Arial',12))
        boton_volver.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0; color: black;
                border: 2px solid #0078d7; border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover { background-color: #e1f0ff; }
            QPushButton:pressed { background-color: #cce0ff; }
        """)
        boton_volver.clicked.connect(self.cerrar_ventana)
        layout.addWidget(boton_volver)

        self.setLayout(layout)

    def buscar_doctor(self):
        dni = self.input_dni.text().strip()
        if not dni:
            self.mensaje_error("¡Ingrese el DNI para buscar!")
            return

        doctor = self.controller.crud_doctor.buscar_por_dni(dni)
        if doctor:
            hospital_name = None
            for h_name, h in self.controller.hospitales.items():
                if doctor in h.doctores:
                    hospital_name = h_name
                    break
            self.ventana_mostrar = Ventana_mostrar_doctor(doctor, hospital_name)
            self.ventana_mostrar.show()
        else:
            self.mensaje_error("¡No se encontró ningún médico con ese DNI!")

    def cerrar_ventana(self):
        self.close()

    def mensaje_error(self,texto):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(texto)
        msg.exec()
