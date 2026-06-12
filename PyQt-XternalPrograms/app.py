# Running an external program using the QProcess class from the PyQt6 , and displaying process status messages
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget)
from PyQt6.QtCore import QProcess
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("External Program Status Messages")
        self.setFixedSize(400, 400)

        self.p = None # Default will be an empty value

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
        if self.p is None: # No process is running at this line
            self.message("Executing process.")
            self.p = QProcess() # Keep a reference to the QProcess while its running
            self.p.finished.connect(self.process_finished) # Clean up once the command process is complete
            self.p.start("python", ['dummy_script.py']) # format is process = QProcess() and then process.start("<program_name>", "<arguments>")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None

    
app = QApplication([sys.argv])

w = MainWindow()
w.show()

app.exec()
