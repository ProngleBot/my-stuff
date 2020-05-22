import requests,time,pyautogui
ask = input('Enter tag here: ').lower()
x = -1
def neko():
    f = open("test.html",'w+')
    f.write(f'<body bgcolor = pink>\n <h1 align = "center"><u>{ask}</u></h1><hr>')
    for _ in range(12):
        r = requests.get(f'https://nekos.life/api/v2/img/{ask}')
        r = r.json()
        r = r['url']
        f.write(f'<img heignt ="800", width ="400", src="{r}"/>\n')
    f.write('</body>')
    print('done')
    f.close()
    pyautogui.press('f5')
while True:
    x = x
    x = x+1
    if x <= 1:
        print('reset once')
        neko()
    else:
        print(f'reset {x} times')
        neko()
    time.sleep(30)
neko()