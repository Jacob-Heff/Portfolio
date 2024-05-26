from tkinter import messagebox, ttk
from tkinter import *
import random
import os
import sys
import psutil
import logging

class MainWindow():
    def __init__ (self):
        self.questions = []
        self.questions_to_choose_from = []
        self.options_lst = []
        self.results_lst = []
        self.outcomes_lst = []
        self.pullInformation()
        self.master = Tk()
        self.master.geometry("350x400")
        self.centerScreen()
        self.itemFrame()
        self.questionFrame()
        self.submitFrame()
        self.resultsFrame()
        self.quitFrame()
        # Separator object
        ttk.Separator(self.master, orient=HORIZONTAL).grid(row=1,column=0, columnspan=3, ipadx=100, sticky="ew") 
        self.master.mainloop()
      
    def pullInformation(self):
        file = r"C:\Users\heffi\source\repos\Jacob-Heff\PythonProjects\CHYOA\assets\q&a.txt"
        with open(file) as f:
            for i, line in enumerate(f):
                if(i%4 == 0):
                    line = line.strip()
                    li = tuple(line.split(":"))
                    self.questions.append(li[1])
                    self.questions_to_choose_from.append(li[1])
                if(i%4==1):
                    line = line.strip()
                    li = line.strip("Options: ")
                    options = li.split(" / ")
                    self.options_lst.append(options)
                if(i%4 == 2):
                    line = line.strip()
                    li = line.strip("Results: ")
                    results = li.split(" / ")
                    self.results_lst.append(results)
                if(i%4 == 3):
                    line = line.strip()
                    li = line.strip("Outcomes :")
                    outcomes = li.split("/")
                    self.outcomes_lst.append(outcomes)
                    
    def itemFrame(self):
        self.item_frame = Frame(self.master)
        self.item_frame.grid(row = 0, column = 0)
        # Column 1
        self.coins = PhotoImage(file = r"C:\Users\heffi\source\repos\Jacob-Heff\PythonProjects\CHYOA\assets\coins.png")
        self.coins = self.coins.subsample(100)
        self.coins_total = 0
        Label(self.item_frame, image = self.coins).grid(row = 0, column = 0, padx = 5, pady = 5)
        Label(self.item_frame, text = "Coins").grid(row = 1, column = 0, padx = 5, pady = 5)
        self.coins_lbl = Label(self.item_frame, text = self.coins_total)
        self.coins_lbl.grid(row = 2, column = 0, padx = 5, pady = 5)
        # Column 2
        self.mp = PhotoImage(file = r"C:\Users\heffi\source\repos\Jacob-Heff\PythonProjects\CHYOA\assets\potion.png")
        self.mp = self.mp.subsample(200)
        Label(self.item_frame, image = self.mp).grid(row = 0, column = 1, padx = 5, pady = 5)
        Label(self.item_frame, text = "Magic Points").grid(row = 1, column = 1, padx = 5, pady = 5)
        self.mp_total = 0
        self.mp_lbl = Label(self.item_frame, text = self.mp_total)
        self.mp_lbl.grid(row = 2, column = 1, padx = 5, pady = 5)
        # Column 3
        self.img1 = PhotoImage(file = r"C:\Users\heffi\source\repos\Jacob-Heff\PythonProjects\CHYOA\assets\coins.png")
        self.img1 = self.img1.subsample(100)
        Label(self.item_frame, image = self.img1).grid(row = 0, column = 2, padx = 5, pady = 5)
        Label(self.item_frame, text = "Coins").grid(row = 1, column = 2, padx = 5, pady = 5)
        Label(self.item_frame, text = "0").grid(row = 2, column = 2, padx = 5, pady = 5)
        # Column 4
        self.img2 = PhotoImage(file = r"C:\Users\heffi\source\repos\Jacob-Heff\PythonProjects\CHYOA\assets\coins.png")
        self.img2 = self.img2.subsample(100)
        Label(self.item_frame, image = self.img2).grid(row = 0, column = 3, padx = 5, pady = 5)
        Label(self.item_frame, text = "Coins").grid(row = 1, column = 3, padx = 5, pady = 5)
        Label(self.item_frame, text = "0").grid(row = 2, column = 3, padx = 5, pady = 5)
        # Column 5
        self.img3 = PhotoImage(file = r"C:\Users\heffi\source\repos\Jacob-Heff\PythonProjects\CHYOA\assets\coins.png")
        self.img3 = self.img3.subsample(100)
        Label(self.item_frame, image = self.img3).grid(row = 0, column = 4, padx = 5, pady = 5)
        Label(self.item_frame, text = "Coins").grid(row = 1, column = 4, padx = 5, pady = 5)
        Label(self.item_frame, text = "0").grid(row = 2, column = 4, padx = 5, pady = 5)

    def questionFrame(self):
        self.question_frame = Frame(self.master)
        self.question_frame.grid(row = 2, column = 0)
        self.question_lbl = Label(self.question_frame, text = self.questionPicker(), wraplength=300)
        self.question_lbl.grid(row=0,column=1)
    
    def submitFrame(self):
        self.submit_frame = Frame(self.master)
        self.submit_frame.grid(row = 4, column = 0)
        self.submit_btn = ttk.Button(self.submit_frame, text ="Submit", command = self.displayResults)
        self.submit_btn.grid(row=0,column=1)
        self.answerFrame()
        
    def questionPicker(self):
        question = random.choice(self.questions_to_choose_from)
        self.question = question
        del self.questions_to_choose_from[self.questions_to_choose_from.index(question)]
        self.question_index = self.questions.index(self.question)
        return question
        
    def answerFrame(self):
        self.answer_lst = []
        answers = self.options_lst[self.question_index]
        self.answer_lst = answers
        self.answer_frame = Frame(self.master)
        self.answer_frame.grid(row = 3, column = 0)
        self.combo_lbl = Label(self.answer_frame, text = "Pick an option: ").grid(row=0,column=0)
        self.combo = ttk.Combobox(self.answer_frame, width= 40, state="readonly", values=self.answer_lst)
        self.combo.grid(row=0,column=1)
        
    def resultsFrame(self):
        self.result_frame = Frame(self.master)
        self.result_lbl = Label(self.result_frame, text = "", wraplength=300)
        self.result_lbl.grid(row=0,column=1)
        
    def centerScreen(self):
        self.master.update_idletasks() 
        self.window_width = self.master.winfo_width()
        self.window_height = self.master.winfo_height()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (self.window_width/2))
        y_cordinate = int((screen_height/2) - (self.window_height/2))
        self.master.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))
        
    def updateQuestion(self):
        self.combo.set("")
        self.question_lbl.configure(text = self.questionPicker())
        answers = self.options_lst[self.questions.index(self.question)]
        self.answer_lst = answers
        self.combo.configure(values=self.answer_lst)
        
    def updateResults(self):
        result = self.results_lst[self.question_index]
        final_result = result[self.answer_lst.index(self.selection)]
        self.result_frame.grid(row = 2, column = 0)
        self.results_sep = ttk.Separator(self.master, orient=HORIZONTAL)
        self.results_sep.grid(row=3,column=0, columnspan=3, ipadx=100, sticky="ew") 
        self.question_frame.grid(row = 4, column = 0)
        self.answer_frame.grid(row = 5, column = 0)
        self.submit_frame.grid(row = 6, column = 0)
        self.result_lbl.configure(text = final_result)
        self.result_lbl.grid(row=0,column=1)
        
    def updateResources(self):
        operators = ["+", "-", "*"]
        benefits = self.outcomes_lst[self.question_index]
        print(benefits)
        print(self.selection)
        print(self.answer_lst)
        benefits_lst = benefits[self.answer_lst.index(self.selection)]
        final_benefits = benefits_lst.split(", ")
        for final_benefit in final_benefits:
            print(final_benefit.lower())
            if "coin" in final_benefit.lower():
                for operator in operators:
                    if operator in final_benefit.lower():
                        expr = str(self.coins_total) + " " + operator + " " + str(final_benefit.split(operator,1)[1])
                        self.coins_total = eval(expr)
                        self.coins_lbl.configure(text = self.coins_total)
            if "mp" in final_benefit.lower():
                for operator in operators:
                    if operator in final_benefit.lower():
                        expr = str(self.mp_total) + " " + operator + " " + str(final_benefit.split(operator,1)[1])
                        self.mp_total = eval(expr)
                        self.mp_lbl.configure(text = self.mp_total)
            if "end" in final_benefit.lower():
                return "end"  

    def displayResults(self):
        # Get the selected value.
        self.selection = self.combo.get()
        if self.selection in self.answer_lst:
            self.updateResults()
            end = self.updateResources()
            if end == "end":
                self.endFrame()
                return None
            self.master.update()
            self.updateQuestion()
        else:
            pass
        
    def endFrame(self):
        self.question_frame.destroy()
        self.answer_frame.destroy()
        self.submit_frame.destroy()
        self.end_frame = Frame(self.master)
        self.end_frame.grid(row = 4, column = 0)
        Label(self.end_frame, text = "Game Over!").grid(row = 0, column = 1)
        ttk.Button(self.end_frame, text ="Restart", command = self.restartProgram).grid(row = 1, column = 1)
    
    def quitFrame(self):
        self.quit_frame = Frame(self.master)
        ttk.Button(self.quit_frame, text ="Quit", command = self.quitProgram).grid(row = 0, column = 1)
        self.quit_frame.grid(row = 10, column = 0)

    def restartProgram(self):
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        import os
        os.execv(sys.executable, ['python3'] + sys.argv)
        
    def quitProgram(self):
        quit()
        

displayMain = MainWindow()