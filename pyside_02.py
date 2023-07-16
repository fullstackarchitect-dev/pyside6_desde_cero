from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from FormularioWidget import FormularioWidget


app = QApplication()

widget_principal = QWidget()

widget1 = FormularioWidget()
widget2 = FormularioWidget()

label_info = QLabel()
label_info.setText("Version 0.1")

layout = QHBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)
layout.addWidget(label_info)

widget_principal.setLayout(layout)
widget_principal.show()
app.exec()