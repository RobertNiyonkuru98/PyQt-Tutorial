# Monitoring the standardoutput and standarderror of the external program
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget)
from PyQt6.QtCore import QProcess
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)            
            self.p.finished.connect(self.process_finished) # Clean up once the command process is complete
            self.p.start("python", ['dummy_script.py']) # format is process = QProcess() and then process.start("<program_name>", "<arguments>")

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf-8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf-8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.ProcessState.NotRunning: "Not Running",
            QProcess.ProcessState.Starting: "Starting",
            QProcess.ProcessState.Running: "Running"
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None

    
app = QApplication([sys.argv])

w = MainWindow()
w.show()

app.exec()
