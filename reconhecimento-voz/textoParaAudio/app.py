# coding=utf-8
from gtts import gTTS
import os.path
import playsound

diretorio = raw_input('Informe o diretório arquivo de texto:')
print(diretorio)
teste = os.path.isfile(diretorio)

if teste == True:
    print("O arquivo está sendo carregado. Aguarde...")
    file_data = open(diretorio)
    file_data = file_data.read()
    
    print("Salvando o arquivo ...")
    voz = gTTS(file_data.decode("utf-8"),lang='pt')
    voz.save("voz.mp3")
    print("Falando ...")
    playsound.playsound("voz.mp3")
else:
    print("Diretório não foi encontrado !")