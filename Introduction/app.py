from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QSlider

app = QApplication([])

def button_clicked():
    label.setText("<h1>Button Clicked! Good job.</h1>")
    button.setText("Thanks for clicking!")

# Create a Qt widget, which will be our window
window = QWidget()
window.setWindowTitle("My First App") # Giving window a title
# window.setGeometry(50, 50, 1800, 200) # Moving window to (100, 100) with width 400 and height 300 --- (x,y, width, height) format

layout = QVBoxLayout(window)
label = QLabel("<h1>This is an informative text message</h1>", parent=window)
button = QPushButton("Click here...", parent=window)
button.clicked.connect(button_clicked)
# slider= QSlider

# slider.setMinimum(0)
# slider.setMaximum(3000)

layout.addWidget(label)
layout.addWidget(button)
# layout.addWidget(slider)

window.show() # IMPORTANT!!! WINDOWS ARE HIDDEN BY DEFAULT

# Start the event loop -> listens always for events when the app is running like video games listening for input
app.exec()