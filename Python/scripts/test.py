import time,pyautogui
time.sleep(3)
for x in range(5,75,5):
    pyautogui.write(f'.xpcr {x} 1000',interval='0.04')
    pyautogui.press('enter')


    
    