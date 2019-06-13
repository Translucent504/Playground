import pyautogui as pa
import time

pa.PAUSE = 0.3

def SwitchToWord():
    pa.click(542,15)

def SwitchToAdd():
    pa.click(1200,15)

x = pa.prompt('words')

def copyOver():
    time.sleep(2)
    for words in range(x):

        SwitchToWord()
        pa.press('tab')
        pa.hotkey('ctrl','c')           
        #pa.hotkey('alt','tab')
        SwitchToAdd()
        pa.hotkey('ctrl','v')
        pa.press('tab')
        #now def field is in focus
        SwitchToWord()
        pa.press('tab')
        pa.hotkey('ctrl','c')
        SwitchToAdd()
        pa.hotkey('ctrl','v')
        pa.press('tab')
        #now noun field in focus
        SwitchToWord()
        pa.press('tab')
        pa.hotkey('ctrl','c')       
        SwitchToAdd()
        pa.hotkey('ctrl','v')
        pa.press('tab')
        # verb
        SwitchToWord()
        pa.press('tab')
        pa.hotkey('ctrl','c')
        SwitchToAdd()
        pa.hotkey('ctrl','v')
        pa.press('tab')
        # adjective
        SwitchToWord()
        pa.press('tab')
        pa.hotkey('ctrl','c')
        SwitchToAdd()
        pa.hotkey('ctrl','v')
        pa.press('tab')
        # examples
        SwitchToWord()
        pa.press('tab')
        pa.press('tab')
        pa.hotkey('ctrl','c')
        SwitchToAdd()
        pa.hotkey('ctrl','v')

        #add
        pa.press('tab')
        pa.press('tab')
        pa.press('enter')

copyOver()