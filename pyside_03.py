from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QStackedLayout
from FormularioWidget import FormularioWidget

# LAYOUTS
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        

        self.label2 = QLabel()
        self.label2.setText("Label 2")

        self.label3 = QLabel()
        self.label3.setText("Label 3")
            
        # layout
        self.layout = QStackedLayout(self)
        self.layout.addWidget(FormularioWidget())
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.label3)

    def cambiarWidget(self, index):
        self.layout.setCurrentIndex(index)


app = QApplication()

main_widget = QWidget()

mywidget = MyWidget()

combo = QComboBox()
combo.addItem("Seleccionar 1")
combo.addItem("Seleccionar 2")
combo.addItem("Seleccionar 3")
combo.activated.connect(mywidget.cambiarWidget)

layout = QVBoxLayout(main_widget)
layout.addWidget(mywidget)
layout.addWidget(combo)

main_widget.show()
app.exec()