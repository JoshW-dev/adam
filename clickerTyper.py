import os
import time
import pyautogui

print("start")

#click 
time.sleep(2)
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.moveTo(400, 400, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()


time.sleep(1)

#type
pyautogui.hotkey('alt', 'tab') # Press the Ctrl-C hotkey combination.
pyautogui.moveTo(200, 200, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.write('Hello world!', interval=0.25)

print("end")
