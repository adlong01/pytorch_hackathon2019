import speech_recognition as sr
import sys
inputfile = './input/'+ sys.argv[1]
r = sr.Recognizer()
audiofile = sr.AudioFile(inputfile)
with audiofile as source:
    audio = r.record(source)
text = r.recognize_google(audio)
print(text)
