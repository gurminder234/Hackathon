import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from bs4 import BeautifulSoup

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1])


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('hey there! user.')
    elif 'who are you' in command:
        talk('I am just a software')
    elif 'ok bye' in command:
        talk('Well then see you later')
    elif 'what is your name' in command:
        talk('I am Jarvis, nice to meet you.')
    elif 'how are you' in command:
        talk('I am good what about you?')
    elif 'i am fine' in command:
        talk('Good to hear that! Well,I have got some tasks for you today.')
    elif 'what are those' in command:
        talk('Some environmental friendly tasks. First of them is trying to save electricity by switching of unnecessary lights and appliances.Secondly,plant atleast one tree and lastly use less of plastics.')
    elif 'ok' in command:
        talk("That's like a good user")
    else:
        talk('Can you come again.')



while True:
    run_alexa()
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from bs4 import BeautifulSoup

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1])


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('hey there! user.')
    elif 'who are you' in command:
        talk('I am just a software')
    elif 'ok bye' in command:
        talk('Well then see you later')
    elif 'what is your name' in command:
        talk('I am Jarvis, nice to meet you.')
    elif 'how are you' in command:
        talk('I am good what about you?')
    elif 'i am fine' in command:
        talk('Good to hear that! Well,I have got some tasks for you today.')
    elif 'what are those' in command:
        talk('Some environmental friendly tasks. First of them is trying to save electricity by switching of unnecessary lights and appliances.Secondly,plant atleast one tree and lastly use less of plastics.')
    elif 'ok' in command:
        talk("That's like a good user")
    else:
        talk('Can you come again.')



while True:
    run_alexa()
