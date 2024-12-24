# Chequear sintaxis y uso de HTTP services
# httpbin.org

import requests
import os
import json


if __name__ == '__main__':
    os.system('clear')    # Clears the screen
    print('-'*40)
    
    url = 'http://httpbin.org/get'
    args = {'nombre': 'Omar', 'curso': 'Python', 'nivel': 'Intermedio'}
    response = requests.get(url, params=args)
    
    if response.status_code == 200:
        '''
        response_json = response.json()
        origin = response_json['origin']
        '''
        
        
        response_json = json.loads(response.text)
        origin = response_json['origin']


        print('IP origen: ', origin)
