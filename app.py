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

def main():
    initialize()
    display_menu()

if __name__ == "__main__":
    main()