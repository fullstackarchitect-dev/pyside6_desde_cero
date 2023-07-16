### REQUERIMIENTOS ###

# Python 3.11+
# VS Code
# python -m venv venv
# pip install pyside6 
# Minimal GUI

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QMessageBox

app = QApplication()

label = QLabel()
label.setText("Soy un label...")

label2 = QLabel()
label2.setText("Soy otro label...")

def apretar():
    msg = QMessageBox()
    msg.setWindowTitle("Notificacion")
    msg.setText("He sido apretado")
    msg.exec()

button = QPushButton()
button.setText("Apretame")
button.clicked.connect(apretar)

widget = QWidget()

layout = QHBoxLayout()
layout.addWidget(label)
layout.addWidget(label2)
layout.addWidget(button)

widget.setLayout(layout)
widget.show()

app.exec()