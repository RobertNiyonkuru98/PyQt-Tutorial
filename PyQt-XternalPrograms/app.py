from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget)
from PyQt6.QtCore import QProcess
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        # We'll run our process here
        self.message("Executing process.")
        self.p = QProcess()
        self.p.start("python", ['dummy_script.py']) # format is process = QProcess() and then process.start("<program_name>", "<arguments>")

    
app = QApplication([sys.argv])

w = MainWindow()
w.show()

app.exec()
