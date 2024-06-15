import sqlite3
from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # cursor = get_db_connection().cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invigilators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            e_mail TEXT, 
            room INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            room TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            national_id INTEGER NOT NULL,
            e_mail TEXT NOT NULL,
            subject_id INTEGER,
            invigilator_id INTEGER,
            FOREIGN KEY (invigilator_id) REFERENCES invigilators (id),
            FOREIGN KEY (subject_id) REFERENCES subjects (id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()