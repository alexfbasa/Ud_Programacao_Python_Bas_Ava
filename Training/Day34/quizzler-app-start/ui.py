from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.window.title("Quizzler")

        self.score_label = Label(text="Score: 0", font=("ariel", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white")

        self.question_text = self.canvas.create_text(
            150,
            250,
            text="Something",
            fill="white",
            font=("ariel", 15, "bold")
        )
        self.canvas.grid(column=0, row=0)


        self.window.mainloop()
