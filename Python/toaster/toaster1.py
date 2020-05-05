#important stuff
import pyautogui,time,random,gspread,pprint
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sheet = client.open('toasters donations').sheet1
pp = pprint


#Functions
def rosecalc():
    print('Congrats all roses have been donated!')
rosecalc()

def gifter():
    print('----------Menu----------')
    global x
    p = input('\nEnter Amount you have here: ').lower()
    if p == 'm':
        ui()
    else:
        x = float(p)
        x = int(x/50)
        if x <= 1:
            print(f'{x}rose is about to be gifted')
        else:
            print(f'{x}roses are about to be gifted')
        def typer():
            time.sleep(2)
            pyautogui.hotkey('ctrl','a','delete')
            pyautogui.write('.gift rose emotionaltoast',interval=0.06)
            pyautogui.press('enter')
            counter()
        def counter():
            global x 
            x = x - 1 
            if x == 1:
                print(f'{x} rose left')
            elif x == 0:
                print('no roses left')
                ui()
            else:
                print(f'{x} roses left')
        time.sleep(1)
        for _ in (range(1,x+1)):
            typer()

def lister():
    what = ["cats" ,"cheese",'routers']
    chooser = random.choice(what)
    print(f'=================directory mode===================\ni heard you like {chooser}',)
    def listall():
        printout = sheet.get_all_records()
        for x in printout:
            for k,v in x.items():
                print(k,v)
    def addtolist():
        sheet.append_rows(cols=2)
def quitter():
    re_list = ['Dingus','doofus','banana peel','big dumb dumb',]
    ope = random.choice(re_list)
    question = input('\nare you sure you want to quit?[y/n]\n').lower()
    if question == 'n':
        print(f'\n================================\nmake up your mind you {ope}')
        ui()
    elif question == 'y':
        print('ok BAI')
        exit()
    else:
        print(f'idk what you mean by "{question}" try again')
        quitter()
def ui():
    print('----------menu----------')
    prompt = input('>To Gift roses press (G)\n>To open directory mode press (D)\n>To exit the press (E): \n------------------------\nwhat do you want to do?: ').lower()
    if prompt == 'g':
        print('------------------------\nPress M to go back to menu \n Program loading...')
        time.sleep(2)
        gifter()
    elif prompt == 'd':
        lister()
    elif prompt == 'e':
        quitter()
    else:
        print('====\nNot a letter from the list try again\n====')
        ui()
ui()
