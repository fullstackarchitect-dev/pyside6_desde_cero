from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout, QFormLayout

from PySide6.QtCore import Qt


class MultipleLayoutWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Top Layout
        topLayout = QHBoxLayout()
        button1 = QPushButton(text="Datos Personales")
        button1.clicked.connect(self.cambiarWidget1)
        topLayout.addWidget(button1)

        button2 = QPushButton(text="Datos Laborales")
        button2.clicked.connect(self.cambiarWidget2)
        topLayout.addWidget(button2)

        button3 = QPushButton(text="Datos Educacionales")
        button3.clicked.connect(self.cambiarWidget3)
        topLayout.addWidget(button3)

        # Right Layout
        rightLayout = QVBoxLayout()
        reset_button = QPushButton(text="Reset")
        reset_button.clicked.connect(self.reset)
        rightLayout.addWidget(reset_button)

        guardar_button = QPushButton(text="Guardar")
        guardar_button.clicked.connect(self.guardar)
        rightLayout.addWidget(guardar_button)

        # Form Layouts
        widget1 = QWidget()
        form1 = QFormLayout(widget1)
        self.nombre_line_edit = QLineEdit()
        form1.addRow("Nombre:", self.nombre_line_edit)

        self.apellido_line_edit = QLineEdit()
        form1.addRow("Apellido:", self.apellido_line_edit)

        widget2 = QWidget()
        form2 = QFormLayout(widget2)
        form2.addRow("Experiencia Laboral:", QTextEdit())

        widget3 = QWidget()
        form3 = QFormLayout(widget3)
        form3.addRow("Educación:", QTextEdit())

        # Stack Layout
        self.stackLayout = QStackedLayout()
        self.stackLayout.addWidget(widget1)
        self.stackLayout.addWidget(widget2)
        self.stackLayout.addWidget(widget3)

        # Parent Layout
        parentLayout = QGridLayout(self)
        parentLayout.addLayout(topLayout, 0, 0)
        parentLayout.addLayout(self.stackLayout, 1, 0)
        parentLayout.addLayout(rightLayout, 1, 1, alignment=Qt.AlignmentFlag.AlignBottom)

    def cambiarWidget1(self):
        self.stackLayout.setCurrentIndex(0)

    def cambiarWidget2(self):
        self.stackLayout.setCurrentIndex(1)

    def cambiarWidget3(self):
        self.stackLayout.setCurrentIndex(2)

    def reset(self):
        self.nombre_line_edit.clear()
        self.apellido_line_edit.clear()

    def guardar(self):
        
        print(f"guardando... {self.nombre_line_edit.text()}")

app = QApplication()

main_widget = MultipleLayoutWidget()

main_widget.show()

app.exec()