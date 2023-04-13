import webbrowser
import time
import keyboard
import pyautogui
from pytube import YouTube
from colorama import init, Fore
from win10toast import ToastNotifier

init()                      # Initializing colorama 
toaster = ToastNotifier()   # Initializing the notifier

two_pack = input("Do you want 2 different videos with 3 hours difference? (y/N)")

two_pack = True if two_pack.lower().__contains__('y') else False

print("\nDefault workout YouTube video: 4 Minute OFFICE STRETCHING(full body)")
url = input("Enter the url of a workout YouTube video (or press Enter): ")

if url == '':
    url = "https://www.youtube.com/watch?v=MTU4iCDntjs"         # If the user doesn't give a url (Hits Enter)
else:
    if not url.startswith('https'):                             # If the url doesn't start with 'https', we add it.
        url = 'https://www.' + url
        
if not url.__contains__('youtube'):                             # If the url isn't about a YouTube video, program exits.
    print(f"\nFirst url is {Fore.RED}not a YouTube video url{Fore.RESET}.\
        \nNext time please give the {Fore.GREEN}correct url{Fore.RESET}.\
        \nExiting...")
    exit(1)
    
video = YouTube(url)                # We make a YouTube video object, to use its info

video_title = video.title           # YouTube video's title
video_author = video.author         # YouTube video's creator
video_length = video.length         # YouTube video's length-duration

video_minutes = video_length // 60
video_seconds = video_length % 60

if two_pack:
    sec_url = input("Enter the url for the second video: (or press Enter to leave the default)")

    if sec_url == '':
        sec_url = "https://www.youtube.com/watch?v=MTU4iCDntjs"
    else:
        if not sec_url.startswith('https'):
            sec_url = 'https://www.' + sec_url
            
    if not sec_url.__contains__('youtube'):                             
        print(f"\nSecond url is {Fore.RED}not a YouTube video url{Fore.RESET}.\
            \nNext time please give the {Fore.GREEN}correct url{Fore.RESET}.\
            \nExiting...")
        exit(1)

    video2 = YouTube(sec_url)           # We make a second YouTube video object, to use its info

    video2_title = video2.title         # Second YouTube video's title
    video2_author = video2.author       # Second YouTube video's creator
    video2_length = video2.length       # Second YouTube video's length-duration

    video2_minutes = video2_length // 60
    video2_seconds = video2_length % 60


# In this section we set the time we want the script to open the video (24-hour format)
print("\nDefault hour/minute: 15:50 for the first video and 17:50 for the second, if selected.\n")
hour = input("Enter the hour of the day for the reminder (or press Enter): ")
minute = input("\nEnter the minute of the hour for the reminder (or press Enter): ")

if hour == '':              # If no hour given, default is 15
    hour = 15
    hour2 = 17
else:
    hour = int(hour)        # otherwise we typecast it to int
    hour2 = (int(hour) + 2) % 24

if minute == '':            # If no minute given, default is 50
    minute = 50
    minute2 = 50
else:
    minute = int(minute)    # otherwise we typecast it to int
    minute2 = int(minute)
    
minute_vis = '0' + str(minute) if minute < 10 else minute   # If the minute is between 0 and 9, we want to print 00 - 09

cur_seconds = time.localtime().tm_sec

time_scheduled_in_sec = hour * 60 * 60 + minute * 60 + cur_seconds

print(f"\nWorkout reminder has been set!\nYou'll watch '{Fore.GREEN}{video_title}{Fore.RESET}' \n  \
        by {Fore.RED}'{video_author}'{Fore.RESET} \n  \
        at {Fore.BLUE}{hour}:{minute_vis}:{time.localtime().tm_sec if cur_seconds>9 else '0'+str(cur_seconds)}{Fore.RESET}!\n  \
        Be prepared to dedicate {Fore.GREEN}{video_minutes} minutes and {video_seconds} seconds{Fore.RESET} of your time!")

while True:
    # We get the current time again to work inside the loop
    current_time = time.localtime()

    # If the current time is equal to the desired time, we open the YouTube video
    if current_time.tm_hour == hour and current_time.tm_min == minute:
        
        webbrowser.open(url)        # Opening the URL in the default web browser
        
        time_started_in_sec = time.localtime().tm_hour * 60 * 60 + time.localtime().tm_min * 60 + time.localtime().tm_sec
        
        time.sleep(4)               # Waiting 4 seconds to load the video
        
        pyautogui.press('f')        # Pressing 'f' key, to get into fullscreen
        
        print(f"\nYour video: '{Fore.GREEN}{video_title}{Fore.RESET}' just started!\nHave fun!")
        
        toaster.show_toast("Workout started!", "If you want to cancel it, press 'Ctrl + W'! Have fun!", duration=5)
        
        closed = False
        while True:
            if (keyboard.is_pressed('ctrl') and keyboard.is_pressed('w')):
                time_closed_in_sec = time.localtime().tm_hour * 60 * 60 + time.localtime().tm_min * 60 + time.localtime().tm_sec
                time_played_in_sec = abs(time_closed_in_sec - time_started_in_sec)
                closed = True
                break
            current_time_playing = time.localtime().tm_hour * 60 * 60 + time.localtime().tm_min * 60 + time.localtime().tm_sec
            if current_time_playing - time_started_in_sec == video_length:
                time_played_in_sec = video_length
                break
                
        if closed == False:
            pyautogui.hotkey('ctrl', 'w')   # Closing the tab
        
        if two_pack:
            toaster.show_toast("Second workout!", "First workout ended, get ready for the second one in 2 hours from now!", duration=10)
            print(f"\nFirst workout ended, get ready for the second one in 2 hours from now!\n")
            time.sleep(2 * 60 * 60 - time_played_in_sec)    # Waiting exactly 2 hours for the next video to be played
        else:
            toaster.show_toast("Workout ended!", "Tab closed! See you again tomorrow!", duration=5)
            print(f"\nVideo-Workout ended! Tab closed!\nNext workout same time tomorrow! Have a good day!\n")
            time.sleep(24 * 60 * 60 - time_played_in_sec)    # Waiting exactly 24 hours minus the length of the video, to check the time again
            continue
 
    elif current_time.tm_hour == hour2 and current_time.tm_min == minute2 and two_pack:
        
        webbrowser.open(sec_url)        # Opening the URL in the default web browser
        
        time_started_in_sec_2 = time.localtime().tm_hour * 60 * 60 + time.localtime().tm_min * 60 + time.localtime().tm_sec
        
        time.sleep(4)               # Waiting 4 seconds to load the video
        
        pyautogui.press('f')        # Pressing 'f' key, to get into fullscreen
        
        print(f"\nYour video: '{Fore.GREEN}{video2_title}{Fore.RESET}' just started!\nHave fun!")
        
        toaster.show_toast("Workout started!", "If you want to cancel it, press 'Ctrl + W'! Have fun!", duration=5)
        
        closed = False
        while True:
            if (keyboard.is_pressed('ctrl') and keyboard.is_pressed('w')):
                time_closed_in_sec = time.localtime().tm_hour * 60 * 60 + time.localtime().tm_min * 60 + time.localtime().tm_sec
                time_played_in_sec = abs(time_closed_in_sec - time_started_in_sec)
                closed = True
                break
            current_time_playing = time.localtime().tm_hour * 60 * 60 + time.localtime().tm_min * 60 + time.localtime().tm_sec
            if current_time_playing - time_started_in_sec == video2_length:
                time_played_in_sec = video2_length
                break
                
        if closed == False:
            pyautogui.hotkey('ctrl', 'w')   # Closing the tab
            
        toaster.show_toast("Workout ended!", "Tab closed! See you again tomorrow!", duration=5)
        print(f"\nVideo-Workout ended! Tab closed!\nNext workout same time tomorrow! Have a good day!\n")

        time.sleep(22 * 60 * 60 - time_played_in_sec)    # Waiting exactly 22 hours minus the length of the video, to check the time again 
    else:
        time.sleep(60)              # Checking the time every 60 seconds