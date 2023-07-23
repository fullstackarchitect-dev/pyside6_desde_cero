# QFileDialog
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QHBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        abrir_button = QPushButton("Abrir")
        abrir_button.clicked.connect(self.abrirArchivo)

        guardar_button = QPushButton("Guardar Nuevo Archivo")
        guardar_button.clicked.connect(self.guardarArchivo)

        seleccionar_multiple = QPushButton("Seleccionar Multiple")
        seleccionar_multiple.clicked.connect(self.seleccionarMultiple)

        layout = QHBoxLayout(self)
        layout.addWidget(abrir_button)
        layout.addWidget(guardar_button)
        layout.addWidget(seleccionar_multiple)

    def seleccionarMultiple(self):
        paths, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Multiples", ".", "Text Files (*.txt)", "Text File (*.txt)")
        
        if not paths:
            print("archivos no seleccionados...")

        for path in paths:
            texto = self.leerTextDesdeArchivo(path)
            print(texto)

    def guardarArchivo(self):
        
        path, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo...", ".", "Text Files (*.txt)", "Text Files (*.txt)")

        if not path:
            print("archivo no seleccionado...")

        self.escribirTextoEnArchivo(path, "Probando QFileDialog")

    def abrirArchivo(self):
        path, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo Caption", ".", "Text Files (*.txt)", "Text Files (*.txt)")
        
        if not path:
            print("archivo no seleccionado...")
            return
        
        texto = self.leerTextDesdeArchivo(path)
        print(texto)

    def escribirTextoEnArchivo(self, path, texto):
        with open(path, "w") as archivo:
            archivo.write(texto)

    def escribirTextoEnArchivoModoAppend(self, path, texto):
        with open(path, "a") as archivo:
            archivo.write(texto)

    def leerTextDesdeArchivo(self, path):
        with open(path, "r") as archivo:
            return archivo.read()


app = QApplication()

main_widget = MyWidget()
main_widget.show()

app.exec()


# Modos: r, w, a


