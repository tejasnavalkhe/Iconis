from flask import Flask, render_template, request, redirect
from main import *
import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def take():
  return render_template('index.html')

@app.route('/<query>', methods=['GET'])
def main(query):
  query = query.lower()
  if request.method == 'GET':
    if 'hello' in query:
      speak("Hello sir, I am Iconis.")
    elif 'what is your name' in query:
      speak("My name is Iconis")
    elif 'how are you' in query:
      speak("I am fine Sir! What about you?")
    elif ('search' in query) or ('search for' in query):
        search(query)
    elif ('take screenshot' in query) or ('take a screenshot' in query) or ('screenshot' in query):
        takescreenshot()
    elif ('open whatsapp' in query):
        openwhatsapp()
    elif ('weather' in query) or ('temperature' in query):
        weather(query)
    elif ('tell me a joke' in query ) or ('tell a joke' in query) or ('tell joke' in query) or ('tell me joke' in query):
        tell_joke()
    elif ('cpu usage' in query) or ('ram usage' in query) or ('battery of laptop' in query) or ('battery' in query) or ('battery of my laptop' in query):
        cpu_ram_battery(query)
    elif ('restart' in query) or ('shutdown' in query) or ('logout' in query):
        restart_shutdown_logout(query)
    elif 'play' in query:
        song = query.replace('play', '')
        speak('playing ' + song)
        kit.playonyt(song)
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'are you single' in query:
        speak('I am in a relationship with wifi')
        speak('Better luck, next time.')
    if ('send sms' in query) or ('send message' in query):
        try:
            speak("On which number should I send!")
            to = ''.join(takeCommand().split())
            speak("What should I send?")
            content = takeCommand()
            print(content)
            speak('Is this number correct?')
            speak(to)
            correct = takeCommand().lower()

            if correct == 'yes':
                url = "https://www.fast2sms.com/dev/bulkV2"
                auth_code = "DTqFk4SUxBbXWzC0HcshwVvAy27P9LRrnI3poKN51fmOEQi6jZEfuFXCdqITYAOrc4R3y9H70PvVUQj6"
                querystring = {"authorization":auth_code,"flash":0,"message":content,"language":"english","route":"q","numbers":f"{to}"}
                headers = {
                'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                speak(f"SMS has been sent! to {to}")
            else:
                return redirect('/send%20SMS')
        except Exception as e:
            print(e)
            speak("Sorry sir, I am not able to send this SMS")
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open facebook" in query:
        webbrowser.open("facebook.com")
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")
    elif "open code" in query:
        code_path = "C:\\Users\\Tejas Navalkhe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    elif "price" in query: # of Tata Motors
        query = query.replace("price", "")
        query = ''.join(query.upper().split())
        stocks = nse.get_stock_codes()
        for stock_name, _ in stocks.items():
            if stock_name in query:
                query = stock_name
                ltp = f"The price of {stock_name} is {nse.get_quote(query).get('lastPrice')}"
                speak(ltp)
  return "Success!"


if __name__ == '__main__':
  app.run()
