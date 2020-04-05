import netifaces as ni
import urllib3,json

def buscar_ip():
    gateway = ni.gateways()
    ipResult = gateway.get(2)[0][0]
    return ipResult

def cidade_estado_pais():
    ip = buscar_ip()
    http = urllib3.PoolManager()
    url = 'http://ip-api.com/json/{}'.format(ip)
    resp = http.request('GET',url)
    locationJSON = json.loads(resp.data.decode('UTF-8')) 
    return "{}, {} - {}".format(locationJSON['city'],locationJSON['region'],locationJSON['country'])

def previsao_do_tempo():
    cidade_estado = cidade_estado_pais()
    return cidade_estado