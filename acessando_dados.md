# JSON
import json
import requests

data = requests.get(url).text
data = json.loads(data)
print(type(data))
print(data)
print(data['coluna'])


http://ws.audioscrobbler.com/
/2.0/?method=geo.gettopartists&country=spain&api_key=YOUR_API_KEY&format=json
