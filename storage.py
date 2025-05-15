import csv 
from models import Book, Member, Loan 

def load_books(filepath):
    books = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(Book(
                ISBN=row['ISBN'],
                Title=row['Title'],
                Author=row['Author'],
                CopiesTotal=int(row['CopiesTotal']),
                CopiesAvailable=int(row['CopiesAvailable'])
            ))
    return books 

def save_books(filepath, books):
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Book.__annotations__.keys())  # Use fieldnames correctly
        writer.writeheader()
        for book in books:
            writer.writerow(book.__dict__)

def load_members(filepath):
    members = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            member_data = {
                'MemberID': row['MemberID'],
                'Name': row['Name'],
                'PasswordHash': row['PasswordHash'],
                'Email': row['Email'],
                'JoinDate': row['JoinDate']
            }
            members.append(Member(**member_data))
    return members 

def save_members(filepath, members):
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Member.__annotations__.keys())
        writer.writeheader()
        for member in members:
            writer.writerow(member.__dict__)

def load_loans(filepath):
    loans=[]
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            loans.append(Loan(**row))
    return loans

def save_loans(filepath, loans):
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Loan.__annotations__.keys())
        writer.writeheader()
        for loan in loans:
            writer.writerow(loan.__dict__)