from storage import load_books, save_books, load_loans, save_loans, load_members
from auth import session
from models import Book, Loan
import csv 
from datetime import datetime, timedelta

BOOKS_FILE = r"data\books.csv"
LOANS_FILE = r"data\loans.csv"
MEMBERS_FILE = r"data\members.csv"

def add_book(isbn = None, title=None, author=None, copies_total=None, copies_available=None):
    books = load_books(BOOKS_FILE)
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")

    try:
        copies_total = int(input("Total Copies: "))
        copies_available = int(input("Enter Available Copies: "))

        if copies_total < 0 or copies_available < 0:
            print("Copies cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid number for copies.")
        return

    for book in books:
        if book.ISBN == isbn:
            print("Book with this ISBN already exists.")
            return

    new_book = Book(isbn, title, author, copies_total, copies_available)
    books.append(new_book)

    save_books(BOOKS_FILE, books)

    print(f"Book '{title}' added successfully.")

def remove_book(isbn = None):
    isbn = input("Enter ISBN to remove: ")
    books = load_books(BOOKS_FILE)
    books = [b for b in books if b.ISBN != isbn]
    save_books(BOOKS_FILE, books)
    print("Book removed.")

def issue_book(isbn=None, member_id=None):
    books = load_books(BOOKS_FILE)
    loans = load_loans(LOANS_FILE)

    if isbn is None:
        isbn = input("Enter ISBN to issue: ")
    if member_id is None:
        member_id = input("Member ID: ")
    
    book = next((b for b in books if b.ISBN == isbn), None)
    if not book:
        print("Book not found.")
        return 
    if book.CopiesAvailable < 1:
        print("No copies available.")
        return 
    
    book.CopiesAvailable -= 1
    loan_id = max([int(l.LoanID) for l in loans], default=0) + 1
    issue_date = datetime.today()
    due_date = issue_date + timedelta(days=14)

    new_loan = Loan(
        LoanID=str(loan_id),
        MemberID=member_id,
        ISBN=isbn,
        IssueDate=issue_date.strftime("%Y-%m-%d"),
        DueDate=due_date.strftime("%Y-%m-%d"),
        ReturnDate=""
    )
    loans.append(new_loan)

    save_books(BOOKS_FILE, books)
    save_loans(LOANS_FILE, loans)
    print(f" Book issued. Due on {due_date.strftime('%d-%b-%Y')}.")

def return_book(isbn=None, member_id=None):
    books = load_books(BOOKS_FILE)
    loans = load_loans(LOANS_FILE)

    if isbn is None:
        isbn = input("Enter ISBN to return: ")
    if member_id is None:
        member_id = input("Member ID: ")

    loan = next((l for l in loans if l.ISBN == isbn and l.MemberID == member_id and l.ReturnDate == ""), None)
    if not loan:
        print("No active loan found for this book and member.")
        return 
    loan.ReturnDate = datetime.today().strftime("%Y-%m-%d")

    book = next((b for b in books if b.ISBN == isbn), None)
    if book:
        book.CopiesAvailable += 1
    save_loans(LOANS_FILE, loans)
    save_books(BOOKS_FILE, books)
    print("Book returned successfully.")

def show_overdue():
    loans = load_loans(LOANS_FILE)
    members = load_members(MEMBERS_FILE)
    books = load_books(BOOKS_FILE)

    today = datetime.today().date()
    found = False 

    print("\n Overdue Books: ")
    print("-" * 70)
    print(f"{'LoanID': <8} {'Member': <20}{'Book Title': <25}{'DueDate': <10}")
    print("-" * 70)

    for loan in loans:
        if loan.ReturnDate == "" and datetime.strptime(loan.DueDate, "%Y-%m-%d").date() < today:
            member = next((m for m in members if m.MemberID == loan.MemberID), None)
            book = next((b for b in books if b.ISBN == loan.ISBN), None)
            if member and book:
                print(f"{loan.LoanID:<8}{member.Name:<20}{book.Title:<25}{loan.DueDate:<10}")
                found = True

    if not found:
        print("No overdue books today.")
