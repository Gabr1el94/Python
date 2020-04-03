import speech_recognition as sr
import pyttsx3 as pyx
from random import choice
import config


reproducao = pyx.init()


#Função para sair o som
def sai_som(resposta):
    reproducao.getProperty('voice','brazil+f4')
    reproducao.setProperty('rate',140)
    reproducao.setProperty('volume', 1)
    reproducao.say(resposta)
    reproducao.runAndWait()

#Realizando loop da fala e reconhecimento de voz
while True:
    resposta_erro_aleatoria = choice(config.lista_erro)
    recon = sr.Recognizer()

    #Abrindo o microfone
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source,duration=3)
        
        while True:
            try:
                #Ouvindo o usuário
                audio = recon.listen(source)
                entrada = recon.recognize_google(audio,language='pt-br')
                print("Você disse: {}".format(entrada))

                resposta = config.conversas[entrada]

                print('Assistente: {}'.format(resposta))
                sai_som(resposta)
            except sr.UnknownValueError:
                sai_som(resposta_erro_aleatoria)

'''
    resposta_erro_aleatoria = choice(lista_erro)
    fala = reconhece(resposta_erro_aleatoria)
    print(fala)
    sai_som(fala)
'''