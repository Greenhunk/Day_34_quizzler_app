from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Tanvir's quize game")
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg= "white", bg= THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(150, 125, width=280, text="question", font= ("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50 )

        self.image_right = PhotoImage(file="/Users/Md.Tanvir.Hasan@lut.fi/Downloads/quizzler-app-start/images/true.png")
        self.button_right = Button(image=self.image_right, highlightthickness=0, command= self.check_if_right)
        self.button_right.grid(row=2, column=0)
        self.image_wrong = PhotoImage(file="/Users/Md.Tanvir.Hasan@lut.fi/Downloads/quizzler-app-start/images/false.png")
        self.button_wrong = Button(image=self.image_wrong, highlightthickness=0, command=self.check_if_wrong)
        self.button_wrong.grid(row=2, column=1)

        self.get_next_question()






        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text = "The quiz has ended")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def check_if_right(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_if_wrong(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)








