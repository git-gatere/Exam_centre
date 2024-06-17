

from database.setup import create_tables
from models.candidate import Candidate
from models.invigilator import Invigilator
from models.subject import Subject

def initialize():
    print("Creating tables ...")
    create_tables()
    print("Tables created successfully")

def add_candidate():
    name = input("Enter candidate name: ")
    national_id = input("Enter candidate national ID: ")
    e_mail = input("Enter candidate email: ")
    
    # Display available subjects
    subjects = Subject.get_all()
    print("Available Subjects:")
    for idx, subject in enumerate(subjects):
        print(f"{idx+1}. {subject.name} (Room: {subject.room})")
    subject_choice = int(input("Choose a subject by number: "))
    subject = subjects[subject_choice - 1]

    # Display available invigilators
    invigilators = Invigilator.get_all()
    print("Available Invigilators:")
    for idx, invigilator in enumerate(invigilators):
        print(f"{idx+1}. {invigilator.name} (Room: {invigilator.room})")
    invigilator_choice = int(input("Choose an invigilator by number: "))
    invigilator = invigilators[invigilator_choice - 1]

    candidate = Candidate(name=name, national_id=national_id, e_mail=e_mail, subject=subject, invigilator=invigilator)
    candidate.save()
    print("Candidate added successfully")

def add_subject():
    name = input("Enter subject name: ")
    room = input("Enter subject room: ")
    subject = Subject(id=None, name=name, room=room)
    subject.save()
    print("Subject added successfully")

def add_invigilator():
    name = input("Enter invigilator name: ")
    e_mail = input("Enter invigilator email: ")
    room = input("Enter invigilator room: ")
    invigilator = Invigilator(id=None, name=name, e_mail=e_mail, room=room)
    invigilator.save()
    print("Invigilator added successfully")

def display_candidates():
    candidates = Candidate.get_all()
    if not candidates:
        print("No candidates found")
        return

    for candidate in candidates:
        print(f"Name: {candidate.name}, National ID: {candidate.national_id}, Email: {candidate.e_mail}, Subject: {candidate.subject.name}, Invigilator: {candidate.invigilator.name}")

def display_subjects():
    subjects = Subject.get_all()
    if not subjects:
        print("No subjects found")
        return

    for subject in subjects:
        print(f"Name: {subject.name}, Room: {subject.room}")

def display_invigilators():
    invigilators = Invigilator.get_all()
    if not invigilators:
        print("No invigilators found")
        return

    for invigilator in invigilators:
        print(f"Name: {invigilator.name}, Email: {invigilator.e_mail}, Room: {invigilator.room}")

def display_menu():
    print("1. Add Candidate")
    print("2. Add Subject")
    print("3. Add Invigilator")
    print("4. Display Candidates")
    print("5. Display Subjects")
    print("6. Display Invigilators")
    print("7. Exit")

def main():
    initialize()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_candidate()
        elif choice == '2':
            add_subject()
        elif choice == '3':
            add_invigilator()
        elif choice == '4':
            display_candidates()
        elif choice == '5':
            display_subjects()
        elif choice == '6':
            display_invigilators()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()