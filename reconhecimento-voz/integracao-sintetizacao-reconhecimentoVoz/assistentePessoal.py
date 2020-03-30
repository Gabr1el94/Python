import pyttsx3
import speech_recognition as sr
import webbrowser as wb

voz='brazil+f4' 
recon = sr.Recognizer()
en = pyttsx3.init()
en.setProperty('voice',voz)
en.setProperty('rate',140)
en.setProperty('volume',1)
en.say("Olá senhor, o que você deseja fazer neste momento:")
en.runAndWait()

with sr.Microphone() as source:
    audio = recon.listen(source)
    resposta = recon.recognize_google(audio, language='pt-br')
    print(resposta)

if resposta.lower() =="desejo acessar o google":
    en.say("Ok , abrindo o google...")
    en.setProperty('voice',voz)
    en.setProperty('rate',140)
    en.setProperty('volume', 1)
    en.runAndWait()
    wb.open("www.google.com")
elif resposta.lower()=="desejo acessar as notícias":
    en.say("Ok , abrindo as notícias...")
    en.setProperty('voice',voz)
    en.setProperty('rate',140)
    en.setProperty('volume', 1)
    en.runAndWait()
    wb.open("www.g1.globo.com")
elif resposta.lower() == "desejo abrir o youtube":
    en.say("Ok , abrindo o youtube...")
    en.setProperty('voice',voz)
    en.setProperty('rate',140)
    en.setProperty('volume', 1)
    en.runAndWait()
    wb.open("www.youtube.com")
else:
    en.say("Desculpe, não conseguir compreender a sua solicitação!")
    en.setProperty('voice',voz)
    en.setProperty('rate',140)
    en.setProperty('volume', 1)
    en.runAndWait()