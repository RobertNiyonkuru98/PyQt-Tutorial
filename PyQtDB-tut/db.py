from PyQt6.QtSql import QSqlDatabase
import os

def open_connection() -> bool:
    # An instance of QSqlDatabase represents the connection
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'todos.sqlite')
    conn = QSqlDatabase.addDatabase("QSQLITE")
    conn.setDatabaseName(db_path)
    return conn.open()
