# coding=utf-8
from gtts import gTTS
from io import BytesIO
import playsound

#Insert text and caracter
sound = 'hello.mp3'
message = 'Olá Mundo, Seja bem-vindo'

def play_audio(audio):
    playsound.playsound(sound)

def convert_to_audio(texto,play):
    tts = gTTS(texto.decode("utf-8"),lang='pt-br')
    tts.save(play)
    play_audio(play)


convert_to_audio(message,sound)