import pyttsx3
import speech_recognition as sr
import requests
import json
import pywhatkit as kit
#whatsapp
import webbrowser
import datetime


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')

# print (voices)

Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 190)


def speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

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
        query = query.replace("Jarvis", "")
        pywhatkit.search(query)

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

def openwhatsapp():
    webbrowser.open('https://web.whatsapp.com/')

def sendwhatsappmessage():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)
    kit.sendwhatmsg("+918964849230", "message", hour, min+2)

def TaskExe():

    while True:
        query = takeCommand()

        if 'hello' in query:
            speak("Hello sir, I am jarvis.")
            speak("How may I help you?")
        
        elif 'what is your name' in query:
            speak("My name is Jarvis")
        
        elif 'how are you' in query:
            speak("I am fine Sir! What about you?")
        
        elif 'you need a break' in query:
            speak("Ok Sir, you can call me anytime!")
            break

        elif 'bye' in query:
            speak("ok sir, bye!")
            break


        elif ('weather' in query) or ('temperature' in query):
            weather(query)


        elif ('search' in query) or ('search for' in query):
            speak("Here are the results..")
            import wikipedia as googleScrap
            query = query.replace("Jarvis", "")
            query = query.replace("search", "")
            query = query.replace("search for", "")

            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query, 2)
                speak(result)
            except:
                speak('')

  
        elif ('open whatsapp' in query):
            openwhatsapp()

        elif ('send whatsapp message' in query):
            sendwhatsappmessage()




TaskExe()
