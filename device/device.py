
import json, requests
import playsound

url = requests.get("https://jsonplaceholder.typicode.com/users")
text = url.text

data = json.loads(text)

user = data[0]

user = data[0]
signal = user['name']

if signal=='Leanne Graham':
    playsound.playsound('./audio/letwe.wav')
    