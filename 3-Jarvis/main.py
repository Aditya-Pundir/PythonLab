import subprocess  # To execute commands in terminal
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import pyautogui  # For clicking on the buttons using cursor
import requests
import pywhatkit  # For playing things on YouTube
import smtplib  # For sending emails
import re  # For getting to and body for sending email
from datetime import date
from colorama import Fore  # To colour the print statements


def sendMail(to, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("formal.googl@gmail.com", "coder420")
        subject = "Email sent by Aditya's PA - Jarvis"
        body = body

        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("formal.googl@gmail.com", to, msg)
        speak("Email sent successfully")
    except Exception as e:
        print(e)
        speak("Couldn't send email")


def speak(audio):
    print(Fore.CYAN+"Jarvis: "+Fore.GREEN + audio + Fore.WHITE)
    subprocess.run(['say', "-v", "Tom", audio])


def wish():
    hour = datetime.datetime.now().hour
    weatherDetails = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
    temperature = weatherDetails["main"]["temp"]
    if hour >= 0 and hour < 12:
        speak(f"Good Morning Sir! Its {temperature} degrees celsius outside")
    elif hour >= 12 and hour < 17:
        speak(f"Good Afternoon Sir! Its {temperature} degrees celsius outside")
    elif hour >= 17 and hour < 24:
        speak(f"Good Evening Sir! Its {temperature} degrees celsius outside")


def takeCommand():
    recog = sr.Recognizer()
    with sr.Microphone() as src:
        print(Fore.LIGHTMAGENTA_EX+"Listening...")
        recog.pause_threshold = 1
        recog.energy_threshold = 500
        audio = recog.listen(src)

    try:
        print("Recognizing...")
        query = recog.recognize_google(audio, language="en-IN")
        print(Fore.CYAN + "User:", Fore.GREEN + "" + query + "" + Fore.WHITE)
    except:
        return "None"

    return query


if __name__ == "__main__":
    try:
        wish()
        awake = True
        while True:
            query = takeCommand().lower()

            # Logic for executing the tasks based on query:
            if "hey jarvis" in query and awake == True:
                query = query.replace("hey jarvis ", "")

            if "how are you" in query and awake == True:
                speak("I am fine Sir, thanks for asking")

            if "wikipedia" in query and awake == True:
                speak("Searching wikipedia...")
                query = query.replace(" wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
                except:
                    speak("Unable to understand!")

            if "good morning" in query and awake == True:
                hour = datetime.datetime.now().hour
                if hour >= 0 and hour < 12:
                    weatherDetails = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                    temperature = weatherDetails["main"]["temp"]

                    speak(
                        f"Good Morning Sir, its {temperature} degrees celsius outside")
                else:
                    strtime = time.strftime("%H hours and %M minutes")
                    speak(f"It's {strtime}, so technically it's not morning")

            if "good afternoon" in query or "goodmorning" in query and awake == True:
                hour = datetime.datetime.now().hour
                if hour >= 12 and hour < 18:
                    weatherDetails = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                    temperature = weatherDetails["main"]["temp"]

                    speak(
                        f"Good Afternoon Sir, its {temperature} degrees celsius outside")
                else:
                    strtime = time.strftime("%H hours and %M minutes")
                    speak(f"It's {strtime}, so technically it's not afternoon")

            if "good evening" in query or "goodevening" in query and awake == True:
                hour = datetime.datetime.now().hour
                if hour >= 17 and hour < 19:
                    weatherDetails = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                    temperature = weatherDetails["main"]["temp"]

                    speak(
                        f"Good Evening Sir, its {temperature} degrees celsius outside")
                else:
                    strtime = time.strftime("%H hours and %M minutes")
                    speak(f"It's {strtime}, so technically it's not evening")

            if "good night" in query or "goodnight" in query and awake == True:
                hour = datetime.datetime.now().hour
                if hour >= 19 and hour < 24:
                    weatherDetails = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                    temperature = weatherDetails["main"]["temp"]

                    speak(
                        f"Good Night Sir, its {temperature} degrees celsius outside, have sweet dreams")
                else:
                    strtime = time.strftime("%H hours and %M minutes")
                    speak(f"It's {strtime}, so technically it's not night")

            if "the temperature" in query and awake == True:
                weatherDetails = requests.get(
                    "http://api.openweathermap.org/data/2.5/weather?appid=d850f7f52bf19300a9eb4b0aa6b80f0d&q=haridwar&units=metric").json()
                temperature = weatherDetails["main"]["temp"]

                speak(
                    f"Its {temperature} degrees celsius today in Haridwar")

            if "the time" in query and awake == True:
                strtime = time.strftime("%H hours and %M minutes")
                speak(strtime)

            if "the day" in query and awake == True:
                if datetime.datetime.today().weekday() == 0:
                    speak("Monday")
                elif datetime.datetime.today().weekday() == 1:
                    speak("Tuesday")
                elif datetime.datetime.today().weekday() == 2:
                    speak("Wednesday")
                elif datetime.datetime.today().weekday() == 3:
                    speak("Thursday")
                elif datetime.datetime.today().weekday() == 4:
                    speak("Friday")
                elif datetime.datetime.today().weekday() == 5:
                    speak("Saturday")
                elif datetime.datetime.today().weekday() == 6:
                    speak("Sunday")

            if "the date" in query and awake == True:
                d = str(date.today())
                d = d.split("-")
                d.reverse()
                if d[1] == "01":
                    month = "january"
                elif d[1] == "02":
                    month = "february"
                elif d[1] == "03":
                    month = "march"
                elif d[1] == "04":
                    month = "april"
                elif d[1] == "05":
                    month = "may"
                elif d[1] == "06":
                    month = "june"
                elif d[1] == "07":
                    month = "july"
                elif d[1] == "08":
                    month = "august"
                elif d[1] == "09":
                    month = "september"
                elif d[1] == "10":
                    month = "october"
                elif d[1] == "11":
                    month = "november"
                elif d[1] == "12":
                    month = "december"
                d[1] = month
                dateStr = ""
                for i in range(len(d)):
                    dateStr += f" {d[i]}"
                speak(dateStr)

            if "hello jarvis" in query and awake == True:
                speak("Hi Sir")

            if "are you mad" in query and awake == True:
                speak("I can never be as mad as Spider Man")

            if "open google" in query and awake == True:
                webbrowser.open("https://google.com")

            if "open email" in query and awake == True:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            if "open flipkart" in query and awake == True:
                webbrowser.open("https://flipkart.com")

            if "open amazon" in query and awake == True:
                webbrowser.open("https://amazon.in")

            if "open youtube" in query and awake == True:
                webbrowser.open("https://youtube.com")

            if "open wikipedia" in query and awake == True:
                webbrowser.open("https://wikipedia.com")

            if "open spotify" in query and awake == True:
                webbrowser.open("https://open.spotify.com")

            if "search google for" in query and awake == True:
                search = query.replace("search google for ", "")
                webbrowser.open(
                    f"https://google.com/search?q={search}")

            if "search youtube for" in query and awake == True:
                search = query.replace("search youtube for ", "")
                # webbrowser.open(
                #     f"https://youtube.com/results?search_query={search}")
                # time.sleep(10)
                # pyautogui.click(720, 260)
                # time.sleep(5)
                # pyautogui.press("f")

                pywhatkit.playonyt(search)
                time.sleep(5)

            if "send email to" in query and awake == True:
                # Name:
                # In "(.*)", I added "?" to only grab the first time name occurs:
                name = re.search("send email to (.*?) that", query)
                to = name.group(1)

                # Body:
                bod = re.search(" that (.*)", query)
                body = bod.group(1)

                if "myself" in to:
                    sendMail("adityapundir2k@gmail.com", body)

                if "dad" in to:
                    sendMail("devendrak248@gmail.com", body)

                if "sister" in to:
                    sendMail("vandana.er1994@gmail.com", body)

                if "brother" in to:
                    sendMail("avneesh.er1991@gmail.com", body)

                if "mom" in to:
                    sendMail("pundirsunita7@gmail.com", body)

                if "sister-in-law" in to:
                    sendMail("anshikatanwar4@gmail.com", body)

            if "live" in query and awake == True:
                pywhatkit.playonyt(query)
                time.sleep(10)
                pyautogui.click(900, 700)
                time.sleep(5)
                pyautogui.click(1300, 285)

            if "open stackoverflow" in query and awake == True:
                webbrowser.open("https://stackoverflow.com")

            if "it's music time" in query and awake == True:
                webbrowser.open("https://open.spotify.com/collection/tracks")
                time.sleep(15)
                pyautogui.click(310, 500)
                pyautogui.click(310, 550)

            if "tell" and "stories" in query and awake == True:
                query = query.replace("tell ", "")
                query += " for kids"
                query = query.replace(" ", "+")
                pywhatkit.playonyt(query)
                time.sleep(10)
                pyautogui.press("f")

            if "play" in query and awake == True:
                query = query.replace("play ", "")
                speak("playing " + query)
                pywhatkit.playonyt(query)
                time.sleep(10)
                pyautogui.press("f")

            if "connect to my headset" in query or "connect headset" in query or "connect to the headset" in query or "connect my headset" in query and awake == True:
                try:
                    connection = subprocess.Popen(
                        ["blueutil", "--connect", "11-11-22-33-54-c1"])
                except:
                    speak("Unable to connect to the headset right now!")

            if "disconnect my headset" in query or "disconnect headset" in query or "disconnect the headset" in query and awake == True:
                try:
                    subprocess.Popen(
                        ["blueutil", "--disconnect", "11-11-22-33-54-c1"])
                except:
                    speak("Unable to disconnect the headset right now!")

            if "thanks" in query or "thank you" in query and awake == True:
                speak("Mention not Sir")

            if "sleep jarvis" in query or "go to sleep jarvis" in query or "go to bed jarvis" in query and awake == True:
                speak("As you wish Sir!")
                awake = False

            if "wake up jarvis" in query and awake == False:
                speak("Jarvis ready in your service Sir!")
                awake = True

    except:
        print("Thanks for using")
