import requests

chuckrequest = f'https://api.chucknorris.io/jokes/random'
chuckjoke = requests.get(chuckrequest).json()

print(chuckjoke['value'])