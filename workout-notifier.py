import webbrowser
import time
import pyautogui
from pytube import YouTube
from colorama import init, Fore

init()

# Replace the URL below with the YouTube video you want to open
print("\nDefault workout YouTube video: 4 Minute OFFICE STRETCHING(full body)\n")
url = input("Enter the url of a workout YouTube video (or press Enter): ")

if url == '':
        url = "https://www.youtube.com/watch?v=MTU4iCDntjs"

video = YouTube(url)

video_title = video.title
video_author = video.author

# Set the time you want the script to open the video (24-hour format)
print("\nDefault hour/minute: 14:45\n")
hour = input("Enter the hour of the day for the reminder (or press Enter): ")
minute = input("\nEnter the minute of the day for the reminder (or press Enter): ")

if hour == '':
    hour = 14
else:
    hour = int(hour)

if minute == '':
    minute = 45
else:
    minute = int(minute)
    
minute_vis = '0' + str(minute) if minute < 10 else minute

print(f"\nWorkout reminder has been set!\nYou'll watch '{Fore.GREEN}{video_title}{Fore.RESET}' \n  \
        by {Fore.RED}'{video_author}'{Fore.RESET} \n  \
        at {Fore.BLUE}{hour}:{minute_vis}{Fore.RESET}!\n  \
        Be prepared!")

while True:
    # Get the current time
    current_time = time.localtime()

    # Check if the current time matches the desired time to open the video
    if current_time.tm_hour == hour and current_time.tm_min == minute:
        # Open the URL in your default web browser
        webbrowser.open(url)
        
        time.sleep(2)
        
        pyautogui.press('f')
        
        print(f"\nYour video: '{Fore.GREEN}{video_title}{Fore.RESET}' just started!\nHave fun!")

        # Wait for 24 hours before checking the time again
        time.sleep(24 * 60 * 60)
    else:
        # Wait for 1 minute before checking the time again
        time.sleep(60)