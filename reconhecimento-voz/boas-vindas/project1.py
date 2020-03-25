# coding=utf-8

import pyttsx
from datetime import datetime

agora = datetime.now()

nome = "Gabriel"
horas = agora.hour
minutos = agora.minute

texto = "Olá %s sejá bem vindo, agora são %d horas e %d minutos" % (nome,horas,minutos)

print(texto)

em = pyttsx.init()
em.setProperty("rate",125)
em.setProperty("volume",1)
em.setProperty("voice",'brazil+f4')
em.say(texto.decode("utf-8"))
em.runAndWait()