from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget)
from PyQt6.QtCore import QProcess
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.p = None

        self.setWindowTitle("QProcess Tutorial")
        self.setFixedSize(400,400)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.text)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

    def message(self,s):
        self.text.appendPlainText(s)

    def start_process(self):
        pass

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
