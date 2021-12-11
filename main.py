import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return(info.lower())
    except:
        pass
def send_email(receiver,subject,message):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("tt9615842@gmail.com", "tingtongpongpong")
    email=EmailMessage()
    email["From"] = "tt9615842@gmail.com"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)
    talk("done,your email has been delvered sucessfully")
    """server.sendmail("tt9615842@gmail.com",
                    "itsmotionarticles@gmail.com",
                    "please use "
                )"""
email_list={
    "home": "ahzam.akhtar@gmail.com",
    "motion": "itsmotionarticles@gmail.com",
}
def get_email_info():
    talk("welcome to email bot")
    talk("just say the name   subject and message of the email")
    talk("to whom do you want to send email")
    name=get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What is the Subject of ypur email")
    subject=get_info()
    talk("Tell me the message in your email")
    message=get_info()
    send_email(receiver, subject, message)
get_email_info()