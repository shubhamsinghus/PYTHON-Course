import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


# class A:
#     def __init__(self):
#      print("hello")

class Hello(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 350)

        

app = QApplication(sys.argv)
obj = Hello()
obj.show()
sys.exit(app.exec())


