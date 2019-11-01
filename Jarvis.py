import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning vishal")
    elif hour>12 and hour<18:
        speak("Good afternoon vishal")
    else:
        speak("Good evening vishal")
    speak("I am jarvis sir. How I may assist you")

def takecommand():
    '''It takes microphone input and return as string'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        text = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(text, Language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please speak again")
        return "None"
    return query
if __name__ == '__main__':
    # speak("hello vishal how are you")
    # speak("I am doing good jarvis")
    takecommand()