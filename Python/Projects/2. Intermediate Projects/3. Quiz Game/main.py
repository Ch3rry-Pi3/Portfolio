"""
Quiz Game

This program runs a simple True/False quiz using Object-Oriented Programming (OOP).
The quiz is structured as follows:
- A list of predefined questions and answers.
- A `Question` class to model each question.
- A `QuizBrain` class to handle game logic.
- A loop that iterates through the quiz until all questions are answered.
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initialize the question bank
question_bank = [
    Question(question["text"], question["answer"]) for question in question_data
]

# Create an instance of QuizBrain with the list of questions
quiz = QuizBrain(question_bank)

# Main quiz loop
while quiz.still_has_questions():
    quiz.next_question()

# Final message and score display
print("\nThanks for completing the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
