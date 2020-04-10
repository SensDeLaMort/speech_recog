import speech_recognition as sr


recog = sr.Recognizer()

with sr.Microphone() as source:
	print('speak, my boy')
	audio = recog.listen(source)

	voice_data = recog.recognize_google(audio)
	print(voice_data)
