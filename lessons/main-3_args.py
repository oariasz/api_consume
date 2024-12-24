# Chequear sintaxis y uso de HTTP services
# httpbin.org

import requests
import os


if __name__ == '__main__':
    os.system('clear')    # Clears the screen
    print('-'*40)
    
    url = 'http://httpbin.org/get'
    args = {'nombre': 'Omar', 'curso': 'Python', 'nivel': 'Intermedio'}
    response = requests.get(url, params=args)
    
    if response.status_code == 200:
        content = response.text
        print(content)
