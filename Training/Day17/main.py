from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
quiz_brain = QuizBrain(question_bank)

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

while quiz_brain.is_still_question():
    quiz_brain.next_question()


