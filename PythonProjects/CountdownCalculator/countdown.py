from tkinter import messagebox, ttk
from tkinter import * 
from datetime import *
import holidays

class MainWindow():
    def __init__ (self):
        self.holidays_lst = []
        self.us_holidays = holidays.UnitedStates()
        self.current_day = datetime.today()
        year = datetime.today().year
        self.years = [year + i for i in range(6)]
        for d,h in holidays.UnitedStates(years = self.years).items():
            if d.strftime("%Y") >= self.current_day.strftime("%Y"):
                if d.strftime("%m") >= self.current_day.strftime("%m"):
                    if d.strftime("%d") >= self.current_day.strftime("%d"):
                        if h not in self.holidays_lst:
                            if "observed" not in h.lower():
                                self.holidays_lst.append(h)
        self.main_window = Tk()
        self.main_window.config(width=300, height=200)
        self.center_screen()
        self.showDisplay()
        self.main_window.title("Countdown")
        self.main_window.mainloop()
        
    def showDisplay(self):
        # Create Years Label & Combobox and set them
        self.years_lbl = Label(self.main_window, text = "Years: ")
        self.years_combo = ttk.Combobox(
            state="readonly",
            values=self.years
        )
        self.years_lbl.place(x=40, y=30)
        self.years_combo.place(x=100, y=30)
        self.years_combo.bind("<<ComboboxSelected>>", self.showHolidays)
        self.button = ttk.Button(text="Display Countdown", command=self.display_selection)
        self.button.place(x=80, y=100)

    def showHolidays(self, event):
        self.holidays_lst.clear()
        selection = int(self.years_combo.get())
        current_year = int(self.current_day.strftime("%Y"))
        if selection == current_year:
            for d,h in holidays.UnitedStates(years = selection).items():
                if d.strftime("%Y") == self.current_day.strftime("%Y"):
                    if d.strftime("%m") >= self.current_day.strftime("%m"):
                        if d.strftime("%d") >= self.current_day.strftime("%d"):
                            if h not in self.holidays_lst:
                                if "observed" not in h.lower():
                                    self.holidays_lst.append(h)
        else:
            for d,h in holidays.UnitedStates(years = selection).items():
                if "observed" not in h.lower():
                    self.holidays_lst.append(h)
        self.holiday_lbl = Label(self.main_window, text = "Holidays: ")
        self.combo = ttk.Combobox(
            state="readonly",
            values=self.holidays_lst
        )
        self.holiday_lbl.place(x=40, y=50)
        self.combo.place(x=100, y=50)
        
    def center_screen(self):
        self.main_window.update_idletasks() 
        window_width = self.main_window.winfo_width()
        window_height = self.main_window.winfo_height()
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.main_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
    def display_selection(self):
        # Get the selected value.
        day = self.combo.get()
        year = int(self.years_combo.get())
        self.main_window.destroy()
        for d,h in holidays.UnitedStates(years = year).items():
            if day.lower() == h.lower():   
                d_day = int(d.strftime("%d"))
                m_day = int(d.strftime("%m"))
                Y_day = int(d.strftime("%Y"))
                displayCountdown = CountdownWindow(day, d_day, m_day, Y_day)
                
class CountdownWindow():
    def __init__ (self, day, d, m, Y):
        self.day = day
        self.d = d
        self.m = m
        self.Y = Y
        self.count_window = Tk()
        self.count_window.config(width=300, height=300)
        self.center_screen()
        self.count_window.title("Countdown")
        self.center_screen()
        self.showDisplay()
        self.update_countdown()
        self.count_window.mainloop()    
        
    def showDisplay(self):
        self.lbl = Label(self.count_window, text = f'Countdown until {self.day}')    
        self.lbl.place(x=50, y=30)
        self.years_lbl = Label(self.count_window, text = "")
        self.months_lbl = Label(self.count_window, text = "")
        self.days_lbl = Label(self.count_window, text = "")
        self.hours_lbl = Label(self.count_window, text = "")
        self.minutes_lbl = Label(self.count_window, text = "")
        self.seconds_lbl = Label(self.count_window, text = "")
        self.lbl.place(x=50, y=30)
        self.years_lbl.place(x=50, y=50)
        self.months_lbl.place(x=50, y=70)
        self.days_lbl.place(x=50, y=90)
        self.hours_lbl.place(x=50, y=110)
        self.minutes_lbl.place(x=50, y=130)
        self.seconds_lbl.place(x=50, y=150)    
        

    def center_screen(self):
        self.count_window.update_idletasks() 
        window_width = self.count_window.winfo_width()
        window_height = self.count_window.winfo_height()
        screen_width = self.count_window.winfo_screenwidth()
        screen_height = self.count_window.winfo_screenheight()
            # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.count_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def update_countdown(self):
        current_dateTime = datetime.now()
        year = int(current_dateTime.year)
        month = int(current_dateTime.month)
        day = int(current_dateTime.day)
        hour = int(current_dateTime.hour)
        minute = int(current_dateTime.minute)
        second = int(current_dateTime.second)
        if((year % 400 == 0) or  (year % 100 != 0) and  (year % 4 == 0)):   
            total_days = 366
        else:    
            total_days = 265
        if self.Y == year:
            years = self.Y-year
            months = self.m-month
            days = self.d-day-1
            hours = 23-hour
            minutes = 59-minute
            seconds = 60-second
        elif self.d < day:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                max_day_value = 31
            elif month == 4 or month == 6 or month == 9 or month == 11:
                max_day_value = 30
            elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                max_day_value = 29
            else:
                max_day_value = 28
            years = self.Y-year
            months = (12*years)+self.m-month
            print(max_day_value,self.d,day,1)
            days = max_day_value+self.d-day
            hours = 23-hour
            minutes = 59-minute
            seconds = 60-second
            years = 0
            if months >= 12:
                years += months//12    
                months -= 12
        else:
            years = self.Y-year
            months = (12*years)+self.m-month
            days = self.d-day-1
            hours = 23-hour
            minutes = 59-minute
            seconds = 60-second
            years = 0
            if months >= 12:
                years += months//12    
                months -= 12
        self.years_lbl.config(text=f'Years left: {years}')
        self.months_lbl.config(text=f'Months left: {months}')
        self.days_lbl.config(text=f'Days left: {days}')
        self.hours_lbl.config(text=f'Hours left: {hours}')
        self.minutes_lbl.config(text=f'Minutes left: {minutes}')
        self.seconds_lbl.config(text=f'Seconds left: {seconds}')
        self.count_window.after(1000, self.update_countdown)  # Update every 1000 milliseconds (1 second)

displayMain = MainWindow()