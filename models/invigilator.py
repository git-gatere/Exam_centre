#imports connection to database
from database.connection import get_db_connection

#creates a class Invigilator with proerties: id, name, e_mail and room
class Invigilator:
    def __init__(self, id,name, e_mail, room):
        self.id = id
        self.name = name
        self.e_mail = e_mail
        self.room = room

    @property
    def id(self):
        return self.id
    
    @property
    def name(self):
        return self.name

    @property
    def e_mail(self):
        return self.e_mail
    
    @property
    def room(self):
        return self.room

# defines a function
    def save(self):
        #calls the connection to the database
        conn = get_db_connection()
        #creates a cursor
        cursor = conn.cursor()
        #inserts the next row of values
        cursor.execute('INSERT INTO invigilators (name, e_mail, room) VALUES (?, ?, ?)', (self.name, self.e_mail, self.room))
        self._id = cursor.lastrowid 
        conn.commit()
        conn.close()


# a class method that returns the whole invigilators table
    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM invigilators')
        invigilatorsrows = cursor.fetchall()
        conn.close()
        return invigilatorsrows