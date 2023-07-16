from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QPushButton, QLabel, QSlider, QFileDialog


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel()

        self.slider = QSlider()
        self.slider.valueChanged.connect(self.label.setNum)

        self.button = QPushButton(text="Emitir Señal")
        self.button.clicked.connect(self.customSlot)

        self.dialog = QFileDialog(self)
        self.dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.dialog.setNameFilter("Archivos de Python (*.py)")

        self.dialog.fileSelected.connect(self.label.setText)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.slider)

    def customSlot(self):
        self.label.clear()
        self.dialog.exec()

app = QApplication()

main_widget = MyWidget()
main_widget.show()

app.exec()