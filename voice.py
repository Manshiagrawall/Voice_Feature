import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
from docx import Document
import time

# Create a new Document
document = Document()

def speak(text):
    # Use Google TTS to convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")  # Save the audio file temporarily
    playsound("temp.mp3")  # Play the audio file
    os.remove("temp.mp3")  # Remove the audio file after playing

def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please enter your phone number.")
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            phone_number = recognizer.recognize_google(audio)
            print(f"You said: {phone_number}")
            return phone_number
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Could not request results from Google Speech Recognition service.")
            return None

def save_to_document(content):
    # Add the content to the document
    document.add_paragraph(content)
    # Save the document
    document.save("user_input.docx")
    print(f"Saved to document: {content}")

def login_with_voice():
    phone_number = listen_to_voice()
    if phone_number:
        speak(f"You entered: {phone_number}. Logging in...")
        save_to_document(phone_number)  # Save the phone number to the document

if __name__ == "__main__":
    while True:
        login_with_voice()
        time.sleep(1)  # Delay to avoid rapid looping
