from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# empty list created
questions_bank = []
'''
for question in question_data

question_data = [
      question["question"]                              
    {"question": "The Neanderthals were a direct ancestor of modern humans.",
      question["correct_answer"]
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean",
     "difficulty": "medium", "question": "Super Mario Bros. was released in 1990.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
'''
for question in question_data:
    question_text = question["question"]
    # "The Neanderthals were a direct ancestor of modern humans." - 0
    question_answer = question["correct_answer"]
    # "False" - 0
    new_question = Question(question_text, question_answer)
    # new_question = Question("The Neanderthals were a direct ancestor of modern humans." , "False")
    questions_bank.append(new_question)
    # print(questions_bank[0].question)
    # print(questions_bank[0].correct_answer)

quiz = QuizBrain(questions_bank)
while quiz.still_has_question():
    quiz.next_question()