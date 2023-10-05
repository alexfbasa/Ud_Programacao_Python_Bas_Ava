from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text="Some Question Text",
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=0, columnspan=2, pady=50)

        self.right_img = PhotoImage(file="images/true.png")
        self.cross_img = PhotoImage(file="images/false.png")

        self.right_button = Button(image=self.right_img)
        self.right_button.grid(column=0, row=2)

        self.false_button = Button(image=self.cross_img)
        self.false_button.grid(column=1, row=2)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=f"{q_text}")
