""""
Yakuza AI Assistant - Main Codes
Author: Davood Yakuza,
Last Update: 12 oct 2024 - 21 mehr 1403
"""
from convertdate import persian
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
    monthDay = str(datetime.now().month)
    monthName = str(datetime.now().strftime("%B")) # %B mean Month Name
    day = str(datetime.now().day)

    #Speak the time message and the current time
    speak("The Current Date is: ")
    speak(day)
    speak("Month: " + monthName + " " + monthDay)
    speak("in Year: " + year)

def saydate_shamsi():
    # Get today's Gregorian date
    today = datetime.today()

    persianMonths = [
        "Farvardin", "Ordibehesht", "Khordad", "Tir",
        "Mordad", "Shahrivar", "Mehr", "Aban",
        "Azar", "Dey", "Bahman", "Esfand"
    ]
    # Convert Gregorian to Hijri Shamsi (Jalali)
    shamsi_date = persian.from_gregorian(today.year, today.month, today.day)

    # Extract the year, month number, and day
    shamsiYear, shamsiMonth, shamsiDay = shamsi_date

    # Get the month name using the month number (1-based index)
    monthName = persianMonths[shamsiMonth - 1]

    # Print the full Shamsi date with the month name
    speak("Persian Hijri Shamsi Date is: ")
    speak(str(shamsiDay))
    speak("Month: " + str(monthName) + " " + str(shamsiMonth))
    speak("in Year: " + str(shamsiYear))


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

def whishme():
    speak("Welcome back Sir!")
    saytime()
    saydate()
    saydate_shamsi()
    greeting()
    speak("YakuzaD at your Service, Please tell How can I help you?")

whishme()
# while True:
#     textInput = input("Say something: ")
#     speak(textInput)

# if __name__ == "__main__":
#     while True:
#         pass
