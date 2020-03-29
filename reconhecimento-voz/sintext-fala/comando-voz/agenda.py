import speech_recognition as sr 
import os

recon = sr.Recognizer()
with sr.Microphone() as source:
    print("Olá Usuário, Deseja abrir sua agenda?")
    audio = recon.listen(source)

resposta = recon.recognize_google(audio, language="pt-br")
print(resposta.upper()+"!")

if resposta == 'sim':
    print("Abrindo Agenda...")
    os.system(r"gedit < Direct >")
elif resposta == 'não':
    print("Solicitação negada!")