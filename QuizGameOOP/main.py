import data
from question_model import Question
from data import *
from quiz_brain import *

print("Welcome to the quiz :)")
category = input("What type of category would you like to choose?: (Animals/General "
                 "knowledge/Sports/Mythology/Geography) ").lower()

question_bank = []
list_of_questions = data.choose_category(category)
for q in list_of_questions["results"]:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    question_bank.append(Question(question_text, question_answer))


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    if not quiz_brain.next_question():
        print("You've finished the quiz.")
        print("Your final score was: " + quiz_brain.show_score())
        break
    print("Score: " + quiz_brain.show_score())
    print("\n")



