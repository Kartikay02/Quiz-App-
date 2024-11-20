import time
import random
import sqlite3
from sqlite3 import Error

# Database file path
DB_FILE = "quiz_app.db"

# Create or connect to the database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        print(f"Connected to database: {DB_FILE}")
    except Error as e:
        print(e)
    return conn

# Create tables in the database
def create_tables():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        # Create Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            enrollment TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """)
        
        # Create Questions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_answer TEXT NOT NULL
        );
        """)

        # Create Results table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            score TEXT NOT NULL,
            time_taken TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """)

        conn.commit()
        conn.close()

# Load questions from the database
def load_questions():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()
        conn.close()
        return questions
    return []

# Save a new user to the database
def register_user():
    print("\n--- Register ---")
    name = input("Enter your name: ")
    enrollment = input("Enter your enrollment number: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (name, enrollment, email, password) VALUES (?, ?, ?, ?)", 
                           (name, enrollment, email, password))
            conn.commit()
            print("Registration successful!")
        except sqlite3.IntegrityError:
            print("User with this enrollment number already exists!")
        conn.close()

# Login function
def login_user():
    print("\n--- Login ---")
    enrollment = input("Enter your enrollment number: ")
    password = input("Enter your password: ")

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE enrollment = ? AND password = ?", (enrollment, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            print("Login successful!")
            return user[0]  # Returning user ID
    print("Invalid enrollment number or password!")
    return None

# Shuffle questions and options
def shuffle_questions():
    questions = load_questions()
    shuffled_questions = []
    for q in questions:
        options = [q[2], q[3], q[4], q[5]]
        random.shuffle(options)
        shuffled_questions.append({
            "question": q[1],
            "options": options,
            "correct": q[6]
        })
    random.shuffle(shuffled_questions)
    return shuffled_questions

# Attempt quiz
def attempt_quiz(user_id):
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

    # Save the result to the database
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO results (user_id, score, time_taken) VALUES (?, ?, ?)", 
                       (user_id, score, f"{time_taken} seconds"))
        conn.commit()
        conn.close()

    print(f"\nQuiz finished! Your score: {score}")
    print(f"Time taken: {time_taken} seconds")

# View results
def view_results(user_id):
    print("\n--- Results ---")
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            print(f"Score: {result[2]}, Time: {result[3]}")
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
            user_id = login_user()
            if user_id:
                user_dashboard(user_id)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# User dashboard
def user_dashboard(user_id):
    while True:
        print("\n--- User Dashboard ---")
        print("1. Attempt Quiz")
        print("2. View Results")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            attempt_quiz(user_id)
        elif choice == '2':
            view_results(user_id)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")

# Entry point
if __name__ == "__main__":
    create_tables()  # Create tables if they don't exist
    main_menu()
