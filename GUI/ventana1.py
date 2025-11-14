import sys
from PyQt6.QtWidgets import QApplication, QWidget

class Ventana1(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_UI()

    
    def inicializar_UI(self):
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle("Ventana1")
        self.show()

if __name__ == '__main__':
    app = QApplication (sys.argv)
    ventana = Ventana1()
    sys.exit (app.exec())