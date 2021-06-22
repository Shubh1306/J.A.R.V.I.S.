import pyttsx3   # pip install pyttsx3
import speech_recognition as sr   # pip install SpeechRecognition
import datetime
import wikipedia   # pip install wikipedia
import webbrowser
import os
import random
import urllib.request
import numpy as np   # pip install numpy
import smtplib   # pip install secure-smtplib
import cv2   # pip install opencv-python
from requests import get
import pywhatkit as kit   # pip install pywhatkit
import sys
import pyjokes   # pip install pyjokes
from email.mime.text import MIMEText   # pip install email-to
from email.mime.multipart import MIMEMultipart   # pip install email-to
from email.mime.base import MIMEBase   # pip install email-to
from email import encoders   # pip install email-to
import psutil   # pip install psutil
import os.path
import requests
from bs4 import BeautifulSoup   # pip install bs4
import operator   # for doing calculations using voice
import instaloader   # pip install instaloader
import time
import speedtest   # pip install speedtest
from twilio.rest import Client   # pip install twilio
import pyautogui   # pip install pyautogui
import PyPDF2   # pip install PyPDF2 
from pywikihow import search_wikihow   # pip install pywikihow
import MyAlarm

MASTER = "Shubh"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# text to speech:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# to wish:
def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning Sir... its {tt}")

    elif hour>=12 and hour<16:
        speak(f"Good Afternoon Sir... its {tt}")

    else:
        speak(f"Good Evening Sir... its {tt}")

    speak("I am Jarvis. Please tell me how may I help you.")

# for taking screenshot:
def screenshot():
    speak("Sir, please tell me the name for this file...")
    name = takeCommand().lower()
    speak("Please hold on sir... I am taking the screenshot.")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"C:\\Users\\Shubh Jethwa\\OneDrive\\Pictures\\Jarvis Images\\ {name}.png")
    speak("I have successfully taken the screenshot sir...")

# for news updates:
def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=745bcc9c32b240aab7e6b8953fc47a60"

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

# for reading the PDF file:
def pdf_reader():
    book = open("MECHANICS OF FLIGHT BY A.C KERMODE.pdf", "rb")   # here u can enter the name of any book
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Sir, the total number of pages in this book {pages}")
    speak("Sir, please enter the page number")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    # print(text)
    speak(text)

# for getting cpu status:
def cpu():
    cpu = str(psutil.cpu_percent())
    print(cpu)
    speak(f"Sir, you have used {cpu} percent of cpu...")

# To convert voice to text:
def takeCommand():
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=None, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# to send email:
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("jethwashubh32@gmail.com", "Lucifer@1306")
    server.sendmail("jethwashubh32@gmail.com", to, content)
    server.close()

def TaskExecution():
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query:
        if "wikipedia" in query:
            speak("Searching Wikipedia Sir...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("Opening youtube sir...")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open facebook" in query:
            speak("Opening facebook sir...")
            webbrowser.open("facebook.com")

        elif "open stackoverflow" in query:
            speak("Opening stackoverflow sir...")
            webbrowser.open("stackoverflow.com")

        elif "open drive" in query:
            speak("Opening google drive sir...")
            webbrowser.open("drive.google.com")

        elif "open notepad" in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            speak("Opening notepad sir...")
            os.startfile(path)

        elif "adobe reader" in query:
            path = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            speak("Opening adobe reader sir...")
            os.startfile(path)

        elif "open terminal" in query:
            path = ("C:\\WINDOWS\\system32\\cmd.exe")
            speak("Opening command prompt sir...")
            os.startfile(path)

        elif "play music" in query:
            music_dir = "C:\\Users\\Shubh Jethwa\\Music\\My Playlist"
            songs = os.listdir(music_dir)
            speak("Starting the music sir...")
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = "E:\\VS Code Setup\\Microsoft VS Code\\Code.exe"
            speak("Opening visual studio code sir...")
            os.startfile(codePath)

        elif "open recorder" in query:
            path = "D:\\obs-studio\\bin\\64bit\\obs64.exe"
            speak("Opening the recorder sir...")
            os.startfile(path)

        elif "open control panel" in query:
            path = "C:\\Users\\Shubh Jethwa\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel"
            speak("Opening control panel sir...")
            os.startfile(path)

        elif "open photoshop" in query:
            path = "C:\\Program Files\\Adobe\\Adobe Photoshop CC (64 Bit)\\Photoshop.exe"
            speak("Opening adobe photoshop sir...")
            os.startfile(path)

        elif "open autocad" in query:
            path = "C:\\Program Files\\Autodesk\\AutoCAD 2014\\acad.exe"
            speak("Opening autocad sir...")
            os.startfile(path)

        elif "open excel" in query:
            path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            speak("Opening microsoft excel sir...")
            os.startfile(path)

        elif "open firefox" in query:
            path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            speak("Opening mozilla firefox sir...")
            os.startfile(path)

        elif "open edge" in query:
            path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            speak("Opening microsoft edge sir...")
            os.startfile(path)

        elif "open chrome" in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("Opening google chrome sir...")
            os.startfile(path)
        
        elif "open pycharm" in query:
            path = "E:\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            speak("Opening pycharm sir...")
            os.startfile(path)

        elif 'open nitro' in query:
            path = "C:\\Program Files\\Nitro\\Pro\\13\\NitroPDF.exe"
            speak("Opening nitro editor sir...")
            os.startfile(path)

        elif "open outlook" in query:
            path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            speak("Opening microsoft outlook sir...")
            os.startfile(path)

        elif "open powerpoint" in query:
            path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            speak("Opening microsoft powerpoint sir...")
            os.startfile(path)

        elif "open picasa" in query:
            path = "C:\\Program Files (x86)\\Google\\Picasa3\\Picasa3.exe"
            speak("Opening picasa sir...")
            os.startfile(path)

        elif "open whatsapp" in query:
            path = "C:\\Users\\Shubh Jethwa\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak("Opening whatsapp sir...")
            os.startfile(path)

        elif "open powershell" in query:
            path = "C:\\Windows\\SysWOW64\\WindowsPowerShell\\v1.0\\powershell.exe"
            speak("Opening windows powershell sir...")
            os.startfile(path)

        elif "open extractor" in query:
            path = "C:\\Program Files (x86)\\WinRAR\\WinRAR.exe"
            speak("Opening winrar extractor sir...")
            os.startfile(path)

        elif "open word" in query:
            path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("Opening microsoft word sir...")
            os.startfile(path)

        elif "open zoom" in query:
            path = "C:\\Users\\Shubh Jethwa\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            speak("Opening zoom sir...")
            os.startfile(path)

        elif "send email" in query:
            speak("What should I say sir?")
            query = takeCommand().lower()
            if "send a file" in query:
                email = "jethwashubh32@gmail.com"   # your email address
                password = "Lucifer@1306"   # your password
                send_to_email = "itsmeshubh263@gmail.com"   # whom u are sending message to
                speak("Sir, what is the subject for this email?")
                query = takeCommand().lower()
                subject = query   # subject in the email
                speak("Sir what is the message for this email?")
                query2 = takeCommand().lower()
                message = query2  # message in the email
                speak("Sir, please enter the correct path of the file into the shell.")
                file_location = input("please enter the path here")   # file attachment in the email

                speak("Please wait sir, I am sending the email now...")

                msg = MIMEMultipart()
                msg["From"] = email
                msg["To"] = send_to_email
                msg["Subject"] = subject

                msg.attach(MIMEText(message, 'plain'))

                # setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location)
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", "attachment; filename= %s" % filename)

                # attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("Sir the email has been sent successfully...")

            else:
                email = "jethwashubh32@gmail.com"     # your email
                password = "Lucifer@1306"      # your password
                send_to_email = "itsmeshubh263@gmail.com"      # whom u are sending the message to
                message = query    # the message in the email

                server = smtplib.SMTP("smtp.gmail.com")     # connect to the server
                server.starttls()    # use TLS
                server.login(email, password)       # login to email server
                server.sendmail(email, send_to_email, message)     # send the email
                server.quit()     # logout of email server
                speak("Sir, the email has been sent successfully...")

        elif "open camera" in query:
            speak("Opening camera sir...")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:   # press ESC key to close the camera window
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "open mobile camera" in query:
            speak("Opening mobile camera sir...")
            URL = "http://10.213.207.169:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break;
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            print(ip)
            speak(f"Sir, your IP address is {ip}")

        elif "send message" in query:
            speak("Will send your message soon sir...")
            kit.sendwhatmsg("+919920964318", "this is a test message", 9, 1)   # here u can give anyone's no. whom u wish to send message, message and time
        
        elif "play songs on youtube" in query:
            speak("Playing on youtube sir...")
            kit.playonyt("see you again")   # Here you can give name of any song of your choice

        # to close any window:
        elif "close notepad" in query:
            speak("Closing notepad sir...")
            os.system("taskkill /f /im notepad.exe")

        elif "close terminal" in query:
            speak("Closing command prompt sir...")
            os.system("taskkill /f /im cmd.exe")

        elif "close adobe reader" in query:
            speak("Closing adobe reader sir...")
            os.system("taskkill /f /im AcroRd32.exe")

        elif "close code" in query:
            speak("Closing visual studio code sir...")
            os.system("taskkill /f /im Visual Studio Code.exe")

        elif "close recorder" in query:
            speak("Closing recorder sir...")
            os.system("taskkill /f /im obs64.exe")

        elif "close zoom" in query:
            speak("Closing zoom sir...")
            os.system("taskkill /f /im zoom.exe")

        elif "close excel" in query:
            speak("Closing excel sir...")
            os.system("taskkill /f /im EXCEL.EXE")

        elif "close firefox" in query:
            speak("Closing firefox sir...")
            os.system("taskkill /f /im firefox.exe")

        elif "close powerpoint" in query:
            speak("Closing powerpoint sir...")
            os.system("taskkill /f /im POWERPNT.EXE")

        elif "close whatsapp" in query:
            speak("Closing whatsapp sir...")
            os.system("taskkill /f /im WhatsApp.exe")

        elif "close powershell" in query:
            speak("Closing powershell sir...")
            os.system("taskkill /f /im powershell.exe")

        elif "close word" in query:
            speak("Closing word sir...")
            os.system("taskkill /f /im WINWORD.EXE")

        elif "close control panel" in query:
            speak("Closing control panel sir...")
            os.system("taskkill /f /im Control Panel")

        elif "close photoshop" in query:
            speak("Closing photoshop sir...")
            os.system("taskkill /f /im Photoshop.exe")

        elif "close autocad" in query:
            speak("Closing autocad sir...")
            os.system("taskkill /f /im acad.exe")

        elif "close edge" in query:
            speak("Closing microsoft edge sir...")
            os.system("taskkill /f /im msedge.exe")

        elif "close chrome" in query:
            speak("Closing google chrome sir...")
            os.system("taskkill /f /im chrome.exe")

        elif "close nitro" in query:
            speak("Closing nitro editor sir...")
            os.system("taskkill /f /im NitroPDF.exe")

        elif "close pycharm" in query:
            speak("Closing pycharm sir...")
            os.system("taskkill /f /im pychram64.exe")

        elif "close outlook" in query:
            speak("Closing microsoft outlook sir...")
            os.system("taskkill /f /im OUTLOOK.EXE")

        elif "close powershell" in query:
            speak("Closing powershell sir...")
            os.system("taskkill /f /im powershell.exe")

        elif "close picasa" in query:
            speak("Closing picasa sir...")
            os.system("taskkill /f /im Picasa3.exe")

        elif "close extractor" in query:
            speak("Closing winrar extractor sir...")
            os.system("taskkill /f /im WinRAR.exe")

        # to find location using IP address:
        elif "where am I" in query or "where are we" in query:
            speak("Please wait sir, let me check...")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = "https://get.geojs.io/v1/geo/"+ipAdd+".json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data["city"]
                # state = geo_data["state"]
                country = geo_data["country"]
                speak(f"Sir, we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry sir, but due to network issue I am not able to locate")
                pass

        # to check instagram profile:
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("Sir please enter the username correctly...")
            name = input("Enter the username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir, here is the profile of the user {name}")
            time.sleep(5)
            speak("Sir would like to download the profile picture of this user.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir, the profile picture is saved in our main folder.")
            else:
                pass

        # to take screenshot:
        elif "screenshot" in query:
            screenshot()

        # to read PDF file:
        elif "read pdf" in query:
            pdf_reader()

        # to find a joke:
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # to know cpu status:
        elif "cpu status" in query:
            cpu()

        # to hide and unhide files and folders:
        elif "hide all the files" in query or "hide the folder" in query or "visible to everyone" in query:
            speak("Sir please tell me you want to hide the folder or make it visible to everyone...")
            condition = takeCommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden...")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone...")

            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir...")

        # to do calculations:
        elif "calculations" in query or "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Sir,  what do you want to calculate, example 3 plus 3")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                try:
                    def get_operator_fn(op):
                        return {
                            '+' : operator.add,   # plus
                            '-' : operator.sub,   # minus
                            'x' : operator.mul,   # multiplied by
                            'divided' :operator.__truediv__,   # divided
                            'Mod' : operator.mod,
                            'mod' : operator.mod,
                            '^' : operator.xor,
                            }[op]
                    def eval_binary_expr(op1, oper, op2):   # 5 plus 8
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("Sir, your result is")
                    print(eval_binary_expr(*(my_string.split())))
                    speak(eval_binary_expr(*(my_string.split())))
                except Exception as e:
                    speak("Sorry sir, I am not able to calculate at the moment. Please check the numbers.")
                    pass

        # to get weather info:
        elif "climate" in query or "temperature" in query or "weather" in query: 
            search = "weather in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Sir, current {search} is {temp}")

        # to search anything:
        elif "activate how to do mode" in query:
            speak("How to do mode is activated sir...")
            while True:
                speak("Please tell me what you want to know...")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("Okay sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry sir, I am not able to find this...")

        # to know battery status:
        elif "battery" in query or "how much power" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(percentage)
            speak(f"Sir, our system has {percentage} percent battery...")
            if percentage>=75:
                speak("Sir, we have enough power to continue our work...")
            elif percentage>=40 and percentage<75:
                speak("Sir, we should connect our system to charging point to charge the battery...")
            elif percentage>20 and percentage<30:
                speak("Sir, we don't have enough power to work, please connect the charger...")
            elif percentage<=20:
                speak("Sir, we are running low on power, please connect the charger. The system will shutdown very soon")

        # to know the speed of internet:
        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir, we have {dl} bit per second downloading speed and {up} bit per second uploading speed...")

        # to send sms:
        elif "text message" in query:
            speak("Sir, what should I say...")
            msz = takeCommand()

            account_sid = "AC76f39cbffc0ba42a9b86f661ddbc2f07"
            auth_token = "79b9f9ac190ba3eba8a77f25ef1bf983"

            client = Client(account_sid, auth_token)

            message = client.message \
                .create(
                    body= msz,
                    from_ = "+17575781117",
                    to = "9920964318"   # both the numbers should be verified on twilio
                )

            print(message.sid)
            speak("Sir, your message has been sent sucessfully...")

        # to make calls:
        elif "make a call" in query:
            speak("Connecting the call sir...")

            account_sid = "AC76f39cbffc0ba42a9b86f661ddbc2f07"
            auth_token = "79b9f9ac190ba3eba8a77f25ef1bf983"

            client = Client(account_sid, auth_token)

            message = client.calls \
                .create(
                    twiml='<Response><Say>This is the message to test..</Say></Response>',
                    from_ = "+17575781117",
                    to = "9920964318"   # both the numbers should be verified on twilio
                )

            print(message.sid)

        # to control volume:
        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")

        # to set an alarm:
        elif "alarm" in query:
            speak("Sir, please tell me the time to set the alarm. for example, set alarm to 5:30 am")
            tt = takeCommand()   # set alarm to 5:30 a.m.
            tt = tt.replace("set alarm to ", "")
            tt = tt.replace(".", "")   # 5:30 am
            tt = tt.upper()   # 5:30 AM
            MyAlarm.alarm(tt)

        # to remember something:
        elif "write down something" in query or "notedown" in query:
            speak("What should I write down sir...")
            note = takeCommand()
            remember = open("data.txt", 'w')
            remember.write(note)
            remember.close()
            speak("Sir, I have noted that" + note)

        elif "do you remember anything" in query or "do you have anything" in query:
            remember = open("data.txt", 'r').read()
            speak("Sir, you told me to remember that" + remember)

        # to switch between windows:
        elif "switch windows" in query:
            speak("Switching the windows sir...")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        # to perform conversation with jarvis:
        elif "hello" in query or "hey" in query:
            speak("Hello sir, may i help you with something...")

        elif "how are you" in query or "how you doing" in query:
            speak("I am fine sir, what about you?")

        elif "fine" in query or "good" in query:
            speak("That's great to hear from you sir...")

        elif "thanks" in query or "thank you" in query:
            speak("It's my pleasure sir...")

        elif "sleep now" in query or "go to sleep" in query:
            speak("Okay sir, you can call me anytime...")
            break

        elif "exit" in query:
            speak("Thanks for using me sir, have a nice day")
            sys.exit()

        # to end the system:
        elif "shutdown the system" in query:
            speak("Do you want to shut down the system sir...")
            reply = takeCommand()
            if "yes" in reply:
                speak("Shutting down the system sir...")
                os.system("shutdown /s /t 5")
            else:
                break

        elif "restart the system" in query:
            speak("Do you want to restart the system sir...")
            reply = takeCommand()
            if "yes" in reply:
                speak("Restarting the system sir...")
                os.system("shutdown /r /t 5")
            else:
                break

        elif "log out" in query:
            speak("Do you want to log out from the system sir...")
            reply = takeCommand()
            if "yes" in reply:
                speak("Logging out from the system sir...")
                os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")    # if this is not working then use "shutdown -1"
            else:
                break

if __name__ == '__main__':
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            TaskExecution()