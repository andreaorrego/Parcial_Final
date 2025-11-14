import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QPixmap

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_UI()

    def inicializar_UI(self):
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle ("Ventana2")
        self.generar_informacion()
        self.show()

    def generar_informacion(self):
        self.is_logged = False

        label_doctor = QLabel(self)
        label_doctor.setText("Doctor: ")
        label_doctor.setFont(QFont ('Arial', 10))
        label_doctor.move(20, 54)

        self.input_doctor = QLineEdit(self)
        self.input_doctor.resize (250, 24)
        self.input_doctor.move (90, 50)
        
        label_dni = QLabel(self)
        label_dni.setText("DNI: ")
        label_dni.setFont(QFont ('Arial', 10))
        label_dni.move(20, 86)

        self.input_dni = QLineEdit(self)
        self.input_dni.resize (250, 24)
        self.input_dni.move (90, 82)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())