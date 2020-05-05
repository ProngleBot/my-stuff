username  = ['limey','borj','asg']
names = ['shreehari','imran','ruby']
likes = ['Guitar solos.','cats.','Beans.']
pronouns = ['he', 'she']
print(', '.join(username))
prompt = input("Above is the list of all the registered users who's info would you like to see:\n")
if prompt =="":
    print ('input error')
elif prompt == username[0]:
    print(prompt,'is',names[2],'and',pronouns[1],'loves',likes[2])
elif prompt == username[1]:
    print(prompt, 'is', names[1],'and', pronouns[0],'loves',likes[1])
else:
    print(prompt, 'is',names[0],'and',pronouns[0], 'loves',likes[0])