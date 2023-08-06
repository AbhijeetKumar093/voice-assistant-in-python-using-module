import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import openai
import random

# chatStr = ""
#
#
# def chat(command):
#     global chatStr
#     print(chatStr)
#     openai.api_key = "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"
#     chatStr = f"you {command}\n alexa: "
#
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=chatStr,
#         temperature=0.7,
#         max_token=256,
#         top_p=1,
#         frequenncy_penality=0,
#         presence_penalty=0,
#     )
#     # todo: Wrap this inside of a try catch block
#     talk(response["choices"][0]["text"])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return response["choices"][0]["text"]
#
#     with open(f"Openai/{''.join(prompt_split('alexa')[1:]).strip()}.txt", "w") as f:
#         f.write(text)


def ai(prompt):
    openai.api_key = "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"
    text = f"Open AI response for Prompt: {prompt} \n**************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_token=256,
        top_p=1,
        frequenncy_penality=0,
        presence_penalty=0,
    )
    # todo: Wrap this inside of a try catch block
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/prompt- {random.randint(1,99999)}", "w") as f:
        f.write(text)


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="en-in")
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)


    except:
        pass
    return command


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        print("Good Morning")
        talk("Good Morning")
    elif 12 <= hour <= 17:
        print("Good afternoon")
        talk("Good afternoon")
    else:
        print("Good evening")
        talk("Good evening")
    print("I am alexa. How may i help you")
    talk("I am alexa. How may i help you")


def run_alexa():
    while True:
        try:
            command = take_command()
            print(command)
            if 'hello' in command:
                print("hello, how may I help you")
                talk("hello, how may I help you")
            if 'play folder' in command:
                music = 'D:\\purifier_song'
                song = os.listdir(music)
                print(song)
                os.startfile(os.path.join(music, song[1]))
            if 'play' in command:
                song = command.replace('play', '')
                pywhatkit.playonyt(song)
            if 'time' in command:
                time = datetime.datetime.now().strftime('%H:%M %p')
                print(time)
                talk('Current time is ' + time)
            if 'tell me about' in command:
                person = command.replace('tell me about', '')
                info = wikipedia.summary(person, 10)
                print(info)
                talk(info)
            if 'wikipedia' in command:
                print("searching wikipedia...")
                person = command.replace('wikipedia', '')
                info = wikipedia.summary(person, 10)
                print(info)
                talk(info)
            if 'hey' in command:
                talk('hello')
            if 'how are you' in command:
                print('i am wonderful, tell me what about you')
                talk('i am wonderful, tell me what about you')
            if 'joke' in command:
                print(pyjokes.get_joke())
                talk(pyjokes.get_joke(language="en", category="neutral"))
            if 'open google' in command:
                talk("google opening sir...")
                webbrowser.open("google.com")
            if 'open youtube' in command:
                talk("youtube opening sir...")
                webbrowser.open("www.youtube.com")
            if 'open geek for geeks' in command:
                webbrowser.open("https://practice.geeksforgeeks.org/")
            if 'open vs code' in command:
                code = "C:\\Users\\ak677\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code)
            if 'alexa exit' in command:
                break
            elif 'alexa' in command:
                ai(prompt=command)

            else:
                talk('Please say it again...')
                print('Please say it again...')

        except Exception:  #=> Too broad exception clause
            print("I can't understand...")
            talk("I can't understand...")


if __name__ == "_main_":
    wishMe()


run_alexa()