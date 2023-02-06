import speech_recognition as sr
import pyttsx3 as tts


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
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' or 'song' or 'sing' in command:
        talk('Playing your song!')