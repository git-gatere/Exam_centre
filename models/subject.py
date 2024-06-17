from database.connection import get_db_connection

class Subject:
    all = []
    
    def __init__(self, id, name, room):
        self._id = id
        self._name = name
        self._room = room
        Subject.all.append(self)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def room(self):
        return self._room

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO subjects (name, room) VALUES (?, ?)', (self._name, self._room))
        self._id = cursor.lastrowid 
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM subjects')
        subjects_rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], room=row[2]) for row in subjects_rows]

    @classmethod
    def get_by_id(cls, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM subjects WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1], room=row[2])
        return None