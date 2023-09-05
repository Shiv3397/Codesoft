import tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

questions = [
    Question("What color is the sky?", ["Red", "Blue", "Green", "Yellow"], "Blue"),
    Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    Question("Which planet is known as the 'Red Planet'?", ["Mars", "Jupiter", "Venus", "Saturn"], "Mars"),
    Question("Which Animal is known as the 'Singham'?", ["Cheetah", "Leopard", "Hedgehog", "Lion"], "Lion")
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")
        self.root.configure(background="#20232a")

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", fg="white", bg="#20232a", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i), font=("Arial", 14))
            self.option_buttons.append(button)
            button.pack(pady=10, padx=20, fill=tk.X)

        self.next_question()

    def next_question(self):
        if self.current_question < len(questions):
            question = questions[self.current_question]
            self.question_label.config(text=question.prompt)

            options = question.options.copy()
            random.shuffle(options)

            for i in range(4):
                self.option_buttons[i].config(text=options[i], bg="#282c34", fg="white")

            self.current_question += 1
        else:
            messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(questions)}")
            self.root.destroy()

    def check_answer(self, selected_option):
        question = questions[self.current_question - 1]
        selected_option_text = self.option_buttons[selected_option].cget("text")

        if selected_option_text == question.correct_answer:
            self.score += 1

        self.next_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
