import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('OSR_us.wav')
'''make sure that the voice format extension should be in wav file, the audio should not
exceed more than 30 sec'''
with harvard as source:
 r.adjust_for_ambient_noise(source,duration=4)    
 audio = r.record(source)
 type(audio)
 txt = r.recognize_google(audio)
 print(txt)