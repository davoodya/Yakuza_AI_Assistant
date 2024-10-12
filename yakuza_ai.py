""""
Yakuza AI Assistant - Main Codes
Author: Davood Yakuza,
Last Update: 12 oct 2024 - 21 mehr 1403
"""

from convertdate import persian
from pyttsx3 import init
from datetime import datetime

from speech_recognition import Recognizer, Microphone


# Create a text-to-speech engine
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

def getvoices(voice):
    voices = engine.getProperty('voices')

    if voice == 1:
        # voices[0].id => Male Voice
        engine.setProperty('voice', voices[0].id)
        speak("Hello Sir, this is Yakuza D Ai Assistant")
    elif voice == 2:
        # voices[0].id => Female Voice
        engine.setProperty('voice', voices[1].id)
        speak("Hi Sir, this is Yakuza D on Friday Mode")


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

def whishme(persian_date=False):
    speak("Welcome back Sir!")
    saytime()

    if persian_date:
        saydate_shamsi()
    else:
        saydate()

    greeting()
    speak("Yakuza-D at your Service, Please tell How can I help you?")

def take_cmd_text():
    """this function takes the command from the user input and returns it"""
    command = input("please tell me how can i help you?\n")
    return command

def take_cmd_mic():
    """this function takes the command from the user Microphone and returns it as text"""
    recognize = Recognizer()
    whisperModelName = "turbo"
    with Microphone() as source:
        print("Start Listening...")
        # Set noise reduction and pause threshold to have a clear voice
        recognize.adjust_for_ambient_noise(source, duration=0.5)
        recognize.pause_threshold = 1

        # Start listening to the user voice
        audio = recognize.listen(source)

    try:
        print("Start Recognizing...")
        # audioCmd: str | Any = "this test"

        # Convert audio to text using Google Cloud
        # TODO : 1. add feature to recognize voice using Whisper Models
        #        2.add feature to recognize voice in persian language
        #audioCmd = recognize.recognize_whisper(audio, model=whisperModelName)
        audioCmd = recognize.recognize_google_cloud(audio, language="fa-IR")
        print("You said => ", audioCmd, sep="\n")

    except Exception as e:
        print("Error: ", e)
        speak("Say that again please...")
        return "None"
    return audioCmd


#getvoices(2)

if __name__ == "__main__":
    #whishme(persian_date=True)
    while True:
        # for index, name in enumerate(Microphone.list_microphone_names()):
        #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        cmd = take_cmd_mic().lower()
        print(cmd)
        if "time" in cmd:
            saytime()
        elif "date" in cmd:
            saydate()
        elif "persian" in cmd:
            saydate_shamsi()
