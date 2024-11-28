import pyttsx3 
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes
#pyttsx3 is a library for text to speech conversion that even works offline
engine=pyttsx3.init('sapi5') #sapi5  is a voice recognition and synthesis microsoft speech api,api is an application programming interface that allows software applications
#to communicate with each other 
#init method initialises objects when they are created from a class,it assignes values passes as attributes to objects 
#characteristics or attributes
voices=engine.getProperty('voices')
print(voices[len(voices)-1].id)
engine.setProperty('voices',voices[0].id)
#function to convert text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#converts voice to text    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=100,phrase_time_limit=5)
    try:
        print("recognising...")
        query=r.recognise_google(audio,language='en-in')
        print(f"use said: {query}") 
    except Exception as e:
        speak("say that again please...")
        return "none"
    return query
#function to wish us gm,etc
def wish():
    hour=int(datetime.datetime.now().hour)
    tt =time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        speak(f"good morning Mr Gautam,....its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon Mr Gautam,....its {tt}")
    else:
        speak(f"good evening Mr Gautam,....its {tt}")  
    speak('I am jarvis Sir................ How may i help you')      



if 1:

    wish()  
    
    query=takecommand().lower()

#logic building for tasks
    if "open notepad" in query:

        npath="C:\\Windows\\notepad.exe"
        os.startfile(npath)
    elif "close notepad" in query:
        speak("okay sir,closing notepad")
        os.system("taskkill /f /im notepad.exe")    
    elif "open command prompt" in query:
        os.system("start cmd") 
    elif "open camera" in query:
        cap=cv2.VideoCapture(0) #0 cuz used internal camera
        while True:
            ret,img=cap.read()
            cv2.imshow('webcam',img)
            k=cv2.waitKey(50)
            if k==27:
                break
            cap.release()    
            cv2.destroyAllWindows()
    elif "ip address" in query:
        ip=get('https://api.ipify.org').text
        speak(f"your IP address is {ip}")
    elif "wikipedia" in query:
        speak("searching wikipedia.......")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        speak(results)
        print(results)
    elif "open youtube" in query:
        webbrowser.open("www.youtube.com")
    elif "open instagram" in query:
        webbrowser.open("www.instagram.com")
    elif "open stackoverflow" in query:
        webbrowser.open("www.stackoverflow.com") 
    elif "open google" in query:
        speak("sir,what should i search on google")
        cm=takecommand().lower()
        webbrowser.open(f"{cm}")
    elif "tell a joke" in query:
        joke = pyjokes.get_joke()
        speak(joke) 
    elif "shutdown the system" in query:
        os.system("shutdown /s /t 5")    
    elif "restart the system" in query:
        os.system("shutdown /r /t 5")   
    elif "sleep mode on" in query:
        os.system("rund1132.exe powrprof.dil,SetSuspendState 0,1,0")     
    elif "play songs on youtube" in query:
        kit.playonyt("see you again")  
   
    elif 'no thanks' in query:
        speak('As you wish sir,have a good day')
        sys.exit()
    speak('sir...any other tasks for today?')
