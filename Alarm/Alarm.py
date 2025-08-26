import re
import os
import time
import datetime
import pygame


ALARM_SOUNDS = {

    "1": "alarm2.mp3", 
    "2": "alarm3.mp3",   
}


def validate_time_format(time_str):
    
    pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$"
    if not re.match(pattern, time_str):
        return False
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
        return True
    except ValueError:
        return False


def select_alarm_sound():
    print("\nAvailable alarm sounds:")
    for key, sound in ALARM_SOUNDS.items():
        print(f"{key}: {sound}")

    while True:
        choice = input("Enter the number of your chosen sound (e.g., 1, 2, ): ")
        if choice in ALARM_SOUNDS:
            selected_sound = ALARM_SOUNDS[choice]
            if not os.path.exists(selected_sound):
                print(f" Error: Sound file '{selected_sound}' not found in the current directory.")
                print("Please place the file in this folder and try again.")
                return None
            return selected_sound
        print(" Invalid choice. Please select a valid number.")



def play_alarm(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

    print("\n Alarm is ringing! WAKE UP! ")

    while pygame.mixer.music.get_busy():
        time.sleep(1)


def set_alarm(alarm_time, sound_file):

    print(f"\n Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"⏳ Current Time: {current_time}", end="\r")  # updates in place

        if current_time == alarm_time:
            play_alarm(sound_file)
            break

        time.sleep(1)


def main():

    print("=========  Python Alarm Clock ==========")

    # Ask user for alarm time
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")

    if not validate_time_format(alarm_time):
        print(" Invalid time format. Please use HH:MM:SS (e.g., 07:30:00).")
        return

    # Ask user to choose alarm sound
    sound_file = select_alarm_sound()
    if not sound_file:
        print(" Cannot proceed without a valid sound file. Exiting.")
        return

    # Start alarm countdown
    set_alarm(alarm_time, sound_file)


if __name__ == "__main__":
    main()
