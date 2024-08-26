import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
from googletrans import Translator
from gtts import gTTS
import wolframalpha
from requests import get
import pywhatkit as kit
import pyjokes
import newsapi
import requests
import sys
import pyautogui
import cv2
import numpy as np


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you")

def WolfRam(query):
    api_key = "7Q7GVK-GKEU33QJGH"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)
    try:
        Answer = next(requested.results).text
        return Answer
    except:
        speak("String value is not answerable")

def Calculator(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divided by","/")
    Term = Term.replace("into","*")
    Term = Term.replace("multiplied by","*")
    Term = Term.replace("upon","/")

    Final = str(query)
    try:
        result = WolfRam(Final)
        speak(f"{result}")
        print(result)
    except:
        speak("String value is not answerable")

def Temp(query):
    Temp = str(query)

    Temp = Temp.replace("what is","")
    Temp = Temp.replace("jarvis","")
    Temp = Temp.replace("temperature","")
    Temp = Temp.replace("the","")
    Temp = Temp.replace("in","")
    temp_query = str(Temp)

    if 'outside' in Temp:
        i = "Temperature in vadodara"
        answer = WolfRam(i)
        speak(f"{i} is {answer}")

    else:
        j = "Temperature in " + temp_query
        answer = WolfRam(j)
        speak(f"{j} is {answer}")


def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please...")
        return " "
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server. ehlo()
    server.starttls()
    server.login('tanaybaviskardpsv@gmail.com', 'dtanay@123')
    server.sendmail('tanaybaviskardpsv@gmail.com', to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/everything?q=tesla&from=2021-07-01&sortBy=publishedAt&apiKey=d19972b3dae64da38f66746ddebd075d'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first", "second", "third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def TaskExecution():
    #wishMe()
    while True:
        query = takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak ('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)
            speak (results)

#open statements

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
            break
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'your name' in query:
            speak("My name is Jarvis. I am your very own virtual assistant")

        elif 'send an email' in query:
            try:
                speak("what should i write?")
                content = takeCommand().lower()
                to = "tanaybaviskar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry i couldn't deliver this email")

#opening apps in the laptop
        elif 'open notepad' in query:
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open command prompt' in query:
            os.system("start cmd")
            break

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP adress is {ip}")

        elif 'send message' in query:
            mummy = "8460448586"
            speak("to whome should i send this message?")
            cm = takeCommand().lower()
            speak("what should i say?")
            dm = takeCommand().lower()
            kit.sendwhatmsg("+91",cm, dm, 21,42)

        elif 'play songs' in query:
            speak("which song do you want me to play?")
            cm = takeCommand().lower()
            kit.playonyt(cm)
            break

        elif "set an alarm" in query:
            speak("for what time should i set it?")
            i = takeCommand().lower()
            stop = False
            while stop == False:
                rn = str(datetime.datetime.now().time())
                print(rn)
                if rn >= (i):
                    stop = True
                    os.system("C:\\Users\\tanay\\Downloads\\alarm.mp3")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shutdown the system' in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 0")
            sys.exit()

        elif 'restart the system' in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 0")

        elif 'news' in query:
            speak("Here are the latest updates")
            news()

        elif 'screenshot' in query or 'take a screenshot' in query:
            speak("taking screenshot")
            img = pyautogui.screenshot()
            speak("What should i name the screenshot file?")
            name = takeCommand().lower()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif 'record screen' in query or 'screen recorder' in query:

            screen_size=(1920,1080)
            fourcc=cv2.VideoWriter_fourcc(*"XVID")
            out=cv2.VideoWriter("output.avi",fourcc,20.0,(screen_size))
            cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Live", 480, 270)

            while True:
                img=pyautogui.screenshot()
                frame=np.array(img)
                frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                out.write(frame)
                cv2.imshow("show",frame)
                if cv2.waitKey(1)==ord("q"):
                    break

            cv2.destroyAllWindows()
            out.release()
            break

        elif "sleep" in query:
            speak("i am going to sleep now. You can call me anytime")
            break

        elif 'temperature' in query:
            Temp(query)

        elif 'google' in query:
            query = query.replace ("google", "")
            query = query.replace("can","")
            query = query.replace("you","")
            query = query.replace("search","")
            query = query.replace("on","")
            query = query.replace("for","")
            query = query.replace("me","")
            kit.search(query)
            break

        elif 'info' in query:
            query = query.replace("info","")
            query = query.replace("some","")
            query = query.replace("can","")
            query = query.replace("you","")
            query = query.replace("share","")
            query = query.replace("give","")
            query = query.replace("me","")
            query = query.replace("us","")
            query = query.replace("about","")
            query = query.replace("information","")
            query = query.replace("on","")
            i = kit.info(query)
            speak (i)

        elif 'information' in query:
            query = query.replace("info","")
            query = query.replace("some","")
            query = query.replace("can","")
            query = query.replace("you","")
            query = query.replace("share","")
            query = query.replace("give","")
            query = query.replace("me","")
            query = query.replace("us","")
            query = query.replace("about","")
            query = query.replace("information","")
            query = query.replace("on","")
            i = kit.info(query)
            speak (i)

        else:
            result = WolfRam(query)
            print(result)
            speak(result)

if __name__=="__main__":
    while True:
        permission = takeCommand().lower()
        if "wake up" in permission:
            wishMe()
            TaskExecution()
        elif "are you there" in permission:
            speak("Sir i am always here for you")
            TaskExecution()
        elif 'jarvis' in permission:
            speak("yes sir?")
            TaskExecution()
        elif "goodbye" in permission:
            speak("goodbye sir!")
            sys.exit()
