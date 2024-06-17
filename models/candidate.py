
#imports the connection to the database
import sys
import os
from database.connection import get_db_connection 
from subject import *
from invigilator import *


#creates a class called Candidates with attributes name, national_id, e_mail, subject and invigilator
class Candidate:
    def __init__(self,name, national_id,e_mail,subject,invigilator):
        self.name = name
        self.national_id = national_id
        self.e_mail = e_mail
# checks whether the value passed in for subject is actually an instance of the class Subject and returns an error if it is not
        if isinstance (subject, Subject):
            self.subject = subject
        else:
            ValueError("Subject not found!")
        
# checks whether the value passed in for invigilator is actually an instance of the class Invigilator and returns an error if it is not
        if isinstance(invigilator, Invigilator):
            self.invigilator = invigilator
        else:
            ValueError("Invigilator not found!")
   
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
        cursor.execute('INSERT INTO candidates (name, national_id, e_mail, subject, invigilator) VALUES (?, ?, ?, ?, ?)',
                       (self.name, self.national_id, self.e_mail, self.subject, self.invigilator))
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
    