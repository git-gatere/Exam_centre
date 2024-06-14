import unittest
from models.invigilator import Invigilator
from models.candidate import Candidate
from models.subject import Subject

class TestModels(unittest.TestCase):
    def test_invigilator_creation(self):
        invigilator = Invigilator(id=1, name="John Doe")
        self.assertEqual(invigilator.name, "John Doe")

    def test_subject_creation(self):
        
        subject = Subject(id=1, name="Computer Science", room=309)
        self.assertEqual(subject.name, "Computer Science")

    def test_candidate_creation(self):
        invigilator = Invigilator( name="John Doe")
        subject = Subject(name="Computer Science", room=309)
        candidate = Candidate( name="Jane Doe", national_id=123456789)
        self.assertEqual(candidate.name, "Test Article")

    def test_author_articles(self):
        invigilator = Invigilator( name="John Doe")
        subject = Subject( name="Computer Science", room=309)
        candidate = Candidate( name="Jane Doe", national_id=234567890)
    

    #

if __name__ == "__main__":
    unittest.main()