import pyttsx3                    #pip install pyttsx3
import speech_recognition as sr   #pip install speechRecognition
#import wikipedia                 #pip install wikipedia
import wikipediaapi               #pip install wikipedia-api
import webbrowser
import datetime
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    # It takes microphone input from the user and returns string output
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
      #  query = takeCommand().lower()
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('user@gmail.com', 'urPassword')
    server.sendmail('user@gmail.com', to, content)
    server.close()

#main function
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            if query:  # Check if the query is not empty
                try:
                    wiki_wiki = wikipediaapi.Wikipedia(user_agent='AI Virtual Assistant/1.0', language='en')
                    page = wiki_wiki.page(query)
                    if page.exists():
                        results = page.summary[:1000]  # Get the first 500 characters of the summary
                        speak("According to Wikipedia")
                        # Print results with encoding to avoid Unicode errors
                        print(results.encode('ascii', 'ignore').decode('ascii'))
                        speak(results)
                    else:
                        speak("Sorry, I couldn't find anything on Wikipedia for your query.")
                except Exception as e:
                    print("An error occurred while fetching Wikipedia results:", e)
                    speak("Sorry, I couldn't fetch the Wikipedia results.")
            else:
                speak("Please specify what you want to search on Wikipedia.")

        elif 'open gpt' in query:
            speak("Opening ChatGPT in Google Chrome...")
            try:
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Path to Chrome
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab("https://chat.openai.com/")
                speak("ChatGPT is now open.")
            except Exception as e:
                print("An error occurred while opening ChatGPT:", e)
                speak("Sorry, I couldn't open ChatGPT.")

        elif 'open youtube' in query:
            speak("Yes sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Yes sir")
            webbrowser.open("google.com")       
        
        elif 'play music' in query:
            speak("Yes sir")
            music_dir = "C:\\Users\\Deepak\\Music\\Music"
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    value = random.randint(0, len(songs) - 1)
                    os.startfile(os.path.join(music_dir, songs[value]))
                else:
                    speak("No songs found in the music directory.")
            else:
                speak("Music directory does not exist.")

        elif 'play video' in query:
            speak("Yes sir")
            video_dir = r"D:\Videos\#Songs Videos"
            if os.path.exists(video_dir):
                videos = os.listdir(video_dir)
                if videos:
                    value = random.randint(0, len(videos) - 1)
                    os.startfile(os.path.join(video_dir, videos[value]))
                else:
                    speak("No videos found in the video directory.")
            else:
                speak("Video directory does not exist.")


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")    
            print(strTime)
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            speak("Yes sir")
            codePath = "C:\\Users\\deepak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            speak("Yes sir")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)    

            
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "test1@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent:",content)
                speak("Email has been sent!")
            except Exception as e:
                print("\nSORRY!MAIL NOT SENT")
                speak("Sorry deepak bhai. I am not able to send this email")    


        elif 'exit' in query:
            speak("Yes sir")
            exit()        
