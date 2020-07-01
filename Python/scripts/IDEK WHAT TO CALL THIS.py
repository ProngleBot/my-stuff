import pymongo
import pprint as pp
client = pymongo.MongoClient("mongodb+srv://bigpapaasg:shinchan11@cluster0.0hiha.mongodb.net/oasis?retryWrites=true&w=majority")
db = client.oasis
col = db.cheese
def ccheese():
    print('---Add Menu---')
    idno = input('Enter ID Number: ')
    name = input('Enter Name: ')
    cheesepref  = input('Do you like cheese?[Y/N]: ').lower()
    favoritecheese = input('Whats your favorite cheese?: ')
    if cheesepref == 'n':
        db.cheese.insert_one({
            "id": idno,
            "name": name,
            "cheesepref": 'n',
        })
    else:
        db.cheese.insert_one({
            "id": idno,
            "name": name,
            "cheesepref": cheesepref,
            "favoritecheese": favoritecheese
        })
    print('User Added to list')
    asker = input('Would you like to add another user to the list? [y/n]: ').lower()
    if asker == 'y':
        ccheese()
    else:
        print('okay')
        exit()

def rcheese():
    print("---Read Menu---")
    choice = input('If you want to list All users, say users: ')
    users = col.find()
    if choice == "users":
        for user in users:
            pp.pprint(user)
    else:
        user = input('Enter id: ')
        users = col.find_one({'id':f'{user}'})
        print(users['name'],':',users['favoritecheese'])

def ui():
    ask = input('[C]reate user, [S]ee user data').lower()
    if ask == 'c':
        ccheese()
    else:
        rcheese()
ui()