import speech_recognition as sr
import sys
import pydub
from pydub import AudioSegment

def mp32string():
	inputfile = './input/search.mp3'
	sound = pydub.AudioSegment.from_mp3(inputfile)
	sound.export('./input/input.wav', format="wav")
	r = sr.Recognizer()
	audiofile = sr.AudioFile('./input/input.wav')
	with audiofile as source:
	    audio = r.record(source)
	text = r.recognize_google(audio)
	return text

if __name__ == "__main__":
	mp32string()