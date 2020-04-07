from climaTemp import previsao_do_tempo,clima_e_tempo
from calculadora import operacoes_matematica

version = "1.2.1"
boas_vindas = "Olá, por favor informe o seu nome:"


def intro():
    msg = "Assistente - versão {} / por: Gabriel Soares".format(version)
    clima_tempo = previsao_do_tempo()
    print("-"*len(msg)+"\n{}\n{}\n".format(msg,clima_tempo)+"-"*len(msg))

lista_erro = [
    "Não entendi nada",
    "Desculpa, não entendi",
    "Repita novamente por favor!",
    "Solicitação negada"
]

conversas = {
    "Olá": "oi, tudo bem?",
    "sim e você": " Estou bem e obrigada por perguntar"
}

comandos = {
    "desligar":"desligando",
    "reiniciar":"reiniciando"
}

def verificar_nome(username):
    if username.startswith("Meu nome é"):
        username = username.replace("Meu nome é","")
    
    if username.startswith("Eu me chamo"):
        username = username.replace("Eu me chamo","")
    
    if username.startswith("Eu sou a"):
        username = username.replace("Eu sou a","")

    if username.startswith("Eu sou a"):
        username = username.replace("Eu sou a","")

    if username.startswith("Sou o"):
        username = username.replace("Sou o","")
    
    if username.startswith("Sou a"):
        username = username.replace("Sou a","")

    return username

def verificar_nome_exist(nome):
    dados = open("dados/nomes.txt","r")
    nomes = dados.readlines()

    if not nomes:
        vazio = open("dados/nomes.txt","r")
        conteudo = vazio.readlines()
        conteudo.append("{}".format(nome))
        vazio = vazio = open("dados/nomes.txt","w")
        vazio.writelines(conteudo)
        vazio.close()

        return "Olá {}, prazer em te conhecer!".format(nome)
    
    for linha in nomes:
        if linha == nome:
            return "Olá {}, acho que já nos conhecemos".format(nome)
    
    vazio = open("dados/nomes.txt","r")
    conteudo = vazio.readlines()
    conteudo.append("\n{}".format(nome))
    vazio = vazio = open("dados/nomes.txt","w")
    vazio.writelines(conteudo)
    vazio.close()

    return "Oi {} é a primeira vez que nos falamos".format(nome)

def name_list():
    try:
        nomes = open("dados/nomes.txt","r")
        nomes.close()
    except FileNotFoundError:
        nomes = open("dados/nomes.txt","w")
        nomes.close()

def tipo_funcao(entrada):
    result = ''

    if "quanto é" in entrada.lower():
        calculo = entrada.replace('quanto é',"")
        result = operacoes_matematica(calculo)
    elif "mostrando informações da cidade" in entrada.lower():
        cidade = entrada.replace("mostrando informações da cidade","")
        result = clima_e_tempo(cidade.strip())
    else:
        result = conversas[entrada]
    
    return result