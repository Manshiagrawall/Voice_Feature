import speech_recognition as sr
import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Flag to control voice input functionality
voice_input_active = True

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_to_voice():
    global voice_input_active

    if voice_input_active:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Please enter your phone number.")
            print("Listening...")
            audio = recognizer.listen(source)

            try:
                phone_number = recognizer.recognize_google(audio)
                print(f"You said: {phone_number}")
                voice_input_active = False  # Disable voice input after number is entered
                return phone_number
            except sr.UnknownValueError:
                speak("Sorry, I did not understand that.")
                return None
            except sr.RequestError:
                speak("Could not request results from Google Speech Recognition service.")
                return None
    return None  # If voice input is disabled or an error occurred

def login_with_voice():
    phone_number = listen_to_voice()
    if phone_number:
        speak(f"You entered: {phone_number}. Logging in...")
        # Add your login logic here
    # If phone_number is None, do nothing (no repeated messages)

if __name__ == "__main__":
    while True:
        login_with_voice()
        time.sleep(1)  # Delay to avoid rapid looping
