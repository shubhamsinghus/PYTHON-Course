# import sys
#
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QIcon
# from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,QMessageBox
#
# # from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QStyleFactory, QVBoxLayout, QLineEdit
# # import PyQt6.QtWidgets as qt
# # from PyQt6.QtWidgets import *
#
#
# app = QApplication([])
# import pyrebase
# # --- Firebase Configuration ---
# firebaseConfig = {
#     "apiKey": "YOUR_API_KEY",
#     "authDomain": "YOUR_AUTH_DOMAIN",
#     "databaseURL": "YOUR_DATABASE_URL",
#     "projectId": "YOUR_PROJECT_ID",
#     "storageBucket": "YOUR_STORAGE_BUCKET",
#     "messagingSenderId": "YOUR_MSG_SENDER_ID",
#     "appId": "YOUR_APP_ID"
# }
#
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
#
#
# class Signup(QWidget):
#     def __init__(self):
#         super().__init__()
#         #window setup
#         # self.window_title="Sign Up Window"
#         self.setWindowTitle("Sign Up Window")
#         self.setWindowIcon(QIcon("icon.png"))
#         self.setFixedSize(300,300)
#         self.setStyleSheet("background-color: white; color: black;")
#         #layout
#         # layout = QVBoxLayout()
#         # self.setLayout(layout)
#
#         layout = QGridLayout()
#         self.setLayout(layout)
#         #Labels
#         self.label1_Username=QLabel("USERNAME")
#         layout.addWidget(self.label1_Username,0,0)
#
#         self.label2_Password=QLabel("PASSWORD",)
#         layout.addWidget(self.label2_Password,1,0)
#         input_username = QLineEdit()
#         layout.addWidget(input_username,0,1)
#         input_password = QLineEdit()
#         layout.addWidget(input_password,1,1)
#         input_password.setEchoMode(QLineEdit.EchoMode.Password)
#
#         signup_button = QPushButton("Sign Up")
#         layout.addWidget(signup_button,2,0,1,2)
#         signup_button.setStyleSheet("""
#                     QPushButton {
#                         background-color: #008567ACC;
#                         color: white;
#                         border-radius: 5px;
#                         padding: 20px;
#                     }
#                     QPushButton:circle {
#                         background-color: ;
#                     }
#                 """)
#         login_button = QPushButton("Login")
#         layout.addWidget(login_button,3,0,1,2)
#
#         self.button_signup.clicked.connect(self.create_account)
#
#         def create_account(self):
#             username = self.input_username.text().strip()
#             password = self.input_password.text().strip()
#
#             if not username or not password:
#                 QMessageBox.warning(self, "Error", "Please fill in all fields.")
#                 return
#
#             if username in users:
#                 QMessageBox.warning(self, "Error", "Username already exists.")
#                 return
#
#             users[username] = password
#             QMessageBox.information(self, "Success", "Account created successfully!")
#             self.input_username.clear()
#             self.input_password.clear()
#
#
# class Login(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Login Window")
#         self.setWindowIcon(QIcon("icon.png"))
#         self.setFixedSize(300,300)
#         self.setStyleSheet("background-color: white; color: black;")
#         #layout
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.label1_Username=QLabel("USERNAME")
#         layout.addWidget(self.label1_Username,0,0)
#         self.label2_Password=QLabel("PASSWORD",)
#         layout.addWidget(self.label2_Password,1,0)
#         input_username = QLineEdit()
#         layout.addWidget(input_username,0,1)
#         input_password = QLineEdit()
#         layout.addWidget(input_password,1,1)
#         input_password.setEchoMode(QLineEdit.EchoMode.Password)
#
#         button_login = QPushButton("Login")
#         layout.addWidget(button_login,2,0,1,2)
#         button_login.setStyleSheet("""
#         QPushButton {
#         background-color: #008567ACC;
#         color: white;
#         border-radius: 5px;
#         padding: 20px;
#         }
#         QPushButton:circle {
#                         background-color: ;
#                     }
#                 """)
# #frunctionallity
#
#
# window1=Signup()
# window1.show()
#
# sys.exit(app.exec())
#
#
#
# # Real time database :- CRUD :- create , read , update , delete

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QHBoxLayout
)
import firebase_admin

from firebase_admin import credentials, db

# --- FIREBASE INITIALIZATION USING FILE PATH ---
cred = credentials.Certificate(r"D:\PRACTICE\edunova-hr--recruitmentsystem-firebase-adminsdk-fbsvc-116b9d2478.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://edunova-hr--recruitmentsystem-default-rtdb.firebaseio.com'
})

# --- AUTH WINDOW CLASS ---
class AuthApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduNova HR - Admin Portal")
        self.setFixedSize(400, 380)

        # Widgets
        self.title = QLabel("EduNova HR Admin", self)
        self.title.setStyleSheet("font-size: 22px; font-weight: bold; color: #fff; margin-bottom: 15px;")

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter email")

        self.role_label = QLabel("Role:")
        self.role_input = QLineEdit()
        self.role_input.setPlaceholderText("e.g., HR, Candidate")

        # Buttons
        self.save_btn = QPushButton("Save User")
        self.fetch_btn = QPushButton("Fetch Users")

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_input)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.fetch_btn)
        layout.addLayout(btn_layout)

        layout.addStretch()
        self.setLayout(layout)
        self.apply_styles()

        # Connect buttons
        self.save_btn.clicked.connect(self.save_user)
        self.fetch_btn.clicked.connect(self.fetch_users)

    # --- SAVE USER TO DATABASE ---
    def save_user(self):
        email = self.email_input.text().strip()
        role = self.role_input.text().strip()

        if not email or not role:
            QMessageBox.warning(self, "Missing Info", "Please enter both email and role.")
            return

        try:
            ref = db.reference("users")
            ref.push({"email": email, "role": role})
            QMessageBox.information(self, "Success", f"✅ User saved: {email} ({role})")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"❌ Failed to save user.\n{e}")

    # --- FETCH USERS FROM DATABASE ---
    def fetch_users(self):
        try:
            ref = db.reference("users")
            users = ref.get()
            if users:
                msg = "\n".join([f"{u['email']} ({u['role']})" for u in users.values()])
                QMessageBox.information(self, "User List", msg)
            else:
                QMessageBox.information(self, "User List", "No users found.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"❌ Failed to fetch users.\n{e}")

    # --- STYLING FUNCTION ---
    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E2F;
                color: white;
                font-family: 'Segoe UI';
                font-size: 14px;
            }

            QLineEdit {
                background-color: #2C2C3E;
                border: 1px solid #5A5A7E;
                border-radius: 8px;
                padding: 6px;
                }""")

