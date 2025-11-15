import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtWidgets import QLabel

from agregar_doctor import Ventana_agregar_doctor
from buscar import Ventana_buscar
from Controller.controller_hospital import Controller

class Ventana_inicio (QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.inicializar_UI()

    def inicializar_UI(self):
        self.setWindowTitle("Gestión de Médicos")
        self.setGeometry(200, 200, 300, 200)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("white"))
        self.setPalette(paleta)
        self.setAutoFillBackground(True)

        layout = QVBoxLayout()
        layout.setSpacing(30)
        layout.setContentsMargins(50, 50, 50, 50)

        label_titulo = QLabel("Gestión de Médicos")
        label_titulo.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        label_titulo.setStyleSheet("color: #0078d7;") 
        layout.addWidget(label_titulo)

        layout.addSpacing(10)

        boton_agregar = QPushButton("Agregar médico")
        boton_agregar.setFont(QFont('Arial', 12))
        boton_agregar.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0; color: black;
                border: 2px solid #0078d7; border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #e1f0ff; }
            QPushButton:pressed { background-color: #cce0ff; }
        """)
        boton_agregar.clicked.connect(self.abrir_agregar)
        layout.addWidget(boton_agregar)

        boton_buscar = QPushButton("Buscar médico por DNI")
        boton_buscar.setFont(QFont('Arial', 12))
        boton_buscar.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0; color: black;
                border: 2px solid #0078d7; border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #e1f0ff; }
            QPushButton:pressed { background-color: #cce0ff; }
        """)
        boton_buscar.clicked.connect(self.abrir_buscar)
        layout.addWidget(boton_buscar)

        self.setLayout(layout)

    def abrir_agregar(self):
        self.ventana_agregar = Ventana_agregar_doctor(self.controller)
        self.ventana_agregar.show()

    def abrir_buscar(self):
        self.ventana_buscar = Ventana_buscar(self.controller)
        self.ventana_buscar.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    ventana = Ventana_inicio(controller)
    ventana.show()
    sys.exit(app.exec())