import speech_recognition as sr
import pyttsx3 as pyx
from random import choice
from config import *
from calculadora import operacoes_matematica


reproducao = pyx.init()


#Função para sair o som
def sai_som(resposta):
    reproducao.getProperty('voice','brazil+f4')
    reproducao.setProperty('rate',140)
    reproducao.setProperty('volume', 1)
    reproducao.say(resposta)
    reproducao.runAndWait()

def assistente():
    #Realizando loop da fala e reconhecimento de voz
    print(boas_vindas)
    sai_som(boas_vindas)
    while True:
        resposta_erro_aleatoria = choice(lista_erro)
        recon = sr.Recognizer()

        #Abrindo o microfone
        with sr.Microphone() as source:
            
            recon.adjust_for_ambient_noise(source,duration=3)
            
            while True:
                try:

                    #Ouvindo o usuário
                    audio = recon.listen(source)
                    user_name = recon.recognize_google(audio,language='pt-br')
                    user_name = verificar_nome(user_name)
                    name_list()
                    apresentacao = "{}".format(verificar_nome_exist(user_name))
                    print(apresentacao)
                    sai_som(apresentacao)

                    #guardando o nome completo
                    brute_user_name = user_name
                    user_name = user_name.split(" ")
                    user_name = user_name[0]
                    break
                except sr.UnknownValueError:
                    sai_som(resposta_erro_aleatoria)
            break

    print("="*len(apresentacao))
    print("Ouvindo...")
    while True:
        
        resposta_erro_aleatoria = choice(lista_erro)
        recon = sr.Recognizer()

        #Abrindo o microfone
        with sr.Microphone() as source:
            recon.adjust_for_ambient_noise(source,duration=3)
            
            while True:
                try:
                    #Ouvindo o usuário
                    audio = recon.listen(source)
                    entrada = recon.recognize_google(audio,language='pt-br')
                    print("{}: {}".format(user_name,entrada))
                    
                    resposta = operacoes_matematica(entrada)

                    print('Assistente: {}'.format(resposta))
                    sai_som(resposta)

                except sr.UnknownValueError:
                    sai_som(resposta_erro_aleatoria)

if __name__=='__main__':
    intro()
    sai_som("Iniciando...")
    assistente()