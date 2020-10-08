import pyautogui as gui
import time

#get input
request = input('How can I help? ')

#convert to siri command
gui.hotkey('ctrlleft', 'space')
time.sleep(1)
gui.write(request, interval=0.01)
gui.press('return')
