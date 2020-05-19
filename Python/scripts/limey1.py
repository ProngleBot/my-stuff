import requests,time
x = 0
def cats(x):
    for __ in range(6):
        x = x+1
        cat = requests.get('https://api.thecatapi.com/v1/images/search')
        cat = cat.json()[0]['url']
        print(f'{x} {cat}')
def dice(x):
    for __ in range(6):
        x = x+1
        result = requests.get('http://roll.diceapi.com/json/d6/d6')
        dice1 = result.json()['dice'][0]['value']
        dice2 = result.json()['dice'][1]['value']
        print(f'this is dice 1 {dice1}')
        print(f'this is dice 2 {dice2}')
        print(x)
        if dice1 == 4:
            print('oh shit')
p = input('cat or dice ').lower()
if p == 'cat':
    cats(x)
else:
    dice(x)