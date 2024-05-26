# Jacob Heffington
# Alarm Clock/Python
# Reference: youtube.com/watch?v=no5dz0GOWy8
# Sound Effect from: fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203

from playsound import playsound
import time
import os

ALARM = os.path.dirname(__file__)+"/alarm.mp3"
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed +=1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
        
    playsound(ALARM)
        
print("Enter the amount of time to wait before the alarm sounds.")
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = (minutes * 60) + seconds
alarm(total_seconds)