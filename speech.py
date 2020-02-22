import speech_recognition as sr
import sys

def countLikes(text):
    count = 0
    words = text.split(" ")
    for w in words:
        w = w.lower()
        if (w == "like"):
            count += 1
    return count

filename = input("Enter your text file name: ")

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r1.energy_threshold = 2000
r1.pause_threshold = .2
r2.energy_threshold = 2000
r2.pause_threshold = 3


fulltext = ""
print ("Say something!")

while True:
    with sr.Microphone() as source:
        audio = r1.listen(source)
        r2.listen(audio)
    try:
        text = r1.recognize_google(audio)
        print(text, end="")
        fulltext += text
    except:
        print("Could not dictate.")
        sys.exit()
    
print("Done!")
file = open("textfiles/" + filename, "a+")
file.write(text)
likeCount = countLikes(text)
print("You said 'like' " + str(likeCount) + " times!")
