import time
import random
import os

# Data in memory
users = []
questions = [
    {"question": "What is the capital of Japan?", "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"], "correct": "Tokyo"},
    {"question": "What is 12 x 8?", "options": ["80", "92", "96", "88"], "correct": "96"},
    {"question": "Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "correct": "Carbon Dioxide"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "J.K. Rowling"], "correct": "William Shakespeare"},
    {"question": "What is the boiling point of water at sea level (in °C)?", "options": ["90", "100", "110", "120"], "correct": "100"},
    {"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "correct": "Leonardo da Vinci"},
    {"question": "What is the chemical symbol for Gold?", "options": ["Go", "Ag", "Au", "Pt"], "correct": "Au"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "correct": "Mars"}
]
results = {}

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
