from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
# https://opentdb.com/
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
# current_question = question_bank[question_number = 0]
# current_question = self.question_list[self.question_number]
# self.question_number += 1
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was:{quiz.score}/{quiz.question_number}.")
