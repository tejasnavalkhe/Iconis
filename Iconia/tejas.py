import pyttsx3
from datetime import datetime
import pytz
import requests
import socket
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import psutil
from nsetools import Nse

tz = pytz.timezone('Asia/Calcutta')
nse = Nse()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
  """speak function will speak the given audio statement.

  Args:
      audio (str): The statement that will pass to speak by iconia
  """
  engine.say(audio)
  engine.runAndWait()
  engine.stop()

def wishMe():
  """wishMe function will wish according to time and will give temperature.
  """
  name = socket.gethostname()
  hour = int(datetime.now(tz).hour)
  weather_api = "https://api.openweathermap.org/data/2.5/weather?"
  API_KEY = 'b66ab67a44018d425129a91b93153744'
  city = requests.get('https://api.ipdata.co?api-key=523d86e8b28465cfdec73bdfa72b2903e4a4449a0300ace673e7bb2e').json().get('city')
  URL = weather_api + "q=" + city + f"&units=metric" + "&appid=" + API_KEY
  response = requests.get(URL)
  if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = main['temp']

  if hour>=0 and hour<12:
    speak(f"Good Morning {name}, It's {temperature} degrees Celsius temperature.")
  elif hour>=12 and hour < 16:
    speak(f"Good Afternoon {name}, It's {temperature} degrees Celsius temperature.")
  elif hour>=16 and hour<20:
    speak(f"Good Evening {name}, It's {temperature} degrees Celsius temperature.")
  else:
    speak(f"Good Night {name}, It's {temperature} degrees Celsius temperature.")


def takeVoice():
  """This function will take voice input from user and return string output.
  """
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 1
    audio = r.listen(source)

    try:
      query = r.recognize_google(audio, language='en-in')
    except Exception as e:
      print(e)
      print("Say again...")
      return "None"

  return query

if __name__ == '__main__':
  while True:
    query = takeVoice().lower()
    if 'wikipedia' in query:
      print("Searching Wikipedia...")
      query = query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences=2)
      speak(f"According to wikipedia, {results}")
    elif "good morning" in query:
      wishMe()
    elif "open youtube" in query:
      webbrowser.open("youtube.com")
    elif "open facebook" in query:
      webbrowser.open("facebook.com")
    elif "open google" in query:
      webbrowser.open("google.com")
    elif "open stackoverflow" in query:
      webbrowser.open("stackoverflow.com")
    elif "play music" in query:
      music_dir = 'D:\\Entertainment\\Songs'
      songs = os.listdir(music_dir)
      random.shuffle(songs)
      play_this = random.randint(0, len(songs)-1)
      os.startfile(os.path.join(music_dir, songs[play_this]))
    elif "open code" in query:
      code_path = "C:\\Users\\Tejas Navalkhe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
      os.startfile(code_path)
    elif "exit" or "close" in query:
      exit(0)
    elif "price" in query:
      query = query.replace("price", "")
      query = ''.join(query.upper().split())
      stocks = nse.get_stock_codes()
      for stock_name, _ in stocks.items():
        if stock_name in query:
          # print('Got it: ', stock_name)
          query = stock_name
          ltp = f"The price of {stock_name} is {nse.get_quote(query).get('lastPrice')}"
          speak(ltp)
    elif 'cpu usage' in query:
        speak('The CPU usage is: ', psutil.cpu_percent(4))
    elif 'shutdown pc' or 'shutdown laptop' in query:
        os.system("shutdown /s")
    elif 'logoff pc' or 'logoff laptop' in query:
        os.system("shutdown /l")
    elif 'restart pc' or 'restart laptop' in query:
        os.system("shutdown /r")