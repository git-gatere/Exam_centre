
from database.connection import get_db_connection 

class Candidate:
    def __init__(self,name, national_id,e_mail,subject,invigilator):
        self.name = name
        self.national_id = national_id
        self.e_mail = e_mail
        self.subject = subject
        self.invigilator = invigilatorconn = get_db_connection()
   
    @property
    def name(self):
        return self.name

    @property
    def national_id(self):
        return self.national_id

    @property
    def invigilator(self):
        return self.invigilator

    @property
    def e_mail(self):
        return self.e_mail

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO candidates (name, national_id, invigilator_id, subject_id) VALUES (?, ?, ?, ?)',
                       (self.name, self.national_id, self.invigilator.id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM candidates')
        candidates = cursor.fetchall()
        conn.close()
        return candidates
    
