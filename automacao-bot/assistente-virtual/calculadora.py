from config import conversas 

def frase_to_list(text):
    lista = list(text.split(" "))
    
    while "" in lista:
        lista.remove("")

    return lista

def operacoes_matematica(respVoz):
    listText = frase_to_list(respVoz)
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
        return "Operação não enctontrada!"