import webbrowser
import time
import pyautogui
from pytube import YouTube
from colorama import init, Fore

init()      # Initializing colorama 

print("\nDefault workout YouTube video: 4 Minute OFFICE STRETCHING(full body)\n")
url = input("Enter the url of a workout YouTube video (or press Enter): ")

if url == '':
        url = "https://www.youtube.com/watch?v=MTU4iCDntjs"     # If the user doesn't give a url (Hits Enter)
else:
    if not url.startswith('https'):                             # If the url doesn't start with 'https', we add it.
        url = 'https://www.' + url
        
if not url.__contains__('youtube'):                             # If the url isn't about a YouTube video, program exits.
    print(f"\nThat's {Fore.RED}not a YouTube video url{Fore.RESET}.\
        \nNext time please give the {Fore.GREEN}correct url{Fore.RESET}.\
        \nExiting...")
    exit(1)

video = YouTube(url)                # We make a YouTube video object, to use its info

video_title = video.title           # YouTube video's title
video_author = video.author         # YouTube video's creator

# In this section we set the time we want the script to open the video (24-hour format)
print("\nDefault hour/minute: 14:45\n")
hour = input("Enter the hour of the day for the reminder (or press Enter): ")
minute = input("\nEnter the minute of the day for the reminder (or press Enter): ")

if hour == '':              # If no hour given, default is 14
    hour = 14
else:
    hour = int(hour)        # otherwise we typecast it to int

if minute == '':            # If no minute given, default is 45
    minute = 45
else:
    minute = int(minute)    # otherwise we typecast it to int
    
minute_vis = '0' + str(minute) if minute < 10 else minute   # If the minute is between 0 and 9, we want to print 00 - 09

print(f"\nWorkout reminder has been set!\nYou'll watch '{Fore.GREEN}{video_title}{Fore.RESET}' \n  \
        by {Fore.RED}'{video_author}'{Fore.RESET} \n  \
        at {Fore.BLUE}{hour}:{minute_vis}{Fore.RESET}!\n  \
        Be prepared!")

while True:
    # We get the current time
    current_time = time.localtime()

    # If the current time is equal to the desired time, we open the YouTube video
    if current_time.tm_hour == hour and current_time.tm_min == minute:
        
        webbrowser.open(url)        # Opening the URL in the default web browser
        
        time.sleep(2)               # Waiting 2 seconds to load the video
        
        pyautogui.press('f')        # Pressing 'f' key, to get into fullscreen
        
        print(f"\nYour video: '{Fore.GREEN}{video_title}{Fore.RESET}' just started!\nHave fun!")

        time.sleep(24 * 60 * 60)    # Waiting exactly 24 hours, to check the time again
    else:
        time.sleep(60)              # Checking the time every 60 seconds