# Obs: No momento só funciona com a versão 3.6
import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        #Ajuste no ambiente
        recon.adjust_for_ambient_noise(source,duration=3)
        print("Diga alguma coisa...")
        audio = recon.listen(source)
        print(recon.recognize_sphinx(audio))