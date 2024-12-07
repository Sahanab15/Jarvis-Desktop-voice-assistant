import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import streamlit as st
import subprocess

# Inline CSS for the Jarvis Desktop Assistant
custom_css = """
<style>
body {
  font-family: 'Arial', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(to right, #141e30, #243b55);
  color: #fff;
  margin: 0;
  overflow: hidden;
}

.container {
  text-align: center;
}

.jarvis-logo {
  position: relative;
  margin: 0 auto 20px;
  width: 120px;
  height: 120px;
}

.circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #00f260, #0575e6);
  margin: auto;
  animation: pulse 1.5s infinite;
}

.circle-outline {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 2px solid rgba(255, 255, 255, 0.3);
  transform: translate(-50%, -50%);
  animation: rotate 3s linear infinite;
}

.welcome-text {
  font-size: 2rem;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 1rem;
  color: #d3d3d3;
  margin-bottom: 20px;
}

.start-btn {
  background: linear-gradient(135deg, #00f260, #0575e6);
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 25px;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.start-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.3);
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

@keyframes rotate {
  from {
    transform: translate(-50%, -50%) rotate(0deg);
  }
  to {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
</style>
"""

# HTML for the Jarvis layout
jarvis_html = """
<div class="container">
  <div class="jarvis-logo">
    <div class="circle"></div>
    <div class="circle-outline"></div>
  </div>
  <h1 class="welcome-text">Welcome to Jarvis Desktop Assistant</h1>
  <p class="subtitle">Your personal AI assistant at your service.</p>
  <button class="start-btn">Get Started</button>
</div>
"""

# Set Streamlit page configuration
st.set_page_config(page_title="Jarvis Desktop Assistant", layout="centered")

# Inject the CSS and HTML
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(jarvis_html, unsafe_allow_html=True)


engine = pyttsx3.init()


def speak(audio) -> None:
    try:
        engine.say(audio)
        engine.runAndWait()
    except RuntimeError:
        pass


def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)


def date() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print(f"The current date is {day}/{month}/{year}")


def wishme() -> None:
    print("Welcome back Madam!!")
    speak("Welcome back Madam!!")

    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Madam!!")
        print("Good Morning Madam!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Madam!!")
        print("Good Afternoon Madam!!")
    elif 16 <= hour < 24:
        speak("Good Evening Madam!!")
        print("Good Evening Madam!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("Jarvis at your service Madam, please tell me how may I help you.")
    print("Jarvis at your service Madam, please tell me how may I help you.")


def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source, timeout=30, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm JARVIS created by Ms.Sahana and Ms.Harshitha and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Ms.Sahana and Ms.Harshitha and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine Madam, What about you?")
            print("I'm fine Madam, What about you?")

        elif "fine" in query:
            speak("Glad to hear that Ma'am!!")
            print("Glad to hear that Ma'am!!")

        elif "good" in query:
            speak("Glad to hear that Ma'am!!")
            print("Glad to hear that Ma'am!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open google" in query:
            wb.open("google.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0, x-1)
            #os.startfile(os.path.join(song_dir, songs[y]))
            song_path = os.path.join(song_dir, songs[y])
            wmplayer_path = r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe"
            subprocess.call([wmplayer_path, song_path])
                                 
            
           
            

        elif "open chrome" in query:
            chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")


        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")


        elif "offline" in query:
            quit()
