from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
quiz_brain = QuizBrain(question_bank)

for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

while quiz_brain.still_has_question():
    quiz_brain.next_question()


print(f"You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}.")
