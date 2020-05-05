import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

#important stuff
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sheet = client.open('Art Contest').sheet1
rcount = sheet.row_count
#formatted thingies
class Format:
    underline = '\033[4m'
    enderline = '\033[0m'
    bold = '\033[1m'
    unbold = '\033[0;0m'
def listsub():
    print('Just go look here please https://docs.google.com/spreadsheets/d/13EevqL0oth8VCokg4KaIvmwbKm9rKX-u3YN3ivbmRCQ/edit?usp=sharing')
def submit():
    row=[]
    name = input('Enter Name:')
    cid  = input('Enter Contestant ID:')
    sub  = input('Paste Submission(note:dont ctrl+v):') 
    index = 2
    row.append(name)
    row.append(cid)
    row.append(sub)
    row.append(index)
    sheet.insert_row(row,index)
    print('Done! exiting now...')


#drivers
print('                          ' + Format.underline+'NASU\n' +Format.enderline)
print(Format.underline +Format.bold + 'Number of current submissions:'+ Format.unbold + Format.enderline + str(rcount))
print("\nIf you want to submit a submission type 'Sub'\n\nIf you want to see a list of submissions type'List Sub'\n\nIf you want to know more about NASU type 'about'. " )
response = input('\nEnter your request here:').lower()

if response == 'sub':
    submit()
elif response =='list sub':
    listsub()
elif response == 'about':
    print('\nNASU(Nightjar Art Submission Uploader) is a python script that uploads and updates a spreadsheet document.')
