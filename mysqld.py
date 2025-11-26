import sys
import pyQt6
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QHBoxLayout, QTextEdit,
    QTabWidget, QFormLayout, QSpinBox, QComboBox, QDateEdit,
    QTextEdit, QGroupBox, QScrollArea, QMainWindow
)
from PyQt6.QtCore import Qt, QDate


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root@123",
  database="sql_hazard",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
mycursor.execute()
#mydb.commit()


class ProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
          label1 = QLabel("USERNAME")
          label2 = QLabel("PASSSWORD")
          QApplication.setStyleSheet("background-color:rgb(255,255,255);")
          self.username=QLineEdit()
          self.password=QLineEdit()
button1 = QPushButton()
button2 = QPushButton()
window = ProfileWindow()
window.show()
app = QApplication(sys.argv)
app.setStyleSheet("background-color: rgb(255,255,255);")
window = ProfileWindow()
window.show()
sys.exit(app.exec())




