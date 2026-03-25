"""SECTION A: MCQs
1. What will be the output? x = [1,2,3]
print(x * 2)
a) [1,2,3,1,2,3]
b) Error c) [2,4,6] d) None

2. What is the output? print(bool(""))
a) True
b) False
c) Error d) None

3. Which is mutable? a) tuple
b) string
c) list
d) int


4. What will be output? print(10 == 10.0)
a) True
b) False


SECTION B: Output Prediction
5.
a = [1,2,3] b=a b.append(4) print(a)

6.
def func(x=[]):
x.append(1) return x
print(func()) print(func())

7.
for i in range(5):
if i == 3: break print(i)

8. try:
print(10/0) except:
print("Error") finally:
print("Done")

SECTION C: Coding Questions

9. Write a program to:
- Take input string
- Count vowels and consonants

10. Write a program to:
- Read a file
- Count number of lines, words and characters

11. Write a program:
- Create a class BankAccount
- Methods: deposit, withdraw, check balance

12. Write a program:
- Accept list of numbers - Remove duplicates
- Sort it without using sort()

13. Write a program using lambda + map + filter: - Square only even numbers from list

SECTION D: Advanced / Thinking

14. Write a program:
- Simulate login system
- Use file to store username/password

15. Exception Handling:
- Create custom exception "InvalidAgeError" - Raise error if age < 18

SECTION E: GUI + Database Based

16. Create a Tkinter form: - Name input
- Submit button
- Show entered name

17. Python + SQL:
- Connect database
- Create table Student
- Insert 3 records
- Fetch and display all

18. Build mini project:
STUDENT MANAGEMENT SYSTEM Features:
- Add student
- View student
- Delete student
- Store data in file or database

"""

#Q1 Ans(c.[2,4,6])

#Q2 Ans(b. False)

#Q3 Ans(c. List)

#Q4 Ans(a. True)

#Q5 Ans([1,2,3,4])

#Q6 Ans([1]
#       [1, 1])

#Q7 Ans (0,
#        1,
#        2)

#Q8 Ans(Error
#       Done)

#Q9 Ans

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")


#Q10 Ans
filename = input("Enter filename: ")
with open(filename, 'r') as f:
    text = f.read()
lines = text.splitlines()
words = text.split()
print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))


#Q11 Ans
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}.")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

my_account = BankAccount(100)
my_account.check_balance()
my_account.deposit(50)
my_account.withdraw(30)
my_account.check_balance()


#Q12
nums = [4, 2, 9, 2, 1, 4, 7, 3]

unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)

n = len(unique_nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if unique_nums[j] > unique_nums[j + 1]:
            unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]

print(unique_nums)


#Q13
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)


#Q14
import os

def login_system():
    filename = "users.txt"

    def register():
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        
        with open(filename, "a") as f:
            f.write(f"{username},{password}\n")
        print("Registration successful!")

    def login():
        username = input("Username: ")
        password = input("Password: ")
        
        if not os.path.exists(filename):
            print("No users registered yet.")
            return

        with open(filename, "r") as f:
            for line in f:
                stored_user, stored_pass = line.strip().split(",")
                if stored_user == username and stored_pass == password:
                    print(f"Login successful! Welcome, {username}.")
                    return
        
        print("Invalid username or password.")

    print("--- Login System ---")
    choice = input("1. Register\n2. Login\nChoice: ")
    
    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    login_system()


#Q15
class InvalidKeyError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidKeyError("Age must be at least 18.")
    return "Access granted."

try:
    user_age = 16
    check_age(user_age)
except InvalidKeyError as e:
    print(f"Caught an error: {e}")


#Q16
import tkinter as tk

def show_name():
    entered_name = name_entry.get()
    result_label.config(text=f"Hello, {entered_name}!")

root = tk.Tk()
root.title("Name Form")
root.geometry("300x200")
root.configure(bg="lightblue")

tk.Label(root, text="Enter Name:", bg="lightblue").pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", command=show_name)
submit_btn.pack(pady=10)

result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()


 
#Q17

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="password",
    database="student_db"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    std_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

students = [
    (1, "Rahul", 20),
    (2, "Sipun", 21),
    (3, "Amit", 22)
]

cursor.executemany("INSERT INTO Student (std_id, name, age) VALUES (%s, %s, %s)", students)

conn.commit()

cursor.execute("SELECT * FROM Student")

print("Student Records:")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()


#18

import os

FILE_NAME = "students.txt"

def add_student():
    with open(FILE_NAME, "a") as file:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        file.write(f"{roll},{name},{age},{course}\n")
        print("✅ Student Added Successfully!\n")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found!\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        if not records:
            print("⚠️ No students to display!\n")
            return

        print("\n📋 Student Records:")
        print("Roll | Name | Age | Course")
        print("-" * 30)
        for line in records:
            roll, name, age, course = line.strip().split(",")
            print(f"{roll} | {name} | {age} | {course}")
        print()


def delete_student():
    roll_to_delete = input("Enter Roll No to delete: ")

    if not os.path.exists(FILE_NAME):
        print("⚠️ File not found!\n")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        found = False
        for line in lines:
            roll = line.split(",")[0]
            if roll != roll_to_delete:
                file.write(line)
            else:
                found = True

    if found:
        print("🗑️ Student Deleted Successfully!\n")
    else:
        print("❌ Student not found!\n")


def main():
    while True:
        print("===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

main()
