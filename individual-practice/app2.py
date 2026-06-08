from PyQt6.QtWidgets import QMainWindow, QApplication, QLayout, QLabel, QVBoxLayout,QLineEdit,QPushButton,QHBoxLayout,QWidget
from PyQt6.QtCore import Qt

class StudyExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Study Concept")
        self.setFixedSize(300,200)

        layout = QVBoxLayout()

        self.label = QLabel("Hello There")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Who are you....")

        self.btn = QPushButton("Submit...")
        self.btn.clicked.connect(self.on_submit_clicked)
        self.input.returnPressed.connect(self.on_submit_clicked)

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.btn)
        
        self.setLayout(layout)

    def on_submit_clicked(self):
        user_text = self.input.text()
        self.label.setText(f"You submitted {user_text}")
        self.input.clear()

app = QApplication([])
study = StudyExample()
study.show()
app.exec()