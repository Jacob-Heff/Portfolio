import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title('Digital Clock')

window_height = 300
window_width = 300

def center_screen():
    """ gets the coordinates of the center of the screen """
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

center_screen()

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)
    
# Create a label to display the time
clock_label = tk.Label(root, text="", font=("Helvetica", 48))
clock_label.pack(padx=20, pady=20)
# Start updating the time
update_time()
# Start the Tkinter event loop
root.mainloop()
