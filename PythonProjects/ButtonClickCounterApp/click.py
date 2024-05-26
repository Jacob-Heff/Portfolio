from tkinter import *
import time
import random

class First():
    def __init__(self):
        self.root = Tk()
        self.w = 30 # width for the Tk root
        self.h = 300 # height for the Tk root

        # get screen width and height
        self.ws = self.root.winfo_screenwidth() # width of the screen
        self.hs = self.root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.root.title("Button Clicker")
        #Initialize a Label to display the User Input
        self.label= Label(self.root, text="Pick a Number")
        self.label.place(x=110, y=0)

        #Create an Entry widget to accept User Input
        self.entry = Entry(self.root, width= 10)
        self.entry.focus_set()
        self.entry.place(x=0,y=80)

        #Create a Button to validate Entry Widget
        self.button = Button(self.root, text= "Okay", width= 80, command= self.close).place(x=110,y=200)
    def close(self):
        self.root.destroy()
        return self.entry


class Clicker():
    def __init__(self, number):
        self.root = Tk()
        w = 300 # width for the Tk root
        h = 100 # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.title("Button Clicker")
        self.number = 0
        self.ClickingButton = Button(self.root,text="Click Me!", command=self.ClickButton)
        self.ShowInfo = Label(self.root, text=f'You Clicked {self.number} times.')
        self.ClickingButton.place(x=40,y=20)
        self.ShowInfo.place(x=20,y=80)
    def ClickButton(self):
        self.number += 1
        self.ShowInfo.configure(text=f'You Clicked {self.number} times.')
        self.ClickingButton.place(x=random.randint(0, 200), y=random.randint(0,20))
        if self.number == 10:
            self.root.destroy()
            
class Last():
    def __init__(self, time):
        self.root = Tk()
        self.w = 300 # width for the Tk root
        self.h = 100 # height for the Tk root

        # get screen width and height
        self.ws = self.root.winfo_screenwidth() # width of the screen
        self.hs = self.root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.root.title("Button Clicker")
        self.ShowInfo = Label(self.root, text=f'You Clicked 10 times in {time} seconds.')
        self.ShowInfo.place(x=20,y=80)

start_time = time.time()
end_time = time.time()
total_time = round(end_time - start_time, 2)

while True:
    first = First()
    first.root.mainloop
    break

while True:
    app = Clicker(first)
    app.root.mainloop()
    break

end_time = time.time()
total_time = round(end_time - start_time, 2)

while True: 
    last = Last(total_time)
    last.root.mainloop()
    break