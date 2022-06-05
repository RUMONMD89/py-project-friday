import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import pyjokes

listener = sr.Recognizer()
friday = pyttsx3.init()
voices = friday.getProperty("voices")
friday.setProperty("voice", voices[1].id)


def talk(text):
    friday.say(text)
    friday.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "friday" in command:
                command = command.replace("friday", "")
    except:
        pass
    return command


def run_friday():
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%p")
        print(time)
        talk("Current time is " + time)

    elif "play" in command:
        song = command.replace("play", "")
        print("playing" + song)
        pywhatkit.playonyt(song)

    elif "open" in command:
        social = command.replace("open", "")
        print("opening" + social)
        pywhatkit.search(social)

    elif "tell me about" in command:
        look_for = command.replace("tell me about", "")
        info = wikipedia.summary(look_for, 5)
        print(info)
        talk(info)

    elif "jokes" in command:
        talk(pyjokes.get_joke())
    elif "date" in command:
        talk("sorry. i am already married")

    else:
        talk("i did not get it but i am searching...")
        pywhatkit.search(command)


while True:
    run_friday()
