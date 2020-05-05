import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
time.sleep(1)
n = 0
def presser():
    global n
    n = n+1
    keyboard = KeyboardController()
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    if n == 1:
        print('Key Pressed 1 time!')
    else:
        print('Key Pressed', n ,'times!')    
    time.sleep(5)
    presser()
def scroller():
    mouse = MouseController()
    mouse.scroll(0,-3)
    time.sleep(1)
    scroller()
def starter():
    x = input(' clicker or scroller ').lower()
    if x == 'clicker':
        presser()
    elif x == 'scroller':
        scroller()
starter()