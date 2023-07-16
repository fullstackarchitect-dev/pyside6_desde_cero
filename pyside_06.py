from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QTextEdit, QToolBar
from PySide6.QtGui import QAction

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Status Bar
        self.about_label = QLabel()
        self.about_label.setText("Version 0.1")
        self.statusBar().addPermanentWidget(self.about_label)

        # Central Widget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Action
        resetAction = QAction("Reset", self)
        resetAction.triggered.connect(self.reset)

        # Tool Bar
        toolBar = QToolBar()
        self.addToolBar(toolBar)
        toolBar.addAction(resetAction)

        # Menu Bar
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(resetAction)

    def reset(self):
        self.textEdit.clear()

app = QApplication()

main_widget = MyMainWindow()
main_widget.show()

app.exec()