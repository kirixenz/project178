from tkinter import *
import random

root = Tk()
root.title("Project 178")
root.geometry("800x600")

label_name = Label(root, font=("Helvetica", 24), bg="white")
label_name.place(relx=0.5, rely=0.5, anchor="center")

class Game:
    def  __init__(self):
        self.__score = 0

    def updateGame(self):
        self.text = ["BLACK", "PINK", "GREEN", "BLUE", "YELLOW", "RED"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black", "pink", "green", "blue", "yellow", "red"]
        self.random_number_for_color = random.randint(0,5)   
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]

game_instance = Game()

button_start = Button(root, text="Start", command=game_instance.updateGame, bg="lightblue", fg="black", relief=FLAT, padx=10, pady=1, font=("Helvetica", 15))
button_start.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()