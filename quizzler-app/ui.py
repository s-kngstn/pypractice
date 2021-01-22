from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 12, "normal"),
            padx=20,
            pady=20
        )
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(
            width=300, 
            height=250, 
            highlightthickness=0, 
            bg="white"
        )
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Questions go here", 
            font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(
            image=true_img, 
            highlightthickness=0,
            command=self.true
        )
        self.true_btn.grid(
            column=0, 
            row=2,
        )

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(
            image=false_img, 
            highlightthickness=0,
            command=self.false
        )
        self.false_btn.grid(
            column=1, 
            row=2,
        )

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()    
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, 
                text="You've reached the end of the quiz."
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true(self):
        self.user_answer = "True"
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def false(self):
        self.user_answer = "False"
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)