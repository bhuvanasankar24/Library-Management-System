import pytest 
from datetime import datetime
from auth import register_member_with_data
from librarian import issue_book, return_book, load_books, save_books, load_loans, add_book, remove_book
from storage import Book, load_members
from unittest.mock import patch 


BOOKS_FILE = r"data\books.csv"
LOANS_FILE = r"data\loans.csv"
MEMBERS_FILE = r"data\members.csv"

def test_register_member_with_data():
    filepath = r"data\members.csv"
    members = load_members(filepath)
    
    member_id = str(max([int(m.MemberID) for m in members], default=1000) + 1)
    
    name = "Test User1"
    email = "testuser1@email.com"
    password = "Password@123"
    confirm = "Password@123"

    register_member_with_data(member_id, name, email, password, confirm)

    members = load_members(MEMBERS_FILE)
    new_member = next((m for m in  members if m.MemberID == member_id), None)
    
    assert new_member is not None 
    assert new_member.Name == name 
    assert new_member.Email == email

def test_add_book():
    books = load_books(BOOKS_FILE)
    isbn = "12345678901234"
    title = "Test BOOK"
    author = "Test Author"
    copies_total = 5
    copies_available = 5

    with patch('builtins.input', side_effect=[isbn, title, author,copies_total, copies_available]):
        add_book(isbn, title, author, copies_total, copies_available)

    books = load_books(BOOKS_FILE)
    new_book = next((b for b in books if b.ISBN == isbn), None)
    assert new_book is not None 
    assert new_book.Title == title 
    assert new_book.Author == author 

def test_remove_book():
    isbn = "1234567891234"
    with patch('builtins.input', side_effect=[isbn]):
        remove_book(isbn)

        books = load_books(BOOKS_FILE)
        removed_book = next((b for b in books if b.ISBN == isbn), None)
        assert removed_book is None

def test_issue_book():
    books = load_books(BOOKS_FILE)
    loans = load_loans(LOANS_FILE)

    isbn = "9780262033848"
    member_id = 1002

    for book in books:
        if book.ISBN == isbn:
            book.CopiesAvailable = 1
    save_books(BOOKS_FILE, books)

    initial_copies_available = next(b for b in books if b.ISBN == isbn).CopiesAvailable 

    issue_book(isbn, member_id)

    books = load_books(BOOKS_FILE)
    updated_copied_available = next(b for b in books if b.ISBN == isbn).CopiesAvailable

    assert updated_copied_available == initial_copies_available - 1 
    assert len(load_loans(LOANS_FILE)) == len(loans) + 1

def test_return_book():
    loans = load_loans(LOANS_FILE)
    
    loan = next((l for l in reversed(loans) if l.ReturnDate == ""), None)
    assert loan is not None, "No active loan available to return."
    
    isbn = loan.ISBN 
    member_id = loan.MemberID

    books = load_books(BOOKS_FILE)
    initial_copies_available = next(b for b in books if b.ISBN == isbn).CopiesAvailable

    return_book(isbn=isbn, member_id=member_id)

    loans = load_loans(LOANS_FILE)
    books = load_books(BOOKS_FILE)

    updated_copies_available = next(b for b in books if b.ISBN == isbn).CopiesAvailable
    
    updated_loan = next((l for l in loans if l.ISBN == isbn and l.MemberID == member_id and l.ReturnDate != ""), None)
    
    assert updated_copies_available == initial_copies_available + 1
    assert updated_loan is not None