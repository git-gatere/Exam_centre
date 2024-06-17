from database.connection import get_db_connection

class Invigilator:
    def __init__(self, id, name, e_mail, room):
        self._id = id
        self._name = name
        self._e_mail = e_mail
        self._room = room

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @property
    def e_mail(self):
        return self._e_mail
    
    @property
    def room(self):
        return self._room

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO invigilators (name, e_mail, room) VALUES (?, ?, ?)', (self._name, self._e_mail, self._room))
        self._id = cursor.lastrowid 
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM invigilators')
        invigilators_rows = cursor.fetchall()
        conn.close()
        return [cls(id=row[0], name=row[1], e_mail=row[2], room=row[3]) for row in invigilators_rows]

    @classmethod
    def get_by_id(cls, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM invigilators WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1], e_mail=row[2], room=row[3])
        return None