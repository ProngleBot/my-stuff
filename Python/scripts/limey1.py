import requests
def quotes():
    request = requests.get('https://breaking-bad-quotes.herokuapp.com/v1/quotes')
    request = request.json()
    quote = request[0]['quote']
    author = request[0]['author']
    print(f'Quote : {quote}\nAuthor : {author}')
    while True:
        x = input('Press Enter to get another quote or type exit to exit!: ')
        if x == 'exit':
            print('bye!')
            exit()
        else:
            quotes()
quotes()