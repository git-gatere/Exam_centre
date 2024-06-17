from database.connection import get_db_connection

class Subject:
    # rooms = [301, 302, 303, 304, 305, 306, 307, 308]
    # subjects = ["Mathematics", "English", "Physics", "Chemistry", "Biology", "Computer", "Art", "Music"]
    all = []

    
    def __init__(self, id, name, room):
        self._id = id
        self._name = name
        self._room = room
        Subject.all.append(self)


    # @classmethod
    # def create_instances(cls):

    #      for index, subject in enumerate(cls.subjects):
    #        subject = cls(subject, cls.rooms[index])

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
    def create_test_data(cls):
        rooms = [301, 302, 303, 304, 305, 306, 307, 308]
        subjects = ["Mathematics", "English", "Physics", "Chemistry", "Biology", "Computer", "Art", "Music"]

        for room, subject in zip(rooms, subjects):
            subj = cls(id=None, name=subject, room=room)
            subj.save()
        print("Test data created successfully")
    
    create_test_data()
    