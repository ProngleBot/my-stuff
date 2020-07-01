import random
def rockps():
    print('\nROCK PAPER SCISSORS BITCH\n')
    rps = ['rock','paper','scissors']
    rock = ('rock','r')
    paper = ('paper','p')
    scissors = ('scissors','s')
    computer = random.choice(rps)
    
    player = input('Rock paper or scissors? do r,p,s: ').lower()
    
    if computer in rock:
        if player in rock:
            print(f'it was a tie')
            rockps()
        elif player in paper:
            print(f'You chose rock and I chose {computer} so I lose B(')
            rockps()
        else:
            print(f'You chose rock and I chose {computer} so I win B)')
            rockps()
    
    elif computer in paper:
            if player in paper:
                print(f'it was a tie')
                rockps()
            elif player in scissors:
                print(f'You chose paper and I chose {computer} so I lose B(')
                rockps()
            else:
                print(f'You chose paper and I chose {computer} so I win B)')
                rockps()
    
    elif computer in scissors:
            if player in scissors:
                print(f'it was a tie')
                rockps()
            elif player in rock:
                print(f'You chose scissors and I chose {computer} so I lose B(')
                rockps()
            else:
                print(f'You chose scissors and I chose {computer} so I win B)')
                rockps()
    
    else:
        print(f'{player} is neither rock, paper or scissors please try again')
        rockps()
rockps()