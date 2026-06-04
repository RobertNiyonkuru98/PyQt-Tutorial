from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QSlider, QMainWindow
from PyQt6.QtCore import QSize
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")
        self.setFixedSize(QSize(500,100)) # Setting the size of the window to be fixed format (width, height)
        layout = QVBoxLayout()
        self.label = QLabel("<h1>This is an informative text message</h1>")
        self.button = QPushButton("Click here...")
        self.button.clicked.connect(self.button_clicked)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        window = QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)

    def button_clicked(self):
        self.label.setText("<h1>Button Clicked! Good job.</h1>")
        self.button.setText("Thanks for clicking!")


app = QApplication([])
window = MainWindow()
window.show()

# Start the event loop -> listens always for events when the app is running like video games listening for input
app.exec()