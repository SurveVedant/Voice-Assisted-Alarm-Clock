import speech_recognition as s_r
import os
import datetime
from playsound import playsound

r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=0)
with my_mic as source:
    print("What hour of 12hr clock do you want the alarm to ring? :")
    r.adjust_for_ambient_noise(source)
    audio1 = r.listen(source,phrase_time_limit=5)
a  = print(r.recognize_google(audio1))

with my_mic as source:
    print("What minute of an hour do you want the alarm to ring? :")
    r.adjust_for_ambient_noise(source)
    audio2 = r.listen(source,phrase_time_limit=5)
b = print(r.recognize_google(audio2))

with my_mic as source:
    print("Do you want alarm to ring at am or pm? :")
    r.adjust_for_ambient_noise(source)
    audio3 = r.listen(source,phrase_time_limit=10)
c = print(r.recognize_google(audio3))

hour = int(r.recognize_google(audio1))
minutes = int(r.recognize_google(audio2))
ampm = str(r.recognize_google(audio3))

print("Waiting for alarm",hour,":",minutes,ampm,)

if (ampm == "pm"):
    hour = hour + 12

while(1 == 1):
    if(hour == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute) :
        print("Time to wake up")
        playsound('E:\\Songs\\ring tones\\take on me.mp3')
        break
