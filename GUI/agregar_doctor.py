import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox,
    QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy)
from PyQt6.QtGui import QFont, QColor

class Ventana_agregar_doctor (QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.inicializar_UI()

    def inicializar_UI (self):
        self.setWindowTitle ("Registrar médico")
        self.setGeometry (200, 200, 400, 350)
        paleta = self.palette ()
        paleta.setColor (self.backgroundRole(), QColor("white"))
        self.setPalette (paleta)
        self.setAutoFillBackground (True)

        layout_principal = QVBoxLayout ()
        layout_principal.setContentsMargins (30,30,30,30)
        layout_principal.setSpacing (15)

        label_titulo = QLabel ("Agregar Médico")
        label_titulo.setFont (QFont ('Arial', 16, QFont.Weight.Bold))
        label_titulo.setStyleSheet ("color: #0078d7;")
        layout_principal.addWidget (label_titulo)

        layout_principal.addSpacing (10)

        fila_doctor = QHBoxLayout ()
        label_doctor = QLabel ("Doctor:")
        label_doctor.setFont (QFont('Arial',12))
        label_doctor.setStyleSheet ("color: black;")
        self.input_doctor = QLineEdit ()
        self.input_doctor.setFont (QFont('Arial',12))
        self.input_doctor.setStyleSheet ("background-color: white; color: black;")
        fila_doctor.addWidget (label_doctor)
        fila_doctor.addWidget (self.input_doctor)
        layout_principal.addLayout (fila_doctor)

        fila_dni = QHBoxLayout ()
        label_dni = QLabel ("DNI:")
        label_dni.setFont (QFont('Arial',12))
        label_dni.setStyleSheet ("color: black;")
        self.input_dni = QLineEdit ()
        self.input_dni.setFont (QFont('Arial',12))
        self.input_dni.setStyleSheet ("background-color: white; color: black;")
        fila_dni.addWidget (label_dni)
        fila_dni.addWidget (self.input_dni)
        layout_principal.addLayout (fila_dni)

        fila_speciality = QHBoxLayout ()
        label_speciality = QLabel ("Especialidad:")
        label_speciality.setFont (QFont('Arial',12))
        label_speciality.setStyleSheet ("color: black;")
        self.combo_speciality = QComboBox ()
        self.combo_speciality.setFont (QFont('Arial',12))
        self.combo_speciality.setStyleSheet ("background-color: #d3d3d3; color: black;")
        self.combo_speciality.addItems (["Cardiología",
                                         "Pediatría",
                                         "Neurología",
                                         "Medicina Interna",
                                         "Ginecología",
                                         "Dermatología",
                                         "Anestesiología"])
        fila_speciality.addWidget (label_speciality)
        fila_speciality.addWidget (self.combo_speciality)
        layout_principal.addLayout (fila_speciality)

        fila_hospital = QHBoxLayout ()
        label_hospital = QLabel ("Hospital:")
        label_hospital.setFont (QFont('Arial',12))
        label_hospital.setStyleSheet ("color: black;")
        self.input_hospital = QLineEdit ()
        self.input_hospital.setFont (QFont('Arial',12))
        self.input_hospital.setStyleSheet ("background-color: white; color: black;")
        fila_hospital.addWidget (label_hospital)
        fila_hospital.addWidget (self.input_hospital)
        layout_principal.addLayout (fila_hospital)

        layout_principal.addSpacerItem (QSpacerItem(20,40,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding))

        crear_boton = QPushButton ("Crear médico")
        crear_boton.setFont (QFont('Arial',12))
        crear_boton.setStyleSheet ("""
            QPushButton {
                background-color: #f0f0f0; color: black;
                border: 2px solid #0078d7; border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover { background-color: #e1f0ff; }
            QPushButton:pressed { background-color: #cce0ff; }
        """)
        crear_boton.clicked.connect (self.crear_doctor)
        layout_principal.addWidget (crear_boton)

        boton_volver = QPushButton ("Volver")
        boton_volver.setFont (QFont('Arial',12))
        boton_volver.setStyleSheet ("""
            QPushButton {
                background-color: #f0f0f0; color: black;
                border: 2px solid #0078d7; border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover { background-color: #e1f0ff; }
            QPushButton:pressed { background-color: #cce0ff; }
        """)
        boton_volver.clicked.connect (self.cerrar_ventana)
        layout_principal.addWidget (boton_volver)

        self.setLayout (layout_principal)

    def crear_doctor (self):
        nombre = self.input_doctor.text().strip()
        dni = self.input_dni.text().strip()
        speciality = self.combo_speciality.currentText()
        hospital_name = self.input_hospital.text().strip()

        if not nombre or not dni or not hospital_name:
            self.mensaje_error ("¡Debe completar todos los campos!")
            return
        if not dni.isdigit():
            self.mensaje_error ("El DNI debe contener solo números")
            return

        try:
            self.controller.crud_doctor.create(
                doctor_name = nombre,
                speciality = speciality,
                dni = dni
            )

            hospital = self.controller.obtener_hospital(hospital_name)
            hospital.agregar_doctores (self.controller.crud_doctor.ultimo_creado)

            self.mensaje_bien (f"¡Médico agregado con éxito al hospital '{hospital_name}'!")
            self.limpiar_campos ()
        except Exception as e:
            self.mensaje_error (f"Error al crear médico")

    def limpiar_campos(self):
        self.input_doctor.clear()
        self.input_dni.clear()
        self.combo_speciality.setCurrentIndex(0)
        self.input_hospital.clear()

    def cerrar_ventana (self):
        self.close()

    def mensaje_bien (self,texto):
        msg = QMessageBox()
        msg.setIcon (QMessageBox.Icon.Information)
        msg.setWindowTitle ("Éxito")
        msg.setText(texto)
        msg.exec()

    def mensaje_error(self,texto):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(texto)
        msg.exec()
