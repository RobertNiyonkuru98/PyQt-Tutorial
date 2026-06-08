from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget

class TodoTable(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        #table widget

        self.todo_table = QTableWidget()
        self.todo_table.setColumnCount(2)
        self.todo_table.setHorizontalHeaderLabels(
            ['Todo Name', 'Completed']
        )

        layout.addWidget(self.todo_table)
        self.setLayout(layout)