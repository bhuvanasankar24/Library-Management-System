from librarian import add_book, remove_book, issue_book, return_book, show_overdue, MEMBERS_FILE
from auth import register_member
from storage import load_members, load_books, load_loans
from models import Member, Book, Loan

def librarian_menu():
    while True:
        print("\n=== Librarian Dashboard ===")
        print("1. Register member")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. View Overdue List")
        print("7. Logout")
        choice = input("> ")

        if choice == "1":
            register_member()
        elif choice == "2":
            add_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            show_overdue()
        elif choice == "7":
            print("Logged Out.")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    librarian_menu()