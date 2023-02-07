import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' or 'hey' or 'yo' in command:
                command = command.replace('yo', '')
                command = command.replace('hey', '')
                command = command.replace('alexa', '')

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The current time is " + time)
    elif 'search' in command:
        info = command.replace('search', '')
        if "about" in command:
            info = info.replace('about', "")
        info = wikipedia.summary(info, 4)
        talk(info)
    elif 'who' in command:
        info = command.replace('who', '')
        if "is" in command:
            info = info.replace('is', "")
        info = wikipedia.summary(info, 4)
        talk(info)
    elif 'what' in command:
        info = command.replace('who', '')
        if "is" in command:
            info = info.replace('is', "")
        info = wikipedia.summary(info, 4)
        talk(info)
    elif 'how' in command:
        info = command.replace('who', '')
        if "is" in command:
            info = info.replace('is', "")
        info = wikipedia.summary(info, 4)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please say that again.")


    
while True:
    run_alexa()
    command = take_command()
    if "bye" in command:
        talk("Goodbye!")
        break
