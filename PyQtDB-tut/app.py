from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtSql import QSqlDatabase
from db import open_connection
from create_todo import TodoForm
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do Application")
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.todo_form = TodoForm()
        layout.addWidget(self.todo_form)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication([])
# importnant: open a connection BEFORE creating the windows
# later we will fetch data from DB on load - so DB needs to be open

if not open_connection():
    sys.exit(1)

window = MainWindow()
window.show()

# print(f"Database connection status: {open_connection()}")

# QSqlDatabase.close()
app.exec()