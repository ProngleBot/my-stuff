import requests,random,time,pyautogui
endpoints = ['femdom', 'tickle', 'classic', 'ngif', 'erofeet', 'meow', 'erok', 'poke', 'les', 'v3', 'hololewd', 'nekoapi_v3.1', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'eroyuri', 'kiss', '8ball', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lizard', 'slap', 'lewd', 'cum', 'cuddle', 'spank', 'smallboobs', 'goose', 'Random_hentai_gif', 'avatar', 'fox_girl', 'nsfw_avatar', 'hug', 'gecg', 'boobs', 'pat', 'feet', 'smug', 'kemonomimi', 'solog', 'holo', 'wallpaper', 'bj', 'woof', 'yuri', 'trap', 'anal', 'baka', 'blowjob', 'holoero', 'feed', 'neko', 'gasm', 'hentai', 'futanari', 'ero', 'solo', 'waifu', 'pwankg', 'eron', 'erokemo']
while True:
    x = random.choice(endpoints)
    z = random.randint(1,8)
    html = open('test.html','w+')
    html.write(f'<body bgcolor="pink">\n<h1 align="center">{x} ({z}) pictures/gifs! </h1>\n')
    for b in range(0,z):
        r = requests.get(f'https://nekos.life/api/v2/img/{x}')
        r = r.json()
        r = r['url']
        b = b+1
        html.write(f'<p align="center">\n  <img src = "{r}"/><br><h1 align = "center">{b}</h1">\n</p>')
    print('done')
    html.close()
    pyautogui.press('f5')
    b *= 4
    b = b/2
    print(b)
    time.sleep(b)