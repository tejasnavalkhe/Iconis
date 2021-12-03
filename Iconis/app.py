from flask import Flask, render_template, request, redirect
from main import *
import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def take():
  return render_template('index.html')

@app.route('/<query>', methods=['GET'])
def main(query):
  if request.method == 'GET':
    if 'hello' in query:
      speak("Hello sir, I am Iconis.")
      return redirect('/end')
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
    elif ('send whatsapp message' in query):
        sendwhatsappmessage()
    elif ('weather' in query) or ('temperature' in query):
        weather(query)
    elif ('tell me a joke' in query ) or ('tell a joke' in query)  or ('tell joke' in query):
        tell_joke()
    elif ('cpu usage' in query) or ('ram usage' in query) or ('battery of laptop' in query):
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
    if 'send email' in query:
        try:
            speak("What should I say!")
            content = takeCommand()
            to = "navalkhetejas18@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry sir, I am not able to send this email")
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
  return "render_template('index.html')"


if __name__ == '__main__':
  app.run(debug=True)
