import time
import random
import os
import json

# File paths
USERS_FILE = "users.json"
RESULTS_FILE = "results.json"
QUESTIONS_FILE = "questions.json"

# Load users from file
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save users to file
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

# Load results from file
def load_results():
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save results to file
def save_results(results):
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f)

# Load questions from file
def load_questions():
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, 'r') as f:
            return json.load(f)
    return []

# Sample questions (if no file exists)
default_questions = [
    {"question": "Which of the following is not a primitive data type in Java?", "options": ["int", "char", "String", "boolean"], "correct": "String"},
    {"question": "What does the 'self' keyword represent in Python?", "options": ["A reference to the class", "A reference to the instance", "A reference to the parent class", "A reference to the current function"], "correct": "A reference to the instance"},
    {"question": "Which of the following SQL statements is used to retrieve data from a database?", "options": ["INSERT", "SELECT", "DELETE", "UPDATE"], "correct": "SELECT"},
    {"question": "Which of these is a valid Python comment?", "options": ["// This is a comment", "# This is a comment", "/ This is a comment", "<!-- This is a comment -->"], "correct": "# This is a comment"},
    {"question": "Which method in Java is used to start a thread?", "options": ["run()", "start()", "execute()", "init()"], "correct": "start()"},
    {"question": "What does DBMS stand for?", "options": ["Database Management System", "Data Bank Management System", "Database Model System", "Data Binary Management System"], "correct": "Database Management System"},
    {"question": "What is the correct syntax for creating a dictionary in Python?", "options": ["dict = {}", "dict = []", "dict = ()", "dict = ''"], "correct": "dict = {}"},
    {"question": "Which of the following is used to declare a constant in Java?", "options": ["final", "constant", "const", "immutable"], "correct": "final"},
    {"question": "Which keyword is used in Python to create a function?", "options": ["func", "define", "function", "def"], "correct": "def"},
    {"question": "Which of the following SQL clauses is used to filter records?", "options": ["WHERE", "SELECT", "FROM", "GROUP BY"], "correct": "WHERE"},
    {"question": "Which of these methods is used to add an element to a list in Python?", "options": ["add()", "insert()", "append()", "push()"], "correct": "append()"},
    {"question": "What is the default value of a boolean variable in Java?", "options": ["0", "false", "true", "null"], "correct": "false"},
    {"question": "In SQL, which command is used to remove a table?", "options": ["DELETE", "DROP", "REMOVE", "TRUNCATE"], "correct": "DROP"},
    {"question": "Which of these is used to handle exceptions in Java?", "options": ["try-catch", "throw-throw", "exception-catch", "if-else"], "correct": "try-catch"},
    {"question": "Which data type does the 'input()' function return in Python?", "options": ["str", "int", "list", "bool"], "correct": "str"},
    {"question": "What does the 'public' access modifier in Java mean?", "options": ["The class or method is accessible from anywhere", "The class or method is accessible only within the class", "The class or method is accessible only within the package", "The class or method is accessible only in its subclass"], "correct": "The class or method is accessible from anywhere"},
    {"question": "Which of the following SQL commands is used to update data in a table?", "options": ["MODIFY", "UPDATE", "ALTER", "CHANGE"], "correct": "UPDATE"},
    {"question": "Which data type can store multiple values in Python?", "options": ["int", "list", "char", "string"], "correct": "list"},
    {"question": "What is the return type of the 'main' method in Java?", "options": ["void", "int", "String", "boolean"], "correct": "void"},
    {"question": "Which of the following is used to execute an SQL query in Python?", "options": ["execute_query()", "cursor.execute()", "query.execute()", "db.execute()"], "correct": "cursor.execute()"}
]

# Save default questions if no file exists
def save_default_questions():
    with open(QUESTIONS_FILE, 'w') as f:
        json.dump(default_questions, f)

# Load users
users = load_users()
# Load results
results = load_results()
# Load questions
questions = load_questions()

if not questions:
    save_default_questions()
    questions = default_questions

# Registration function
def register_user():
    print("\n--- Register ---")
    name = input("Enter your name: ")
    enrollment = input("Enter your enrollment number: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user["enrollment"] == enrollment:
            print("User with this enrollment number already exists!")
            return

    users.append({"name": name, "enrollment": enrollment, "email": email, "password": password})
    save_users(users)
    print("Registration successful!")

# Login function
def login_user():
    print("\n--- Login ---")
    enrollment = input("Enter your enrollment number: ")
    password = input("Enter your password: ")

    for user in users:
        if user["enrollment"] == enrollment and user["password"] == password:
            print("Login successful!")
            return enrollment

    print("Invalid enrollment number or password!")
    return None

# Shuffle questions and options
def shuffle_questions():
    shuffled_questions = []
    for q in questions:
        shuffled_options = q["options"][:]
        random.shuffle(shuffled_options)
        shuffled_questions.append({
            "question": q["question"],
            "options": shuffled_options,
            "correct": q["correct"]
        })
    random.shuffle(shuffled_questions)
    return shuffled_questions

# Attempt quiz
def attempt_quiz(enrollment):
    print("\n--- Quiz ---")
    shuffled_questions = shuffle_questions()
    correct_answers = 0
    total_questions = len(shuffled_questions)
    start_time = time.time()

    for idx, q in enumerate(shuffled_questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")
        try:
            answer = int(input("Your answer (1-4): ")) - 1
            if q['options'][answer] == q['correct']:
                correct_answers += 1
        except (ValueError, IndexError):
            print("Invalid input! Skipping question.")

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    score = f"{correct_answers}/{total_questions}"
    results[enrollment] = {"score": score, "time_taken": f"{time_taken} seconds"}
    save_results(results)

    print(f"\nQuiz finished! Your score: {score}")
    print(f"Time taken: {time_taken} seconds")

# View results
def view_results(enrollment):
    print("\n--- Results ---")
    if enrollment in results:
        result = results[enrollment]
        print(f"Score: {result['score']}, Time: {result['time_taken']}")
    else:
        print("No results found!")

# Main menu
def main_menu():
    while True:
        print("\n--- Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            enrollment = login_user()
            if enrollment:
                user_dashboard(enrollment)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# User dashboard
def user_dashboard(enrollment):
    while True:
        print("\n--- User Dashboard ---")
        print("1. Attempt Quiz")
        print("2. View Results")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            attempt_quiz(enrollment)
        elif choice == '2':
            view_results(enrollment)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")

# Entry point
if __name__ == "__main__":
    main_menu()
