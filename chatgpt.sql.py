import dataclasses
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PyQt6.QtGui import QIcon
import mysql.connector

# ✅ Database setup
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="sql_hazard",
    auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS login_page (
    name VARCHAR(20),
    username VARCHAR(40) PRIMARY KEY,
    password VARCHAR(20)
)
""")
mydb.commit()

class ProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login / Signup Page")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(200, 200, 350, 250)
        self.initUI()

    def initUI(self):
        label_name = QLabel("Name:")
        self.name_input = QLineEdit()

        label_user = QLabel("Username:")
        self.username_input = QLineEdit()

        label_pass = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.signup_button = QPushButton("Sign Up")

        self.login_button.clicked.connect(self.login_action)
        self.signup_button.clicked.connect(self.signup_action)

        layout = QVBoxLayout()
        layout.addWidget(label_name)
        layout.addWidget(self.name_input)
        layout.addWidget(label_user)
        layout.addWidget(self.username_input)
        layout.addWidget(label_pass)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def login_action(self):
        username = self.username_input.text()
        password = self.password_input.text()

        mycursor.execute("SELECT * FROM login_page WHERE username=%s AND password=%s", (username, password))
        result = mycursor.fetchone()

        if result:
            QMessageBox.information(self, "Success", f"Welcome back, {result[0]}!")
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")

    def signup_action(self):
        name = self.name_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        try:
            mycursor.execute("INSERT INTO login_page (name, username, password) VALUES (%s, %s, %s)",
                             (name, username, password))
            mydb.commit()
            QMessageBox.information(self, "Success", "Account created successfully! You can now log in.")
        except mysql.connector.errors.IntegrityError:
            QMessageBox.warning(self, "Error", "Username already exists. Try another one.")

mycursor = mydb.cursor()
mycursor.execute(;)
#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("background-color: rgb(255,255,255);")
    window = ProfileWindow()
    window.show()
    sys.exit(app.exec())
