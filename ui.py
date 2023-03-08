from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 10, "normal"), fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="",
            font=("Arial", 16, "italic"),
            fill=THEME_COLOR,
            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question)


