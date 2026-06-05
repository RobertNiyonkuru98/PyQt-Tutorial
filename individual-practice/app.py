from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLayout, QVBoxLayout, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practicing cuh...")
        self.label = QLabel("<h1>Yello</h1>")
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.button_clicked)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        window = QWidget()
        window.setLayout(layout)
        self.setCentralWidget(window)
    def button_clicked(self):
        self.label.setText("<h1>You clicked the button, Good job!</h1>")
        self.button.setText("Thanks for clicking!")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
