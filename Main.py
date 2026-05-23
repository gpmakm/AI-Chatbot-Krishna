import wikipedia
import win32com.client
import JavaModule as jm 
import pyjokes

#Set sapi.SpVoice=sapi.Getvoices.Item(1)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
#speaker.Speak("Hello, it is MaYa")
# print("Welcome to AI world")

def openWikipedia():
    title=input(("Enter your topic to get knowledge dude-"))
    limit=int(input("Enter your limit for the discussion in sentences-"))
    result=wikipedia.summary(title,sentences=limit)
    choice = int(input("Enter your choice for output\n \t 0. For Textual Output \t 1.For Voice output \t2.For voice "
                       "result with then textual result--"))
    if choice == 0:
        print(result)
    elif choice == 1:
        speaker.Speak(result)
    elif choice == 2:
        speaker.Speak(result)
        print(result)
    else:
        print("Bye")

jm.intro()
jm.greet()

tool=input("How is your day? How may i help you?")
if "to know about" in tool:
    openWikipedia()
# elif tool=="Java Notes":
    # openJavaNotes()

# result=wikipedia.summary(topic,sentences=num)

# for i in range(1,5,1):
#     joke = pyjokes.get_joke(language="en", category="twister")
#     print(joke)
