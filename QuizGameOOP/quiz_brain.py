#TODO 1: asking the question
#TODO 2: checking if the answer was correct
#TODO 3: checking if we're the end of the quiz

def check_answer(user_response, correct_answer):
    return user_response.lower() == correct_answer.lower()


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number} {question.text} (True/False)?: ")

        if check_answer(response, question.answer):
            self.keep_score()
            print("This answer is correct!")
            return True
        else:
            print(f"The correct answer was: {question.answer}")
            return False

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def keep_score(self):
        self.score += 1

    def show_score(self):
        return f"{self.score}/{self.question_number}"


