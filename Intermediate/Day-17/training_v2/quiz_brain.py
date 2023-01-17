class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q:{self.question_number}: {current_question.text} is (True/False)?")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def check_answer(self, user_guess, right_answer):
        if user_guess.lower() == right_answer.lower():
            self.score += 1
            print(f"You got it right. Your current score is {self.score}/{len(self.question_list)}")
        else:
            print(f"That's wrong! ")
        print(f'The correct answer was {right_answer}')
