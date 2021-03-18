import pyttsx3 # pip install pyttsx3
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib

engine = pyttsx3.init()

def speak(audio): #deifning the speak function
    engine.say(audio)
    engine.runAndWait()

def time_(): #defining the time function 
    speak("the current time is")
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    speak(Time)

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Tahsin!")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Jarvis at your service. Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-uk')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(tp, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('username@gmail.com' , 'password')
    sevrer.sendEmail('username@gmail.com',to,content)
    server.close()


if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia', 'wikipedia')
            result = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak('who is the reciever?')
                reciever = input("What is the email : ")
                to = reciever
                sendEmail(to, content)
                speak(content)
                speak("Email has been sent.")

            except Exception as e:
                print(e)
                speak("unable to send email.")

TakeCommand()
