import time
import datetime
import winsound

def display_time():
    
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def set_alarm(alarm_time):
    
    print(f"Alarm set for {alarm_time}. Waiting...")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("\nALARM! Wake up!\n")
            for _ in range(5):  
                winsound.Beep(1000, 500)  
                time.sleep(1)
            break
        time.sleep(30)  


if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM format): ")
    set_alarm(alarm_time)
