info = {
    'name': 'Ryujin Situp',
    'version': 'v1.0.1'
}

import pygetwindow as gw
import pyautogui
import time
import keyboard
import debug

window = gw.getWindowsWithTitle("Roblox")
try:
    window = window[0]
    window.activate()
except:
    for i in range(3):
        print(f"\rRoblox is not detected! Closing in {3-i} seconds...", end='')
        time.sleep(1)
    exit()

print(f'{info["name"]} {info["version"]}')

letters = "ACEQWXZ"

window.activate()
while not keyboard.is_pressed('delete'):
    left, top = window.left, window.top
    width, height = window.width, window.height
    pyautogui.click(int(left+(width/2)), int(top+(height/2)))
    for i in letters:
        key = f'{debug.getPath()}\\ryujin_situp\\{i}.png'
        try:
            location = pyautogui.locateOnScreen(key, confidence=.8)
            if location is not None:
                keyboard.press(i)
                time.sleep(.1)
                keyboard.release(i)
                print(f'Pressed {i}')
                break
            else:
                print("Err")
        except: pass
    time.sleep(.5)
