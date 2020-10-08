import pyautogui
#import lxml

# To pyautogui equivalent for terminal = cliclick
# remember to use 'pipenv run' or 'pipenv shell' when executing in terminal

# 1st open Blackboard (full screen) to login page and set terminal on screen to run program
# will also need to allow the application to control your computer

#pyautogui.click(720, 425)  # clicks the sign-in button

# pyautogui.click() # set coordinates to select the appropriate log-in info from cloud keychain

# BUTTONS. pyautogui allows you to locate screenshots and their current position on screen.  I've loaded mine in ./button_locations
signin_button = './button_locations/signin_buttonLoc.png'
famiPass_button = './button_locations/keychainpass_buttonLoc.png'
signin2_button = './button_locations/signin2_buttonLoc.png'
home_button = './button_locations/home_buttonLoc.png'
content_button = './button_locations/content_buttonLoc.png'
cdan_button = './button_locations/cdan_buttonLoc.png'
compsci_button = './button_locations/compsci_buttonLoc.png'
compsci_assignments_button = './button_locations/compsci_assignments_buttonLoc.png'
crimpro_button = './button_locations/crimpro_buttonLoc.png'
firstam_button = './button_locations/firstam_buttonLoc.png'
cdan_content_button = './button_locations/module_cswks_buttonLoc.png'
tax_button = './button_locations/tax_buttonLoc.png'


schedule_fami = {
    'cdan': [cdan_button, cdan_content_button], 
    'compsci': [compsci_button, content_button, compsci_assignments_button], 
    'crimpro': [crimpro_button, content_button], 
    'firstam': [firstam_button, content_button], 
    'tax': [tax_button, content_button]
}

# Global Functions

def click(button):
    pyautogui.click(button)

def scroll_down():
    pyautogui.press('space')

def go_to_blackboard(password_button):
    pyautogui.hotkey('command', 'space')
    pyautogui.write('safari', interval=0.15)
    pyautogui.press('enter') # open safari
    pyautogui.hotkey('command', 'n') # new window
    pyautogui.hotkey('ctrl', 'command', 'f') # make full screen
    pyautogui.write('https://blackboard.usc.edu', interval=0.15)
    pyautogui.press('enter')
    if pyautogui.locateOnScreen(signin_button):
        click(signin_button)
        click(password_button)
        pyautogui.press('enter')
        scroll_down()
    else:
        scroll_down()


def return_to_home():
    click(home_button) # clicks the 'Home' button
    scroll_down() # scrolls to bottom of 'My Courses'

#def download_content(course):
    #go_to_course(course)
    #go_to_content_page(course)

### MAYBE USE CLASSES?  We could ask for the user at the beginning of the program and have it execute accordingly...
class User:
    def __init__(self, schedule):
        self.courses = schedule
        self.course_downloads = {course:[] for (course,buttons) in self.courses.items()} #an empty dictionary to store values of downloaded items maybe 🤷🏾‍♂️
    
    def go_to_course(self, course):
        if course in self.courses:
            buttons = self.courses.get(course)
            click(buttons[0])

    def go_to_content_page(self, course):
        if course in self.courses:
            buttons = self.courses.get(course)
            click(buttons[1])
    
    def go_to_aux_content_page(self, course):  # this is basically just for the assignments page in compsci
        if course in self.courses:
            buttons = self.courses.get(course)
            if buttons[2]:
                click(buttons[2])        

fami = User(schedule_fami)
#tyler = User(schedule_tyler)



#### MAYBE IF SCREENSHOT LOOKS DIFFERENT THAN BEFORE, CLICK THE DIFFERENCE??
#### MAYBE USE THE FILE/FOLDER IMAGE AS A RELATIONAL CLICK POINT [i.e., wherever you see this on the screen click x pixels to the right of it...]
#### NEED A WAY TO STORE THE THINGS WE'VE ALREADY DOWNLOADED, SO WE DON'T HAVE TO REDOWNLOAD THEM AND SORT... could maybe use urls? or screenshots... not sure...


#### TAXATION
# click(tax_button)
# click(content_button)
# scroll_down()
# pyautogui.click(340,748) # clicks most recent upload... Alternatively, we may be able to use the screenshot function to click next to the file/folder image and download stuff that way...
# scroll_down() # scrolls to bottom of content page (most recent stuff is at the bottom)

go_to_blackboard(famiPass_button)

#TAXATION(CLASSES)
#click(tax_button)
#click(content_button)
#pyautogui.screenshot('tax_content_scrnsht.png')