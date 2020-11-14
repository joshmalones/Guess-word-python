import random
import tkinter as tk

print("guess this word")

numberOne = "josh"
numberTwo = "two"
numberThree = "three"
numberFour = "four"
numberFive = "five"

guess = []

class Application(tk.Frame):
    # while guess != numberOne:
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.input = input()
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.hi_there = input("input text")

        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()