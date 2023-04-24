class LGOEnvironment:

    def __init__(self,
                 q_question,
                 q_answer):
        self.question = q_question
        self.answer = q_answer

    def __str__(self):
        return f"{self.question} {self.answer}"
