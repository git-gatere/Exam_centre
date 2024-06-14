from database.setup import create_tables
from models.candidate import Candidate
from models.invigilator import Invigilator
from models.subject import Subject



def initialize():
    print("creating tables ...")
    create_tables()
    print("Tables created successfully")


def display_menu():
    print("1. Add Candidate:")
    print("2. Add Subject")
    print("3. Add invigillator")
    print("3. Display Candidate")
    print("4. Display Subject")
    print("5. ")

# def main():
#     create_tables()

    
#     invigilator_name = input("Enter invigilator's name: ")
#     subject_name = input("Enter subject name: ")
#     subject_room = input("Enter your subject room: ")
#     candidate_name = input("Enter the candidate's name: ")
#     candidate_national_id = input("Enter the candidate's national identification number : ")

    
#     invigilator = Invigilator(name=invigilator_name)
#     invigilator.save()

    
#     subject = Subject(name=subject_name, room=subject_room)
#     subject.save()

    
#     candidate = Candidate(name=candidate_name, national_id=candidate_national_id, invigilator=invigilator_name, subject=subject_name)
#     candidate.save()

    
#     subjects = Subject.get_all()
#     print("\nMagazines:")
#     for sub in subjects:
#         print(sub)

    
#     invigilators = Invigilator.get_all()
#     print("\nInvigilators:")
#     for invg in invigilators:
#         print(invg)

    
#     candidates = Candidate.get_all()""
#     print("\nCandidates:")
#     for cand in candidates:
#         print(cand)


