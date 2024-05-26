# Jacob Heffington
# Quiz Game
# Resource: github.com/techwithtim/5-Python-Projects-For-Beginners

import random
import os

PATH = os.path.dirname(__file__)
TOTAL_QUESTIONS = 9

def selectQuestions():
    # Read questions from the text file
    with open(PATH+'/questions.txt', 'r') as file:
        questions = file.read().splitlines()

    # Read answers from the text file
    with open(PATH+'/answers.txt', 'r') as file:
        answers = file.read().splitlines()

    # Create a list of tuples, each containing a question and its answer
    quiz_data = list(zip(questions, answers))
    
    # Randomly select TOTAL_QUESTIONS questions for the quiz
    selected_questions = random.sample(quiz_data, TOTAL_QUESTIONS)

    return selected_questions

def playQuiz(questions):
    score = 0
    
    for i, (question, answer) in enumerate(questions, start=1):
        user_answer = input(f"{i}. {question} ")
        
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}\n")
    
    print(f"Quiz completed! Your score: {score}/{TOTAL_QUESTIONS} | {int((score/TOTAL_QUESTIONS)*100)}%.")


print("Welcome to my computer quiz!")

# Get randomly selected questions
selected_questions = selectQuestions()

# Play the quiz with the selected questions
playQuiz(selected_questions)