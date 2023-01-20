import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

def speechtext():
    rec = sr.Recognizer();
    with sr.Microphone() as source :
        print("Listening ...");
        rec.adjust_for_ambient_noise(source);
        audio = rec.listen(source);
        try :
            print("Recognizing...");
            data = rec.recognize_google(audio);
            return data;
        except sr.UnknownValueError:
            print("Not Understand");          

def speech(x):
    en = pyttsx3.init();
    voice = en.getProperty("voices")
    en.setProperty('voice', voice[1].id)
    rate = en.getProperty("rate");
    en.setProperty("rate",140);
    en.say(x);
    en.runAndWait();

if __name__ == '__main__':

    if speechtext().lower() == "hello" :
       speech("Yes");
       while True : 
        data1 = speechtext().lower();
        if "your name" in data1 :
            name = " My name is alexa";
            speech(name);
        elif "old are you" in data1 :
            age = "I am 5 years old";
            speech(age);    
        elif "time" in data1 :
            ti = datetime.datetime.now().strftime("%I%M%p");
            speech(ti);    
        elif "bye" in data1:
            speech("bye bye, take care !!");
            break;
        elif "youtube" in  data1:
            speech("ok");
            webbrowser.open("https://www.youtube.com/");
        elif "about yourself" in data1 :
            y = "My name is alexa I am 5 years old. I can speak with you and also I can help you for opening youtube and google . I am not much intelligent yet but i will be in future . Thank you !" ;
            speech(y);           
        elif "google" in data1 :
            speech("ok");
            webbrowser.open("google.com")    
        elif "are you" in data1:
            y="I am Fine";
            speech(y);    
        elif "cricbuzz" in data1:
            speech("ok");
            webbrowser.open("https://www.cricbuzz.com/");    
    else :
        print("Thanks");    
        