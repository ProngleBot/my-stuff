import gspread,pprint
from oauth2client.service_account import ServiceAccountCredentials

#important stuff
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sheet = client.open('Art Contest').sheet1
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
    name = input('Enter Name: ')
    cid  = input('Enter Contestant ID: ')
    sub  = input('Paste Submission: ') 
    row.append(name)
    row.append(cid)
    row.append(sub)
    sheet.insert_row(row,2)
    cont = input('do you wish to add another submission?[y/n]').lower()
    if cont == 'y':
        print('alright')
        submit()
    elif cont == 'n':
        contmenu = input('alright do you wish to go back to menu?[y/n]')
        if contmenu == 'y':
            print('oki')
            menu()
        else:
            print('Qutting NASU Now!')

#drivers
def menu():
    print('                  ' + Format.underline+'Nightjar Art Submission Uploader(NASU)\n' +Format.enderline + Format.underline + '\nTop class menu' + Format.enderline) 
    print('\nTo Upload an Art Submission, type:"Sub"\n\nTo see a list of current submissions, type "List Sub"\n\nIf you would like to know more about NASU type "About",\n\nTo exit the program type "exit"')
    print('=======================================================================')
    response = input('Type here: ').lower()
    print('=======================================================================')
    if response == 'sub':
        submit()      
    elif response =='list sub':
        listsub()
        print('==========================================================')
        question = input('Type "Menu" to go back to Menu').lower()
        if question == 'menu':
            menu()
    elif response == 'about':
        print('\nNASU(Nightjar Art Submission Uploader) is a python script that uploads and updates a spreadsheet document.')
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

    