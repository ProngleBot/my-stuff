import requests, time,random,pyautogui

while True:
    x = ['femdom', 'tickle', 'classic', 'ngif', 'erofeet', 'meow', 'erok', 'poke', 'les', 'v3', 'hololewd', 'nekoapi_v3.1', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'eroyuri', 'kiss', '8ball', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lizard', 'slap', 'lewd', 'cum', 'cuddle', 'spank', 'smallboobs', 'goose', 'Random_hentai_gif', 'avatar', 'fox_girl', 'nsfw_avatar', 'hug', 'gecg', 'boobs', 'pat', 'feet', 'smug', 'kemonomimi', 'solog', 'holo', 'wallpaper', 'bj', 'woof', 'yuri', 'trap', 'anal', 'baka', 'blowjob', 'holoero', 'feed', 'neko', 'gasm', 'hentai', 'futanari', 'ero', 'solo', 'waifu', 'pwankg', 'eron', 'erokemo']
    x = random.choice(x)
    r = requests.get(f'https://nekos.life/api/v2/img/{x}')
    r = r.json()
    r = r['url']
    html = open('test.html','w+')
    html.write(f'<body bgcolor="pink">\n<h1 align = "center">{x}</h1>\n<hr>\n<p align = "center">\n<img width = 50% src ="{r}"/>\n</p>')
    html.close()
    pyautogui.press('f5')
    o = 16
    while True:
        o -= 1 
        time.sleep(1)
        print(o,end='\r')
        pyautogui.scroll(-50)
        if o == 0:
            break