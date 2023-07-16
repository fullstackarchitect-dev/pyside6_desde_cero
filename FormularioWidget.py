from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton


class FormularioWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Labels
        self.nombre_label = QLabel()
        self.nombre_label.setText("Nombre:")
        self.apellido_label = QLabel()
        self.apellido_label.setText("Apellido:")

        # LineEdits
        self.nombre_line_edit = QLineEdit()
        self.apellido_line_edit = QLineEdit()

        # Button
        self.guardar_button = QPushButton()
        self.guardar_button.setText("Guardar")
        self.guardar_button.clicked.connect(self.guardar)

        # Layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.nombre_label)
        self.layout.addWidget(self.nombre_line_edit)
        self.layout.addWidget(self.apellido_label)
        self.layout.addWidget(self.apellido_line_edit)
        self.layout.addWidget(self.guardar_button)

        self.setLayout(self.layout)

    def guardar(self):
        print(f"Datos guardados exitosamente {self.nombre_line_edit.text()} {self.apellido_line_edit.text()}")

