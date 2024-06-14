
from database.connection import get_db_connection

class Invigilator:
    def __init__(self, id,name, national_id, e_mail, room):
        self.id = id
        self.name = name
        self.national_id = national_id
        self.e_mail = e_mail
        self.room = room

    @property
    def id(self):
        return self.id
    
    @property
    def name(self):
        return self.name
    
    @property
    def national_id(self):
        return self.national_id
    
    @property
    def e_mail(self):
        return self.e_mail
    
    @property
    def room(self):
        return self.room


    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO invigilators (name) VALUES (?)', (self.name,))
        self._id = cursor.lastrowid 
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM invigilators')
        authors = cursor.fetchall()
        conn.close()
        return authors