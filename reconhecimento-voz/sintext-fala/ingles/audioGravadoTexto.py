import speech_recognition as sr
import os.path

def call_audio_to_texto(arquivo):

    recon = sr.Recognizer()
    
    with sr.AudioFile(arquivo) as source:
        audio = recon.record(source)
        print("---------------------------")
    
    print(recon.recognize_sphinx(audio))

diretorio = input('Informe o diretório arquivo de audio:')

teste = os.path.isfile(diretorio)

if teste == True:
    call_audio_to_texto(diretorio)
else:
    print("O arquivo não foi encontrado !")