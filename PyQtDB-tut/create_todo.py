from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QCheckBox, QPushButton, QMessageBox, QLabel

class TodoForm(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Name input
        self.name_label = QLabel("Todo Name:")
        layout.addWidget(self.name_label)

        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_input)

        # Completed checkbox
        self.completed_label = QLabel("Completed:")
        layout.addWidget(self.completed_label)

        self.completed_checkbox = QCheckBox(self)
        layout.addWidget(self.completed_checkbox)

        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.submit_todo)
        layout.addWidget(self.submit_button)

        # Set layout
        self.setLayout(layout)
    
    def submit_todo(self):
        print("Submitting...")