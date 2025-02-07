info = {
    'name': 'Ryujin Situp',
    'version': 'v1.0.2'
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

print(f'{info["name"]} {info["version"]}\n')

letters = "ACEQWXZ"

eat_interval = 500

window.activate()
time.sleep(1)
keyboard.press_and_release('1')
while not keyboard.is_pressed('delete'):
    eat_interval -= 1
    left, top = window.left, window.top
    width, height = window.width, window.height
    pyautogui.click(int(left+(width/2)), int(top+(height/2)))
    for i in letters:
        key = f'{debug.getPath()}\\ryujin_situp\\{i}.png'
        try:
            location = pyautogui.locateOnScreen(key, confidence=.8)
            if location is not None:
                keyboard.press_and_release(i)
                print(f'Pressed {i}')
                break
            else:
                print("Err")
        except: pass
    if eat_interval <= 0:
        # do eating here
        keyboard.press_and_release('2')
        time.sleep(.5)
        pyautogui.click(int(left+(width/2)), int(top+(height/2)))
        time.sleep(.5)
        keyboard.press_and_release('1')
        eat_interval = 500
    time.sleep(.5)
