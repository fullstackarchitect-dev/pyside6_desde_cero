from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar, QTabWidget, QMessageBox, QFileDialog, QLabel
from PySide6.QtGui import QAction


class Editor(QTextEdit):
    def __init__(self, filepath=''):
        super().__init__()

        self.setFilepath(filepath)

    def setFilepath(self, filepath):
        self.filepath = filepath
        self.title = filepath.split("/")[-1] if filepath else ''

    def open(self):
        
        with open(self.filepath, "r") as f:
            self.document().setPlainText(f.read())
            self.document().setModified(False)
            self.setFilepath(self.filepath)
            return True

    def closeRequested(self):
        if not self.document().isModified():
            return True
        
        confirmBox = QMessageBox()
        confirmBox.setText("Save?")
        confirmBox.setInformativeText("Save???")
        buttons = QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel 
        confirmBox.setStandardButtons(buttons)
        confirmResult = confirmBox.exec()
        if confirmResult == QMessageBox.StandardButton.Discard:
            return True 
        if confirmResult == QMessageBox.StandardButton.Cancel:
            return False 
        
        return self.save()

    def save(self):
        if not self.document().isModified():
            return True
        
        if self.filepath == '':
            return self.saveAs()
        
        with open(self.filepath, "w") as f:
            f.write(self.document().toPlainText())
            self.document().setModified(False)
            return True

    def saveAs(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save", ".", "Text Files (*.txt)", "Text Files (*.txt)")
        if not path:
            return False
        
        with open(path, "w") as f:
            f.write(self.document().toPlainText())
            self.document().setModified(False)
            self.setFilepath(path)
            return True

class NotepadMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notepad PySide6")
        self.setGeometry(350, 200, 800, 600)

        # Tool Bar
        newAction = QAction("New", self)
        newAction.triggered.connect(self.newSlot)

        openAction = QAction("Open", self)
        openAction.triggered.connect(self.openSlot)

        saveAction = QAction("Save", self)
        saveAction.triggered.connect(self.saveSlot)

        saveAsAction = QAction("Save As", self)
        saveAsAction.triggered.connect(self.saveAsSlot)

        toolBar = QToolBar()
        self.addToolBar(toolBar)
        toolBar.addAction(newAction)
        toolBar.addAction(openAction)
        toolBar.addAction(saveAction)
        toolBar.addAction(saveAsAction)

        # Central Widget
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.tabCloseRequestedSlot)
        self.tabs.currentChanged.connect(self.currentChangedSlot)
        self.setCentralWidget(self.tabs)

        # Status Bar Version
        aboutLabel = QLabel()
        aboutLabel.setText("Version 1.0")
        self.statusBar().addPermanentWidget(aboutLabel)

    def currentChangedSlot(self, index):
        self.statusBar().showMessage(self.tabs.widget(index).filepath)

    def tabCloseRequestedSlot(self, index):
        editor = self.tabs.widget(index)
        if editor.closeRequested():
            self.tabs.removeTab(index)

    def newSlot(self):
        editor = Editor()
        editor.document().modificationChanged.connect(self.modificationChangedSlot)
        index = self.tabs.addTab(editor, editor.title)
        self.tabs.setCurrentIndex(index)

    def modificationChangedSlot(self, modified):
        index = self.tabs.currentIndex()
        if modified:
            self.tabs.setTabText(index, f"*{self.tabs.widget(index).title}")
        else:
            self.tabs.setTabText(index, f"{self.tabs.widget(index).title}")
            

    def openSlot(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open", ".", "Text Files (*.txt)", "Text Files (*.txt)")
        
        if not path:
            return
        
        for i in range(self.tabs.count()):
            prevEditor = self.tabs.widget(i)
            if prevEditor.filepath == path:
                self.tabs.setCurrentIndex(i)
                return

        editor = Editor(path)

        if editor.open():
            index = self.tabs.addTab(editor, editor.title)
            self.tabs.setCurrentIndex(index)
            self.statusBar().showMessage(editor.filepath)

    def saveSlot(self):
        editor = self.tabs.widget(self.tabs.currentIndex())
        if editor.save():
            self.tabs.setTabText(self.tabs.currentIndex(), editor.title)
            self.statusBar().showMessage(editor.filepath)

    def saveAsSlot(self):
        editor = self.tabs.widget(self.tabs.currentIndex())
        if editor.saveAs():
            self.tabs.setTabText(self.tabs.currentIndex(), editor.title)
            self.statusBar().showMessage(editor.filepath)

    def closeEvent(self, event):
        canClose = True 

        for i in range(self.tabs.count()):
            editor = self.tabs.widget(i)
            self.tabs.setCurrentIndex(i)
            if not editor.closeRequested():
                canClose = False
                break
            self.tabs.setTabText(i, editor.title)

        if canClose:
            event.accept()
        else:
            event.ignore()

app = QApplication()

main_window = NotepadMainWindow()
main_window.show()

app.exec()