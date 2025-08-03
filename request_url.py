import sys
import requests

resp = requests.get(sys.argv[2], allow_redirects=True)

path = f"{sys.argv[1]}"

with open(path, 'wb') as file:
    file.write(resp.content)
