import gspread,pprint
from oauth2client.service_account import ServiceAccountCredentials

#important stuff
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('../client_secret.json',scope)
client = gspread.authorize(creds)
sheet = client.open('friends database').sheet1
pp = pprint
#formatted thingies
class Format:
    underline = '\033[4m'
    enderline = '\033[0m'
    bold = '\033[1m'
    unbold = '\033[0;0m'
def listsub():
    submitters = sheet.get_all_records()
    for x in submitters:
        for k,v in x.items():
            print(k,v)
def submit():
    row=[]
    likes = input('Enter Likes: ')
    user  = input('Enter Username: ')
    pro = input('Enter Pronouns: ')
    row.append(likes)
    row.append(user)
    row.append(pro)
    sheet.insert_row(row,2)
    cont = input('do you wish to add another person?[y/n]').lower()
    if cont == 'y':
        print('alright')
        submit()
    elif cont == 'n':
        contmenu = input('alright do you wish to go back to menu?[y/n]')
        if contmenu == 'y':
            print('oki')
            menu()
        else:
            print('Qutting Friends List Maker Now!')

#userinterface
def menu():
    print('                  ' + Format.underline+'Friends List Updater\n' +Format.enderline + Format.underline + '\nTop class menu' + Format.enderline) 
    print('\nTo Add a friend to the list type:"add"\n\nTo see a list of current friends, type "List friends"\n\nIf you would like to know more about Friends List Maker type "About",\n\nTo exit the program type "exit"')
    print('=======================================================================')
    response = input('Type here: ').lower()
    print('=======================================================================')
    if response == 'add':
        submit()      
    elif response =='list friends':
        listsub()
        print('==========================================================')
        question = input('Type "Menu" to go back to Menu').lower()
        if question == 'menu':
            menu()
    elif response == 'about':
        print('\nFLU(Friends List Updater) is a python script that uploads and updates a spreadsheet document.')
        __ = input('Do you want to go back to the menu?[y/n]')
        if __ == 'y':
            print('okay')
            menu()
        else:
            x = input('uhm.. what do you wanna do then, quit?[y/n]').lower()
            if x == 'y':
                print('okay bye ily')
            else:
                print('... i dont know what you want to do with me now maybe its just better to quit this awkward uhhhh bye.')
    elif response =='exit':
        print('bai ily')
menu()

    