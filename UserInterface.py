from tkinter import *


class MyFirstGUI:
    def __init__(self, master):


        self.master = master

        self.input = None

        master.title("Logging Progress")

        # self.label = Label(master, text="This is our first GUI!")
        # self.label.pack()


        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        #self.entry.config( height = 10, width = 10 )
        self.entry.grid(row=0, column=0)
        self.entry.config(bg='#BDBBDF', font=('times', 18, 'italic'))
        self.entry.pack(side="top", fill=BOTH, padx=30, pady=30, ipadx = 10, ipady = 10)
        # msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        # msg.bind('<Motion>',motion)
        # msg.pack()
        self.greet_button = Button(master, text="Submit", command=self.submit)
        self.greet_button.config( height = 2, width = 10 )
        #self.greet_button.grid(row=2, column=0)
        self.greet_button.config(bg='white', font=('times', 18, 'italic'))
        self.greet_button.pack(side="top", fill=BOTH, padx=30, pady=30)
        master.bind('<Return>', self.returnFunc)
        #self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.config( height = 2, width = 10 )
        #self.greet_button.grid(row=2, column=0)
        self.close_button.config(bg='white', font=('times', 18, 'italic'))
        self.close_button.pack(side="top", fill=BOTH, padx=30, pady=30)


    def returnFunc(self, other):
        logChange(self.input)

    def submit(self):
        logChange(self.input)


    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.input = None
            return True
        try:
            input = new_text
            self.input = input
            return True
        except ValueError:
            return False


def logChange(newText):
    print(newText)
    # insert submit code
    print("Submmited!")

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500")
    root.resizable(0, 0)
    root.configure(background='#DFBBCB')
    center(root)

    my_gui = MyFirstGUI(root)
    
    #whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do"
    #msg = Message(root, text = whatever_you_do)
    # msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    # msg.bind('<Motion>',motion)
    # msg.pack()

    root.mainloop()


# import random
# from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

# class GuessingGame:
#     def __init__(self, master):
#         self.master = master
#         master.title("Guessing Game")

#         self.secret_number = random.randint(1, 100)
#         self.guess = None
#         self.num_guesses = 0

#         self.message = "Guess a number from 1 to 100"
#         self.label_text = StringVar()
#         self.label_text.set(self.message)
#         self.label = Label(master, textvariable=self.label_text)

#         vcmd = master.register(self.validate) # we have to wrap the command
#         self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

#         self.guess_button = Button(master, text="Guess", command=self.guess_number)
#         self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)

#         self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
#         self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
#         self.guess_button.grid(row=2, column=0)
#         self.reset_button.grid(row=2, column=1)

#     def validate(self, new_text):
#         if not new_text: # the field is being cleared
#             self.guess = None
#             return True

#         try:
#             guess = int(new_text)
#             if 1 <= guess <= 100:
#                 self.guess = guess
#                 return True
#             else:
#                 return False
#         except ValueError:
#             return False

#     def guess_number(self):
#         self.num_guesses += 1

#         if self.guess is None:
#             self.message = "Guess a number from 1 to 100"

#         elif self.guess == self.secret_number:
#             suffix = '' if self.num_guesses == 1 else 'es'
#             self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
#             self.guess_button.configure(state=DISABLED)
#             self.reset_button.configure(state=NORMAL)

#         elif self.guess < self.secret_number:
#             self.message = "Too low! Guess again!"
#         else:
#             self.message = "Too high! Guess again!"

#         self.label_text.set(self.message)

#     def reset(self):
#         self.entry.delete(0, END)
#         self.secret_number = random.randint(1, 100)
#         self.guess = 0
#         self.num_guesses = 0

#         self.message = "Guess a number from 1 to 100"
#         self.label_text.set(self.message)

#         self.guess_button.configure(state=NORMAL)
#         self.reset_button.configure(state=DISABLED)

# root = Tk()
# my_gui = GuessingGame(root)
# root.mainloop()