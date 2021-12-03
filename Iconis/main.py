import pyttsx3
import speech_recognition as sr
import requests
import json
import pywhatkit as kit
import json
import webbrowser
import pyautogui
import time
import psutil
import random
import os
import string
from nsetools import Nse

nse = Nse()
Assistant = pyttsx3

def speak(audio):
    speaking = Assistant.speak(audio)
    print(f": {audio}")
    return speaking
    

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold=1
        audio = command.listen(source)

    try:
        print("Recognizing......")
        query = command.recognize_google(audio, language='en-in')
        print(f"you said : {query}")

    except Exception as Error:
        print("Please say again..")
        return "None"

    return query.lower()

def search(query):
    speak("Here are the results..")
    import wikipedia as googleScrap
    query = query.replace("Iconis", "")
    query = query.replace("search", "")
    query = query.replace("search for", "")

    kit.search(query)

    try:
        result = googleScrap.summary(query, 2)
        speak(result)
    except:
        speak('')

def weather(query):

    list1 = ['what', "what's", 'is', 'of', 'about', 'how', 'current', 'weather', 'temperature', "today's", 'for', 'at', 'status', 'the', 'in', 'now']
    split_query = query.split()
    location=""
    
    for word in split_query: 
        if word not in list1:
            location = word
            break

    if location =="":
        location = "indore"

    speak(f"{location}")

    api = "http://api.openweathermap.org/data/2.5/weather?q="+ location +"&appid=3e0cd0cfdf7135a53bf72064bdad403f"
    api_request = requests.get(api)
    data = json.loads(api_request.content)
    id = data['cod']
    if id == "404":
        speak("Here are the results..")
        import wikipedia as googleScrap
        query = query.replace("Iconis", "")
        kit.search(query)

        try:
            result = googleScrap.summary(query, 2)
            speak(result)
        except:
            speak('')
        return

    y = data['main']
    condition = data['weather'][0]['main']
    temp = int(y['temp']-273.15)
    max_temp = int(y['temp_max']-273.15)
    min_temp = int(y['temp_min']-273.15)

    if ('weather' in query) :
        speak(f"it's {temp} degree celcius and {condition}. Max temperature is {max_temp}  degree celcius and Min temperature is {min_temp} degree celcius.")
    elif ('temperature' in query):
        speak(f"Current temperature is {temp} degree celcius.")            
        return    

def tell_joke():
    api = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,explicit&type=twopart"
    api_request = requests.get(api)
    data = json.loads(api_request.content)
    speak(data['setup'])
    speak(data['delivery'])


def takescreenshot():
    name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=12))
    speak("please sir hold the screen, i am taking the screenshot")
    time.sleep(0.5)
    img = pyautogui.screenshot()
    img.save(f"screenshot//"+str(name)+".png")
    speak("screenshot is saved now in your main file")

def cpu_ram_battery(query):
    if 'cpu usage' in query :
        # Calling psutil.cpu_precent() for 2 seconds
         speak('The CPU usage is ' + str(psutil.cpu_percent(2)) +"%")
    
    elif 'ram usage' in query :
        # Getting % usage of virtual_memory ( 3rd field)
         speak('The RAM usage is '+ str(psutil.virtual_memory()[2]) + "%")

    elif ('battery of laptop' in query) or ('battery' in query) or ('battery of my laptop' in query):
        # returns a tuple
        battery = psutil.sensors_battery()
        speak(str(battery.percent) + " %  Battery is left" )

def restart_shutdown_logout(query):
    if 'restart now' in query:
        speak("Do you want to restart")
        result = takeCommand().lower()
        if result == 'yes':
            os.system("shutdown /r /t 1") # /r for restart and /t for time
        else:
            return
    
    elif 'shutdown now' in query:
        speak("Do you want to shutdown")
        result = takeCommand().lower()
        if result == 'yes':
            os.system("shutdown /s /t 1") # /r for shutdown and /t for time
        else:
            return
    
    elif 'logout now' in query:
        speak("Do you want to logout")
        result = takeCommand().lower()
        if result == 'yes':
            os.system("shutdown /l") # /l for logout and /t for time
        else:
            return


def openwhatsapp():
    webbrowser.open('https://web.whatsapp.com/')
