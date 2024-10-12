""""
Yakuza AI Assistant - Main Codes
Author: Davood Yakuza,
Last Update: 12 oct 2024 - 21 mehr 1403
"""

from pyttsx3 import init
from datetime import datetime

engine = init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def saytime():
    #Get the current time, %I mean Hour, %M mean Minute, %S mean Second, %p mean AM/PM
    time = datetime.now().strftime("%I:%M:%S %p")

    #Speak the time message and the current time
    speak("The Current Time is: ")
    speak(time)

def saydate():
    # Get the Current date using datetime properties
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)

    #Speak the time message and the current time
    speak("Ok Sir, The Current Time is: ")
    speak(day)
    speak(month)
    speak(year)

def greeting():
    # Get the current hour
    hour = datetime.now().hour

    # Say Good Morning, Afternoon, Evening, or Night based on the current time
    if 6 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    elif 18 <= hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")




greeting()
# while True:
#     textInput = input("Say something: ")
#     speak(textInput)

# if __name__ == "__main__":
#     while True:
#         pass
