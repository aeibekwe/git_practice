import pyautogui

# To pyautogui equivalent for terminal = cliclick
# remember to use 'pipenv run' or 'pipenv shell' when executing in terminal

# 1st open Blackboard to login page and set terminal on screen to run program
# will also need to allow the application to control your computer

pyautogui.click(720, 425)  # clicks the sign-in button

# pyautogui.click() # set coordinates to select the appropriate log-in info from safari

# ONCE LOGGED IN
pyautogui.scroll(-10) # scrolls to center 'My Courses'



