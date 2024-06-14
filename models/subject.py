
from database.connection import get_db_connection

class Subject:
    # rooms = [301, 302, 303, 304, 305, 306, 307, 308]
    # subjects = ["Mathematics", "English", "Physics", "Chemistry", "Biology", "Computer", "Art", "Music"]
    # subject_candidates = []
    all = []
    
    def __init__(self, id, name, room):
        self.id = id
        self.name = name
        self.room = room
        Subject.all.append(self)

    
    # @classmethod
    # def create_instances(cls):

    #     for index, subject in enumerate(cls.subjects):
    #         subject = cls(subject, cls.rooms[index])



    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self.name

    @property
    def room(self):
        return self.room

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO subjects (name, room) VALUES (?, ?)', (self.name, self.room))
        self._id = cursor.lastrowid 
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM subjects')
        subjects = cursor.fetchall()
        conn.close()
        return subjects
    
# Subject.create_instances()