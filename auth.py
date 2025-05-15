import csv 
import bcrypt 
from datetime import date 
from models import Member
from storage import load_members

MEMBERS_FILE = r"data\members.csv"
session = {}

def register_member_with_data(member_id, name, email, password, confirm):
    filepath= r"data\members.csv"
    members = load_members(filepath)
   
    if any(m.MemberID == member_id for m in members):
        print("Duplicate Member ID found.")
        return 

    if password != confirm:
        print("Passwords do not match!")
        return 
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

    with open(filepath, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['MemberID'] == member_id:
                print("ID already Exists.")
                return 
    
    with open(filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([member_id, name, hashed_pw, email, date.today()])
        print("Member registered successfully.")

def register_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    confirm = input("Confirm Password: ")
    register_member_with_data(member_id, name, email, password, confirm)

def login(filepath, role):
    user_id = input("Enter your ID: ")
    password = input("Enter your Password: ")

    with open(filepath, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if role == "member" and row['MemberID'] == user_id:
                if bcrypt.checkpw(password.encode(), row['PasswordHash'].encode()):
                    print(f"Welcome {row['Name']}!")
                    session['user'] = row
                    session['role'] = 'member'
                    return True 
                else:
                    print("Incorrect password.")
                    return False 
            elif role == "librarian" and user_id == "admin" and bcrypt.checkpw(password.encode(), row['PasswordHash'].encode()):
                print("Welcome back Librarian!")
                session['user'] = {'MemberID': 'admin', 'Name': 'Librarian'}
                session['role'] = 'librarian'
                return True 
    print("Login failed. user not found.")
    return False