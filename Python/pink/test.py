import gspread, pprint, json
from oauth2client.service_account import ServiceAccountCredentials

#important stuff
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sheet = client.open('Art Contest').sheet1

print(sheet.row_count)