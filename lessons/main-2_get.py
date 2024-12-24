import requests

if __name__ == '__main__':
    url = 'https://www.google.com.mx'
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content
        file = open('google.html', 'wb')
        with file:
            file.write(content)
            print('Done!')