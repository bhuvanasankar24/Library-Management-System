📚 Library Management System (Mini Project)

A simple, console-based Library Management System built using **Python** and **CSV files**. This project is designed for educational purposes and demonstrates basic file handling, role-based login, password hashing, and test-driven development using `pytest`.

---

🚀 Features

- 👩‍💼 **Librarian Dashboard**
  - Register New Members
  - Add / Remove Books
  - Issue and Return Books
  - View Overdue List
  - Secure Logout

- 👨‍🎓 **Member Dashboard**
  - View Borrowed Books
  - Return Books

- 🔐 **Security**
  - Passwords are hashed using `bcrypt`
  - Role-based access control (Librarian vs Member)

- 🧪 **Testing**
  - Unit tests written with `pytest`
  - Separated logic for testability (`register_member_with_data()`)

---

🗃️ Project Structure

library_project/
```
│
├── data/             # Data folder for CSV storage
│ ├── books.csv       # Stores book records
│ ├── members.csv     # Stores member records
│ └── loans.csv       # Stores loan records
│
├── main.py           # Entry point for the application (menu system)
├── models.py         # Core logic for book/member/loan classes
├── librarian.py      # Functions to add, remove, issue, return, overdue
├── test_library.py   # Test cases written using pytest
├── auth.py           # Handles registration logic and password hashing
├── storage.py        # Utility functions to load/save CSV files
└── README.md         # Project documentation (you're here!)
```

---

⚙️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   
2. **Install dependencies**
   pip install bcrypt pytest
   
4. **Run the program**
    python main.py

5. **Run the test cases**
   pytest -q test_library.py

---

**Key Concepts Used**
1. Python file I/O (CSV)
2. Password hashing with bcrypt
3. Modular programming
4. Custom class structures for books, members, and loans
5. Unit testing with pytest
6. Separation of input logic from business logic

---

**Challenges Faced**

One key challenge was making register_member() testable. Initially, all user inputs were inside the function, making it difficult to automate tests. The solution was to split the function:
register_member() – accepts user inputs via terminal
register_member_with_data() – accepts direct input for testing
This refactor allowed both the main program and the test cases to work seamlessly.

---

**Future Improvements**

~ Add due-date calculations and fine system

~ Replace CSV with SQLite or PostgreSQL for better scalability

~ GUI using Tkinter or web version using Flask/Django

---

**Author**

Bhuvaneshwari S

Final Year BSc Computer Science with AI, 

LinkedIn - www.linkedin.com/in/bhuvana-sankar, 

Mail - bhuvanaasankar241@gmail.com  

---

This project is for educational purposes. You can use and modify it freely.
