# Quiz-App 

1.Quiz App data saved in program memory


Overview
This project is a console-based Quiz Application built in Python. The application
allows users to register, log in, attempt a quiz, and view their results. All data
(users, questions, and results) is stored in memory during program execution,
ensuring simplicity and speed.

Features
1. User Registration:
• Users can register by providing their name, enrollment number, email,
and password.
2. User Login:
• Users log in using their enrollment number and password.
3. Quiz Attempt:
Users can take a quiz that consists of multiple-choice questions.
Questions and their options are dynamically shuffled each time the quiz
is attempted.
The quiz calculates the total score and the time taken.
4. View Results:
• Users can view their quiz scores and the time taken for completion.
5. In-Memory Data Management
• Data is managed entirely in memory, with no reliance on external files.

Prerequisites:
Python 3.x installed on your system.

How to Run
1.Download/Clone the Code:
• Save the script as quiz_app.py or any name you prefer.
2.Execute the Program:
python quiz_app. py
3.Follow On-Screen Instructions:
• Choose options to register, log in, take the quiz, or view results.
Copy code

How the Quiz Works
1. Quiz Questions:
• The quiz consists of predefined questions with multiple-choice answers.
• The correct answer is stored alongside each question.
2. Shuffled Options:
Questions and their options are shuffled dynamically for every quiz
attempt.
3. Scoring:
• Each correct answer scores 1 point.
• Final results include the total score and time taken.

Quiz Questions
The following are the questions included in the application:
1.What is the capital of Japan?,Tokyo,Beijing,Seoul,Bangkok,Tokyo
2.What is 12 x 8?,80,92,96,88,96
3.Which gas do plants absorb from the atmosphere?,Oxygen,Nitrogen,Carbon Dioxide,Hydrogen,Carbon Dioxide
4.Who wrote the play 'Romeo and Juliet'?,Charles Dickens,Mark Twain,William Shakespeare,J.K. Rowling,William Shakespeare
5.What is the boiling point of water at sea level (in °C)?,90,100,110,120,100
6.Who painted the Mona Lisa?,Vincent van Gogh,Pablo Picasso,Leonardo da Vinci,Claude Monet,Leonardo da Vinci
7.What is the chemical symbol for Gold?,Go,Ag,Au,Pt,Au
8.Which planet is known as the Red Planet?,Venus,Mars,Jupiter,Saturn,Mars

Answers :
Tokyo
96
Carbon Dioxide
William Shakespeare
100
Leonardo da Vinci 
Au
Mars

Code Structure
# Main Functions:
register_user : Handles user registration.
login_user : Authenticates users.
shuffle_questions : Shuffles questions and options for each quiz attempt.
attenpt_quiz : Facilitates the quiz-taking process.
view_results : Displays the user's score and time taken.
main ænu : Provides the main interface for user interactions.
# Data Structures:
users : List storing user details (name, enrollment, email, password).
questions : List of dictionaries containing quiz questions, options, and answers.
results : Dictionary storing scores and times keyed by user enrollment.

# Future Enhancements:
Add persistent storage using files or a database.
Include support for multiple quizzes or categories.
Add a graphical user interface (GUD for better usability.
Implement a timer for each question to increase difficulty.

This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the
terms of the license.


Contributors
Kumar Kartikay
Feel free to contribute to this project by improving its features or fixing any issues!














