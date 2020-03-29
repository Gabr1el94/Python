import speech_recognition as sr
import math

def frase_to_list(text):
    lista = list(text.split(" "))
    return lista

def tipo_calculo(respVoz):
    listText = frase_to_list(resposta)
    operador = listText[1].lower()
    if operador == "+" :
        return "Sua Adição de "+respVoz+":"+ str(int(listText[0]) + int(listText[2]))
    elif operador == "-":
        return "Sua Subtração de "+respVoz+":"+ str(int(listText[0]) - int(listText[2]))
    elif operador == "x":
        return "Sua Multiplicação de "+respVoz+":"+ str(int(listText[0]) * int(listText[2]))
    elif operador == "/":
        return "Sua Divisão de "+respVoz+":"+ str(int(listText[0]) / int(listText[2]))
    else:
        return False

recon = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        recon.adjust_for_ambient_noise(source,duration=3)
        print("Descreva o seu cálculo:")
        audio = recon.listen(source)
        
        resposta = recon.recognize_google(audio,language="pt-br")
        #Se desejar fechar o programa!
        if resposta == "fechar" : break

        txtExibido = tipo_calculo(resposta)

        if (txtExibido == False) :
            print("Not found!")
            continue

        print(txtExibido)