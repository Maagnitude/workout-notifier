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
video_length = video.length         # YouTube video's length-duration

video_minutes = video_length // 60
video_seconds = video_length % 60

# We get the current time
current_time = time.localtime()

# In this section we set the time we want the script to open the video (24-hour format)
print("\nDefault hour/minute: 15:50\n")
hour = input("Enter the hour of the day for the reminder (or press Enter): ")
minute = input("\nEnter the minute of the day for the reminder (or press Enter): ")

if hour == '':              # If no hour given, default is 15
    hour = 15
else:
    hour = int(hour)        # otherwise we typecast it to int

if minute == '':            # If no minute given, default is 50
    minute = 50
else:
    minute = int(minute)    # otherwise we typecast it to int
    
minute_vis = '0' + str(minute) if minute < 10 else minute   # If the minute is between 0 and 9, we want to print 00 - 09

print(f"\nWorkout reminder has been set!\nYou'll watch '{Fore.GREEN}{video_title}{Fore.RESET}' \n  \
        by {Fore.RED}'{video_author}'{Fore.RESET} \n  \
        at {Fore.BLUE}{hour}:{minute_vis}:{time.localtime().tm_sec if time.localtime().tm_sec>9 else '0'+str(time.localtime().tm_sec)}{Fore.RESET}!\n  \
        Be prepared to dedicate {Fore.GREEN}{video_minutes} minutes and {video_seconds} seconds{Fore.RESET} of your time!")

while True:
    # We get the current time again to work inside the loop
    current_time = time.localtime()

    # If the current time is equal to the desired time, we open the YouTube video
    if current_time.tm_hour == hour and current_time.tm_min == minute:
        
        webbrowser.open(url)        # Opening the URL in the default web browser
        
        time.sleep(4)               # Waiting 4 seconds to load the video
        
        pyautogui.press('f')        # Pressing 'f' key, to get into fullscreen
        
        print(f"\nYour video: '{Fore.GREEN}{video_title}{Fore.RESET}' just started!\nHave fun!")
        
        time.sleep(video_length)
        
        pyautogui.hotkey('ctrl', 'w')   # Closing the tab
        
        print(f"\nVideo-Workout ended! Tab closed!\nNext workout same time tomorrow! Have a good day!\n")

        time.sleep(24 * 60 * 60 - video_length)    # Waiting exactly 24 hours minus the length of the video, to check the time again
    else:
        time.sleep(60)              # Checking the time every 60 seconds