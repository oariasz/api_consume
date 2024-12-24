# Chequear sintaxis y uso de HTTP services
# httpbin.org

import requests
import os
import json


if __name__ == '__main__':
    os.system('clear')    # Clears the screen
    print('-'*20)
    
    url = 'http://httpbin.org/put'
    # args = {'nombre': 'Omar', 'curso': 'Python', 'nivel': 'Intermedio'}
    payload = {'nombre': 'Omar', 'curso': 'Python', 'nivel': 'Intermedio'}
    headers = {'Content-Type': 'application/json', 'access-token': '123456'}
    
    # Para pasarlos al argumento data del json debo hacer:
    response = requests.put(url, data=json.dumps(payload), headers=headers)

    
    print(response.url)
    if response.status_code == 200:
        # print(response.text)
        headers_response = response.headers
        server = headers_response['server']
        print(server)

    response = requests.get(url)
    print('Cómo quedó el url = ', url)
    if response.status_code == 200:
        # print(response.text)
        headers_response = response.headers
        server = headers_response['server']
        print(response.header)
        print(response.text)
    