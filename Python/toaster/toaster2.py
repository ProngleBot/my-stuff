import pyautogui,time
time.sleep(5)
print('scripts about to start')

x  = 0
while True:
    if x == 30:
        print('done')
        exit()
    else:
        x = x + 1
        pyautogui.write('fuckoff',interval='0.05')
        pyautogui.press('enter')
        print(x)