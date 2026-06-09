from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

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

    def add_todo_item(self, name, completed):
        # Determine the current row count and insert a new row
        row_position = self.todo_table.rowCount()
        self.todo_table.insertRow(row_position)

        # Add the todo name in the first column
        self.todo_table.setItem(row_position, 0, QTableWidgetItem(name))

        status = "Completed" if completed else "Pending"
        self.todo_table.setItem(row_position, 1, QTableWidgetItem(status))