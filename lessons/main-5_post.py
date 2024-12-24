# Chequear sintaxis y uso de HTTP services
# httpbin.org

import requests
import os
import json


if __name__ == '__main__':
    os.system('clear')    # Clears the screen
    print('-'*20)
    
    url = 'http://httpbin.org/post'
    # args = {'nombre': 'Omar', 'curso': 'Python', 'nivel': 'Intermedio'}
    payload = {'nombre': 'Omar', 'curso': 'Python', 'nivel': 'Intermedio'}
    # Para pasarlos al argumento data del json debo hacer:
    response = requests.post(url, json=payload)
    # Otra manera es serializar con json.dumps() nosotros y pasarlo al argumento data. Es el más usado, sobre todo con PUT
    response = requests.post(url, data=json.dumps(payload))
    
    print(response.url)
    if response.status_code == 200:
        print(response.text)
