import requests
import pprint as pp
requests = requests.get('https://api.giphy.com/v1/gifs/random?api_key=wa7IN1SXwDMSS4vLDuNyacpMx6iNXSeP&tag=weather&rating=G')
thumbnail = requests.json()
thumbnail = thumbnail['data']['images']['original']['url']
pp.pprint(thumbnail)