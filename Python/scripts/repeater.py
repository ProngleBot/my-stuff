while True:
    sentence = input('Enter the sentence that is to be repeated: ')
    amount = input(f'How many times do you want to repeat "{sentence}"?')
    for amount in range(0,int(amount)):
        print(sentence)