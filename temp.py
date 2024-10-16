from speech_recognition import Recognizer, Microphone

def take_cmd_mic():
    """This function takes the command from the user's microphone and returns it as text using Whisper."""
    
    # Initialize recognizer
    recognize = Recognizer()
    
    # Load Whisper model size (e.g., "tiny", "base", "small", "medium", "large")
    whisper_model_name = "base"  # Change the model as needed
    
    # Capture audio from the microphone
    with Microphone() as source:
        print("Start Listening...")
        
        # Adjust for ambient noise to improve clarity
        recognize.adjust_for_ambient_noise(source, duration=0.5)
        recognize.pause_threshold = 1  # You can adjust this if needed

        # Start listening to the microphone
        audio = recognize.listen(source)

    try:
        print("Start Recognizing...")
        
        # Recognize speech using the Whisper model
        audioCmd = recognize.recognize_google_cloud(audio, language="en-IN")

        # Print the recognized text
        print("You said:", audioCmd)
        return audioCmd
    except Exception as e:
        print("Error:", e)
        print("Say that again please...")

    # except Exception as e:
    #     print("Error:", e)
    #     return "None"
    

take_cmd_mic()