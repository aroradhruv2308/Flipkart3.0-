import pyttsx3
import datetime
import speech_recognition as SR
import wikipedia
import webbrowser
import os
import random
import subprocess as sp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from translate import Translator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak('Good Morning')
    elif hour < 16:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am Jarvis, How may I help you')


def take_command():
    R = SR.Recognizer()
    with SR.Microphone() as source:
        print('listening...')
        R.pause_threshold = 1
        R.energy_threshold = 500
        audio = R.listen(source)
    try:
        print('Recognising....')
        query = R.recognize_google(audio, language='en-in')
        print(f'User Said : {query}')
    except Exception as E:
        print(E)
        print('Say again please....')
        return 'None'
    return query


def send_email(to_add):
    from_add = 'divybadoniya14092000@gmail.com'
    print('What should be the subject')
    speak('What should be the subject')
    sub = take_command()
    print('What should be the body, sir')
    speak('What should be the body, sir')
    body = take_command()
    msg = MIMEMultipart()
    msg['from'] = from_add
    msg['to'] = to_add
    msg['Subject'] = sub
    msg.attach(MIMEText(body, 'plain'))
    filename = 'Jarvis.py'
    attachment = open(filename,'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment: filename= "+filename)
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(from_add, 'pass')
    server.sendmail(from_add, to, text)
    server.close()


if __name__ == "__main__":
    wishme()
    list_email = {'bhola sir': 'bhola.mact2002@gmail.com', 'ashish': 'popandiyaashish@gmail.com', 'divy': 'divybadoniya14092000@gmail.com',
    'mohit': 'mohitdah4ck3r@gmail.com', 'sandeep': 'cse16manit@gmail.com'}
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak('According to Wikipedia')
            speak(results)
      
        elif 'search' in query:
            speak('Searching...')
            query = query.replace('search', '')
            webbrowser.open(query)

        elif 'play music' in query:
            music_dir = 'D:\\SONGS\\2012'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(1, len(movies))]))

        elif 'play movie' in query:
            movie_dir = 'D:\\MOVIES'
            movies = os.listdir(movie_dir)
            os.startfile(os.path.join(movie_dir, movies[random.randint(1, len(movies))]))
        
        elif 'what is the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {time}')
        
        elif 'open' in query:
            if 'pycharm' in query:
                    opath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
                    os.startfile(opath)
            elif 'visual studio' in query:
                    opath = "C:\\Users\\DIVY\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(opath)
            elif 'codeblocks' in query:
                    opath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
                    os.startfile(opath)
            elif 'chrome' in query:
                    opath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(opath)
            elif 'python interpreter' in query:
                    opath = "C:\\Users\\DIVY\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
                    os.startfile(opath)
            elif 'most wanted' in query:
                    opath = 'D:\\GAMES\\Need for Speed Most Wanted\\speed.exe'
                    os.startfile(opath)
            elif 'zoo tycoon' in query:
                    opath = 'D:\\GAMES\\Zoo Tycoon 1 - (Www.ApunKaGames.Com)\\Game\\zoo.exe'
                    os.startfile(opath)
            elif 'spotify' in query:
                    sp.call('spotify')
            elif 'youtube' in query:
                    webbrowser.open('youtube.com')
            elif 'images' in query:
                if 'indore' in query:
                        opath = 'D:\\images\\INDORE'
                        os.startfile(opath)
                elif 'family' in query:
                        opath = 'D:\\images\\family'
                        os.startfile(opath)
                elif 'college' in query:
                        opath = 'D:\\images\\college'
                        os.startfile(opath)
        
        elif 'send email' in query:
            try:
                if 'bhola' in query:
                    to = list_email['bhola sir']
                elif 'divy' in query:
                    to = list_email['divy']
                elif 'ashish' in query:
                    to = list_email['ashish']
                elif 'mohit' in query:
                    to = list_email['mohit']
                elif 'sandeep' in query:
                    to =list_email['sandeep']
                send_email(to)
                print('Email has been sent')
                speak('Email has been sent')
            except Exception as E:
                speak('Sorry sir, I am not able to send email')
                print('Sorry sir, I am not able to send email')
        elif 'translate' in query:
            query.replace('translate','')
            if 'in hindi' in query:
                query.replace('in hindi','')
                translator = Translator(to_lang="Hindi")
                translation = translator.translate(query)
            elif 'in french' in query:
                query.replace('in french','')
                translator = Translator(to_lang="French")
                translation = translator.translate(query)
            elif 'in german' in query:
                query.replace('in german','')
                translator = Translator(to_lang="German")
                translation = translator.translate(query) 
            print(translation)
            speak(translation)
        else:
            print('I am unable to complete the task, please try again')
            speak('I am unable to complete the task, please try again')