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
    #Get the current time, %I is Hour, %M is Minute, %S is Second, %p is AM/PM
    time = datetime.now().strftime("%I:%M:%S %p")
    speak("The Current Time is: ")
    speak(time)

saytime()
# while True:
#     textInput = input("Say something: ")
#     speak(textInput)
