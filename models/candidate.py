from database.connection import get_db_connection
from models.subject import Subject
from models.invigilator import Invigilator

class Candidate:
    def __init__(self, name, national_id, e_mail, subject, invigilator):
        self._name = name
        self._national_id = national_id
        self._e_mail = e_mail

        if isinstance(subject, Subject):
            self._subject = subject
        else:
            raise Exception("Subject not found!")
        
        if isinstance(invigilator, Invigilator):
            self._invigilator = invigilator
        else:
            raise Exception("Invigilator not found!")
   
    @property
    def name(self):
        return self._name

    @property
    def national_id(self):
        return self._national_id

    @property
    def e_mail(self):
        return self._e_mail

    @property
    def subject(self):
        return self._subject

    @property
    def invigilator(self):
        return self._invigilator

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO candidates (name, national_id, e_mail, subject_id, invigilator_id) VALUES (?, ?, ?, ?, ?)',
            (self._name, self._national_id, self._e_mail, self._subject.id, self._invigilator.id)
        )
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM candidates')
        candidates_rows = cursor.fetchall()
        conn.close()
        return [cls(name=row[1], national_id=row[2], e_mail=row[3], subject=Subject.get_by_id(row[4]), invigilator=Invigilator.get_by_id(row[5])) for row in candidates_rows]