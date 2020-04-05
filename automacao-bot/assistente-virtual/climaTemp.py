import urllib3,json

def cidade_estado_pais(ip):
    http = urllib3.PoolManager()
    url = 'http://ip-api.com/json/{}'.format(ip)
    resp = http.request('GET',url)
    locationJSON = json.loads(resp.data.decode('UTF-8')) 
    return "{}, {} - {}".format(locationJSON['city'],locationJSON['region'],locationJSON['country'])

def previsao_do_tempo(ipLocal):
    cidade_estado = cidade_estado_pais(ipLocal)
    return ""