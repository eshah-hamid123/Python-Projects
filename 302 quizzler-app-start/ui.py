from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=50, bg=THEME_COLOR)
        self.label = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR, font=('Calibri', 20, "normal"))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,width=280, text=f"Some question text", fill=THEME_COLOR,  font=('Arial', 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.get_next_question()

        self.cross_image = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, command=self.work_button_cross)
        self.cross_button.grid(row=2, column=1)

        self.tick_image = PhotoImage(file="./images/true.png")
        self.tick_button = Button(image=self.tick_image, highlightthickness=0, pady=50, command=self.work_button_tick)
        self.tick_button.grid(row=2, column=0)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text=f'You have reached end of quiz.Your final score is {self.quiz.score}')
            self.cross_button.config(state='disabled')
            self.tick_button.config(state='disabled')



    def work_button_cross(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def work_button_tick(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def give_feedback(self, status):
        if status:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


