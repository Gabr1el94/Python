import speech_recognition as sr
import playsound as pl
import pyttsx3
import os


voz= 'brazil+f4'
recon = sr.Recognizer()
em = pyttsx3.init() 
em.setProperty('voice',voz)
em.setProperty('rate',140)
em.setProperty('volume', 1)
em.say("Olá senhor, se você deseja ouvir a sua música"+ 
        "favorita responda 'sim', caso ao contrário, responda 'não' ")
em.runAndWait()

with sr.Microphone() as source:
    recon.adjust_for_ambient_noise(source,duration=3)
    print("...")
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio,language="pt-br")

    #Se desejar fechar o programa! if resposta == "fechar" : break

if resposta == "sim":
        em.say("Ok , Executando a música...")
        em.setProperty('voice',voz)
        em.setProperty('rate',140)
        em.setProperty('volume', 1)
        em.runAndWait()
        os.system('vlc reconhecimento-voz/integracao-sintetizacao-reconhecimentoVoz/musica.mp3.mp3')
elif resposta == "não":
        em.say("Ok , Solicitação negada!")
        em.setProperty('voice',voz)
        em.setProperty('rate',180)
        em.setProperty('volume', 1)
        em.runAndWait()