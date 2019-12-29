import pyautogui
import time

'''
League of Legends auto-accept.
Author: Nikolay Ivanov
https://pythondevbg2.wixsite.com/nikolaypy
Requirements: pyautogui, Accept button image.
'''

def acceptGame():
    #While Image Not Found LOOP.
    while True:
        time.sleep(.1)#UPDATE SEARCH EVERY SECOND
        if pyautogui.locateOnScreen('Accept.png'):#IF PICTURE IS ON SCREEN -> CLICK
            pyautogui.click(pyautogui.locateOnScreen('Accept.png'))
            break
        #IF NOT -> Tell me it is not found yet.
        else:
            print('Not found yet...')
while True:
    acceptGame()
