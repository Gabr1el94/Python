# -*- coding: utf-8 -*- 
#Caso falte o módulo na hora de iniciar: pip install chatterbot_corpus
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Ron Obvious')

conversation = ['oi','olá', 
'olá,bom dia',
'bom dia, como vai?',
'estou bem' ]

convFilmes = ['Que filmes que você gosta?',
'eu gosto de Resident Evil']

trainer = ListTrainer(bot)
trainer.train(conversation)
trainer.train(convFilmes)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    if float(response.confidence) > 0.5:
        print('Bot:', response)
    else:
        print('Bot: Não entendi!')