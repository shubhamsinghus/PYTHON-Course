
# def main():
#     print("hello world")
#
#
# if __name__ == '__main__':
#
#     main()
# i=0
# # sum=0
# while i<=4:
#     # sum+=i
#     # i = i+1
#     # i=i+1
#     i+=1
# print(i)

# i = 0
# while i<=6:
#     print(i)
#     i = i+1
import sys
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, button_1, QLineEdit, QGridLayout, QPushButton
# )
# from PyQt6.QtGui import QFont, QColor
# from PyQt6.QtCore import Qt,QSize
#
# app = QApplication(sys.argv)
#
# # --- Window Setup ---
# window = QWidget()
# window.setWindowTitle("My Mathematics Operations Software")
# window.setFixedSize(250, 250)
# window.setStyleSheet("background-color: #1e1e1e; color: white;")
#
# # --- Fonts ---
# label_font = QFont("Arial", 11)
# input_font = QFont("Consolas", 11)
# button_font = QFont("Arial", 11, QFont.Weight.Bold)
#
# # --- Widgets ---
# label1 = button_1("Num1:")
# label2 = label2("Num2:")
# label3 = button_1("Ans:")
#
# for label in [label1, label2, label3]:
#     label.setFont(label_font)
#
# input1 = QLineEdit()
# input2 = QLineEdit()
# input3 = QLineEdit()
# input3.setReadOnly(True)
#
# for inp in [input1, input2, input3]:
#     inp.setFont(input_font)
#     inp.setStyleSheet("padding: 4px; border-radius: 5px; border: 1px solid #555; color: black; background-color: white;")
#
# # --- Buttons ---
# button_add = QPushButton("+")
# button_sub = QPushButton("-")
# button_mul = QPushButton("*")
# button_div = QPushButton("/")
# button_clear = QPushButton("Clear")
#
# buttons = [button_add, button_sub, button_mul, button_div, button_clear]
# for b in buttons:
#     b.setFont(button_font)
#     b.setCursor(Qt.CursorShape.PointingHandCursor)
#     b.setFixedSize(QSize(80, 40))  # Equal QPushButton size
#     b.setStyleSheet("""
#         QPushButton {
#             background-color: #007ACC;
#             color: white;
#             border-radius: 6px;
#             padding: 8px;
#         }
#         QPushButton:hover {
#             background-color: #005F99;
#         }
#     """)
#
# # --- Layout ---
# layout = QGridLayout()
# layout.addWidget(label1, 0, 0)
# layout.addWidget(input1, 0, 1)
# layout.addWidget(label2, 1, 0)
# layout.addWidget(input2, 1, 1)
# layout.addWidget(label3, 2, 0)
# layout.addWidget(input3, 2, 1)
# layout.addWidget(button_add, 3, 0)
# layout.addWidget(button_sub, 3, 1)
# layout.addWidget(button_mul, 3, 2)
# layout.addWidget(button_div, 3, 3)
# layout.addWidget(button_clear, 4, 1, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
#window.setLayout(layout)

# --- Helper Function ---
# def safe_float(value):
#     try:
#         return float(value)
#     except ValueError:
#         return None
#
# # --- Operation Functions ---
# def add():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     input3.setText("Invalid Input" if num1 is None or num2 is None else str(num1 + num2))
#
# def sub():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     input3.setText("Invalid Input" if num1 is None or num2 is None else str(num1 - num2))
#
# def mul():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     input3.setText("Invalid Input" if num1 is None or num2 is None else str(num1 * num2))
#
# def div():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     if num1 is None or num2 is None:
#         input3.setText("Invalid Input")
#     else:
#         try:
#             result = num1 / num2
#             input3.setText(str(result))
#         except ZeroDivisionError:
#             input3.setText("Cannot divide by 0")
#
# def clear_fields():
#     input1.clear()
#     input2.clear()
#     input3.clear()
#
# # --- Connect Buttons ---
# button_add.clicked.connect(add)
# button_sub.clicked.connect(sub)
# button_mul.clicked.connect(mul)
# button_div.clicked.connect(div)
# button_clear.clicked.connect(clear_fields)

# --- Run App ---
# window.show()
# sys.exit(app.exec())
# import sys
# from PyQt6.QtGui import QFont
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QVBoxLayout
#
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle("My Creation - My Calculator")
# window.setFixedSize(400, 450)
#
# # --- Fonts ---
# font_display = QFont("Consolas", 16)
# font_button = QFont("Arial", 12, QFont.Weight.Bold)
#
# # --- Display Screen ---
# display = QLineEdit()
# display.setFont(font_display)
# display.setAlignment(Qt.AlignmentFlag.AlignRight)
# display.setReadOnly(True)
# display.setStyleSheet("""
#     QLineEdit {
#         border: 2px solid #007ACC;
#         border-radius: 8px;
#         padding: 10px;
#         color: white;
#         background-color: #1e1e1e;
#     }
# """)
#
# # --- Layout ---
# main_layout = QVBoxLayout()
# layout = QGridLayout()
#
# # --- Buttons ---
# buttons = {
#     '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3), 'C': (0, 4),
#     '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3), '(': (1, 4),
#     '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3), ')': (2, 4),
#     '0': (3, 0), '00': (3, 1), '.': (3, 2), '+': (3, 3), '=': (3, 4)
# }
#
# button_widgets = {}
#
# for text, pos in buttons.items():
#     button = QPushButton(text)
#     button.setFont(font_button)
#     button.setCursor(Qt.CursorShape.PointingHandCursor)
#     button.setStyleSheet("""
#         QPushButton {
#             background-color: #007ACC;
#             color: white;
#             border-radius: 8px;
#             padding: 10px;
#         }
#         QPushButton:hover {
#             background-color: #005f99;
#         }
#         QPushButton:pressed {
#             background-color: #003f66;
#         }
#     """)
#     button.setFixedHeight(55)
#     layout.addWidget(button, pos[0], pos[1])
#     button_widgets[text] = button
#
# # --- Logic ---
# def on_button_click(text):
#     current = display.text()
#
#     if text == 'C':
#         display.clear()
#
#     elif text == '=':
#         try:
#             # Evaluate the expression safely
#             expression = current.replace('^', '**')
#             result = str(eval(expression))
#             display.setText(result)
#         except Exception:
#             display.setText("Error")
#
#     else:
#         display.setText(current + text)
#
# # --- Connect Buttons ---
# for text, button in button_widgets.items():
#     button.clicked.connect(lambda _, t=text: on_button_click(t))
#
# # --- Final Layout Setup ---
# main_layout.addWidget(display)
# main_layout.addLayout(layout)
# window.setLayout(main_layout)
#
# # --- Show ---
# window.show()
# sys.exit(app.exec())
#
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtGui import QFont

class Signup(QWidget):
    def __init__(self):
        super().__init__()

        # --- Window setup ---
        self.setWindowTitle("Sign Up Window")
        self.setFixedSize(300, 300)
        self.setStyleSheet("background-color: #1e1e1e; color: blue;")

        # --- Layout ---
        layout = QGridLayout()

        # --- Labels and Inputs ---
        label_username = QLabel("Username:")
        label_password = QLabel("Password:")
        input_username = QLineEdit()
        input_password = QLineEdit()
        input_password.setEchoMode(QLineEdit.EchoMode.Password)

        # --- Button ---
        signup_button = QPushButton("Sign Up")
        signup_button.setStyleSheet("""
            QPushButton {
                background-color: #007ACC;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #005F99;
            }
        """)

        # --- Add widgets to layout ---
        layout.addWidget(label_username, 0, 0)
        layout.addWidget(input_username, 0, 1)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(input_password, 1, 1)
        layout.addWidget(signup_button, 2, 0, 1, 2)

        self.setLayout(layout)

# --- Run the app ---
app = QApplication(sys.argv)
window1 = Signup()
window1.show()
sys.exit(app.exec())



#signup window


import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QGridLayout, QMessageBox
)
from PyQt6.QtCore import Qt
import pyrebase

# ---------------- FIREBASE CONFIG ---------------- #
firebaseConfig = {
    "apiKey": "AIzaSyAEXAMPLE12345",
    "authDomain": "your-project-id.firebaseapp.com",
    "databaseURL": "https://your-project-id-default-rtdb.firebaseio.com/",
    "projectId": "your-project-id",
    "storageBucket": "your-project-id.appspot.com",
    "messagingSenderId": "123456789012",
    "appId": "1:123456789012:web:abc123def456"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


# ---------------- SIGNUP WINDOW ---------------- #
class SignupWindow(QWidget):
    def __init__(self, switch_to_login):
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QGridLayout()
        self.setLayout(layout)

        # --- Inputs ---
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # --- Labels ---
        layout.addWidget(QLabel("Full Name:"), 0, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(QLabel("Email:"), 1, 0)
        layout.addWidget(self.email_input, 1, 1)
        layout.addWidget(QLabel("Password:"), 2, 0)
        layout.addWidget(self.password_input, 2, 1)

        # --- Buttons ---
        self.signup_button = QPushButton("Sign Up")
        self.login_button = QPushButton("Already have an account? Login")

        for btn in [self.signup_button, self.login_button]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #007ACC;
                    color: white;
                    border-radius: 5px;
                    padding: 8px;
                }
                QPushButton:hover {
                    background-color: #005F99;
                }
            """)

        layout.addWidget(self.signup_button, 3, 0, 1, 2)
        layout.addWidget(self.login_button, 4, 0, 1, 2)

        # --- Connect Buttons ---
        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(switch_to_login)

    def signup(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        if not name or not email or not password:
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        try:
            # Create account in Firebase
            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']

            # Store user info in Realtime Database
            db.child("users").child(uid).set({
                "name": name,
                "email": email
            })

            QMessageBox.information(self, "Success", "Account created successfully!")
            self.name_input.clear()
            self.email_input.clear()
            self.password_input.clear()

        except Exception as e:
            QMessageBox.warning(self, "Signup Failed", f"Error: {str(e)[:120]}")


# ---------------- LOGIN WINDOW ---------------- #
class LoginWindow(QWidget):
    def __init__(self, switch_to_signup):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #1e1e1e; color: white; font-size: 14px;")

        layout = QGridLayout()
        self.setLayout(layout)

        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(QLabel("Email:"), 0, 0)
        layout.addWidget(self.email_input, 0, 1)
        layout.addWidget(QLabel("Password:"), 1, 0)
        layout.addWidget(self.password_input, 1, 1)

        self.login_button = QPushButton("Login")
        self.signup_button = QPushButton("Create a new account")

        for btn in [self.login_button, self.signup_button]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #007ACC;
                    color: white;
                    border-radius: 5px;
                    padding: 8px;
                }
                QPushButton:hover {
                    background-color: #005F99;
                }
            """)

        layout.addWidget(self.login_button, 2, 0, 1, 2)
        layout.addWidget(self.signup_button, 3, 0, 1, 2)

        # --- Connect Buttons ---
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(switch_to_signup)

    def login(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            QMessageBox.information(self, "Welcome!", f"Login successful!\nUser: {email}")
        except Exception as e:
            QMessageBox.warning(self, "Login Failed", "Invalid credentials or user not found.")


# ---------------- APP CONTROLLER ---------------- #
class AppController:
    def __init__(self):
        self.signup_window = SignupWindow(self.show_login)
        self.login_window = LoginWindow(self.show_signup)
        self.signup_window.show()

    def show_login(self):
        self.signup_window.hide()
        self.login_window.show()

    def show_signup(self):
        self.login_window.hide()
        self.signup_window.show()


# ---------------- RUN APP ---------------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec())
