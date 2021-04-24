import urllib.request
import requests
import time

def download(url, filename):
    hdrs = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

    #filename = url.split("/")[-1]
    with open(filename, 'wb') as handle:
        response = requests.get(url, timeout = 2.5, headers = hdrs, stream=True)
        if not response.ok:
            print(response)
            
        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
