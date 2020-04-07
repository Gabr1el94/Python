import requests as req
import urllib3,json

def buscar_ip():
    ipResult = req.get('https://api.ipify.org').text 
    return ipResult

def cidade_estado_pais():
    ip = buscar_ip()
    http = urllib3.PoolManager()
    url = 'http://ip-api.com/json/{}'.format(ip)
    resp = http.request('GET',url)
    locationJSON = json.loads(resp.data.decode('UTF-8'))
    return [locationJSON['city'],locationJSON['region'],locationJSON['country']]

def clima_e_tempo(cidade):
    #"http://api.openweathermap.org/data/2.5/weather?appid=YOURKEYHERE&q=
    url_api = "http://api.openweathermap.org/data/2.5/weather?appid=0174eae3226a4762ebb0e5b42e7463d5&q="
    url = url_api+cidade
    infos = req.get(url).json()

    #Coordenadas
    longitude = infos['coord']['lon']
    latitude = infos['coord']['lat']

    #main
    temp_atual = infos['main']['temp'] - 273.15 # - Kelvin para Celsius
    pressao_atm = infos['main']['pressure'] / 1013.25 # - Libras para ATM
    humidade = infos['main']['humidity']  #Porcentagem
    temp_max = infos['main']['temp_max'] - 273.15
    temp_min = infos['main']['temp_min'] - 273.15
    
    #Vento
    v_speed = infos['wind']['speed'] #km / h
    v_direc = infos['wind']['deg']

    #clouds
    nebulosidade = infos['clouds']['all']

    #city 
    id_city = infos['id']

    return [longitude,latitude,temp_atual,pressao_atm,
            humidade,temp_max,temp_min,
            v_speed,v_direc,nebulosidade,id_city]
    

def previsao_do_tempo():
    info_ip = cidade_estado_pais()
    info_clima_tempo = clima_e_tempo(info_ip[0])
    return "{}, {} - {} | Temperatura Atual: {}ºC".format(info_ip[0],
    info_ip[1],info_ip[2],info_clima_tempo[2])