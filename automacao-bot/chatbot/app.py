# -*- coding: utf-8 -*- 
#Caso falte o módulo na hora de iniciar: pip install chatterbot_corpus
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from datetime import datetime
import os

def horario_para_texto(horario):
    if horario < 12 :
        return 'Bom dia'
    elif horario < 18 :
        return 'Boa tarde'
    else:
        return 'Boa noite'

bot = ChatBot('Ron Obvious')
date = datetime.now()
trainer = ListTrainer(bot)

msgHorario =  horario_para_texto(date.hour)

conveW = ['oi',
'olá, '+os.getlogin()+"  "+horario_para_texto(date.hour),
 horario_para_texto(date.hour),'como vai?',
'estou bem','Que ótimo!']

convFilmes = ['Que filmes que você gosta?',
'eu gosto do "Os Vingadores"']

convClosed = ['fechar o programa',
'Fechando e até mais :) ...']

trainer.train(conveW)
trainer.train(convFilmes)
trainer.train(convClosed)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    if float(response.confidence) > 0.5:
        print('Bot:', response)
        if quest == 'fechar o programa' : 
            break
    else:
        print('Bot: Não entendi!')