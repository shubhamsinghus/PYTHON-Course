# import sys
# from PyQt6.QtWidgets import QApplication, QWidget
#
#
# class Pyqt(QWidget):
#     def _init_(self):
#         super()._init_()
#
#
# app = QApplication(sys.argv)    # basic format to pyQt6 program
# obj = Pyqt()
# obj.show()
# sys.exit(app.exec())
# # import sys
# from PyQt6.QtWidgets import QApplication, button_1, QWidget, QVBoxLayout
#
# def main():
#     app = QApplication([])
#
#     window = QWidget()
#     window.setWindowTitle('Hello PyQt6')
#
#     layout = QVBoxLayout()
#
#     label = button_1('Hello, World!')
#     layout.addWidget(label)
#
#     window.setLayout(layout)
#     window.resize(600, 600)
#     window.show()
#
#     sys.exit(app.exec())
#
# if __name__ == '__main__':
#     main()


from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit
#
# app = QApplication([])
#
# window = QWidget()
# layout = QHBoxLayout()
#
# layout.addWidget(QLineEdit("Button 1"))
# layout.addWidget(QLineEdit("Button 2"))
# layout.addWidget(QLineEdit("Button 3"))
#
# window.setLayout(layout)
# window.setWindowTitle("QVBoxLayout Example")
# window.show()
#
# app.exec()



#
#
# from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit
#
# app = QApplication([])
#
# window = QWidget()
# layout = QGridLayout()
#
# layout.addWidget(QLineEdit("Button (0,0)"), 0, 0)
# layout.addWidget(QLineEdit("Button (0,1)"), 0, 1)
# layout.addWidget(QLineEdit("Button (1,0)"), 1, 0)
# layout.addWidget(QLineEdit("Button (1,1)"), 1, 1)
# layout.addWidget(QLineEdit("Button (1,1)"), 2, 2)
# layout.addWidget(QLineEdit("Button (5,5)"), 5, 5)
# layout.addWidget(QLineEdit("Button"), 5, 4)
#
# layout.addWidget(QLineEdit("Button (4,4)"), 4, 4)
#
#
# window.setLayout(layout)
# window.setWindowTitle("QGridLayout Example")
# window.show()
#
# app.exec()
#
# import sys
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QWidget, button_1, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, \
#     QPushButton
#
# app = QApplication(sys.argv)
# window = QWidget()
#
# window.setWindowTitle("My first App")
# window.setFixedSize(350,250)
# label1 = button_1("Num1")
# button_2 = button_1("Num2")
# label3 = button_1("Ans")
# input1 = QLineEdit(" ")
# input2 = QLineEdit(" ")
# input3 = QLineEdit(" ")
# input3.setReadOnly(True)
# layout = QGridLayout()
# button_add = QPushButton("+")
# button_sub = QPushButton("-")
# button_mul = QPushButton("*")
# button_div = QPushButton("/")
# button_clear = QPushButton("clear")
#
# layout.addWidget(label1, 0, 0)
# layout.addWidget(input1, 0, 1)
# layout.addWidget(button_2, 1,0)
# layout.addWidget(input2, 1,1)
# layout.addWidget(label3, 2,0)
# layout.addWidget(input3, 2,1)
# # layout.addWidget(QPushButton("+"), 4, 0)
# # layout.addWidget(QPushButton("-"), 4, 1)
# # layout.addWidget(QPushButton("*"), 4, 2)
# # layout.addWidget(QPushButton("/"), 4, 3)
# layout.addWidget(button_add, 3, 0)
# layout.addWidget(button_sub, 3, 1)
# layout.addWidget(button_mul, 3, 2)
# layout.addWidget(button_div, 3, 3)
# layout.addWidget(button_clear, 4, 1, 1, 2)  # Center the clear QPushButton
#
# window.setLayout(layout)
#
#
# def safe_float(value):
#     """Convert string to float, return None if invalid."""
#     try:
#         return float(value)
#     except ValueError:
#         return None
#
# def add():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     if num1 is None or num2 is None:
#         input3.setText("Invalid Input")
#     else:
#         input3.setText(str(num1 + num2))
#
# def sub():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     if num1 is None or num2 is None:
#         input3.setText("Invalid Input")
#     else:
#         input3.setText(str(num1 - num2))
#
# def mul():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     if num1 is None or num2 is None:
#         input3.setText("Invalid Input")
#     else:
#         input3.setText(str(num1 * num2))
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
# def clear_fields():
#     input1.clear()
#     input2.clear()
#     input3.clear()
#
#
# button_add.clicked.connect(add)
# button_sub.clicked.connect(sub)
# button_mul.clicked.connect(mul)
# button_div.clicked.connect(div)
# button_clear.clicked.connect(clear_fields)
#
#
#
# result=input1.text()+input2.text()
# window.setWindowTitle(" My  mathematics operations software")
#
# window.show()
# sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, button_1, QLineEdit, QGridLayout, QPushButton
# )
# from PyQt6.QtGui import QFont, QColor
# from PyQt6.QtCore import Qt,QSize
#
# app = QApplication(sys.argv)
#
# window.setLayout(layout)
#
# # --- Helper for safe float conversion ---
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
#     if num1 is None or num2 is None:
#         input3.setText("Invalid Input")
#     else:
#         input3.setText(str(num1 + num2))
#
# def sub():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     if num1 is None or num2 is None:
#         input3.setText("Invalid Input")
#     else:
#         input3.setText(str(num1 - num2))
#
# def mul():
#     num1 = safe_float(input1.text())
#     num2 = safe_float(input2.text())
#     if num1 is None or num2 is None:
#         input3.setText("Invalid Input")
#     else:
#         input3.setText(str(num1 * num2))
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
#
# # --- Run App ---
# window.show()
# sys.exit(app.exec())

import sys

from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, \
    QPushButton
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("My creation my calculator")
window.setFixedSize(400, 350)

layout= QGridLayout()

button_1=QPushButton("1")
button_2=QPushButton("2")
button_3=QPushButton("3")
button_4=QPushButton("4")
button_5=QPushButton("5")
button_6=QPushButton("6")
button_7=QPushButton("7")
button_8=QPushButton("8")
button_9=QPushButton("9")
button_0=QPushButton("0")
button_00=QPushButton("00")
button_add = QPushButton("+")
button_sub = QPushButton("-")
button_mul = QPushButton("*")
button_div = QPushButton("/")
button_clear = QPushButton("C")
button_equal = QPushButton("=")
button_decimal = QPushButton(".")
button_open_bracket = QPushButton("(")
button_close_bracket = QPushButton(")")


layout.addWidget(button_7,0,0)
layout.addWidget(button_8,0,1)
layout.addWidget(button_9,0,2)
layout.addWidget(button_div,0,3)
layout.addWidget(button_clear,0,4)

layout.addWidget(button_4,1,0)
layout.addWidget(button_5,1,1)
layout.addWidget(button_6,1,2)
layout.addWidget(button_mul,1,3)
layout.addWidget(button_open_bracket,1,4)

layout.addWidget(button_1,2,0)
layout.addWidget(button_2,2,1)
layout.addWidget(button_3,2,2)
layout.addWidget(button_sub,2,3)
layout.addWidget(button_close_bracket,2,4)


layout.addWidget(button_0, 3, 0)
layout.addWidget(button_00, 3, 1)
layout.addWidget(button_decimal, 3, 2)
layout.addWidget(button_add, 3, 3)
layout.addWidget(button_equal, 3, 4)





window.setLayout(layout)

window.show()
sys.exit(app.exec())








#
#
#
