# App to sync all files/docs/images from a whatsapp group to googledrive
"""
Solution overview:
- Download all docs/media/links from whatsapp group to local dir.
- Upload all contents of dir to google drive if not already uploaded.

- How to automatically download all items from a whatsapp group?
    1) Use official whatsapp API? (only business API exists)
    2) Interact with whatsapp website:
        >> Use a hacky way to control mouse cursor to open chrome -> type in whatsapp site -> open group -> click
        on the ... -> select all files to download based on pixel location .... etc (pyautogui)
        >> Use a web browser simulator like selenium and request the web page and scan the html/source for the 
        group's element and then do the same as the hacky pyautogui thing....
    3) Interact with whatsapp local messenger on windows.
"""
import pyautogui as pa
import time
#whatsapp icon : X:340 Y:1055
#whatsapp typing area X:100, Y:110
#whatsapp select group X:150, Y:230
#whatsapp go to group profile X:710, Y:50
#whatsapp go to group media X:1500, Y:530
pa.click(340, 1055)
time.sleep(0.5)
pa.click(100, 110)
pa.typewrite("python")
time.sleep(1)
pa.click(150, 230)
time.sleep(1)
pa.click(710, 50)
time.sleep(1.5)
pa.click(1500, 530)
time.sleep(1.5)
pa.click(1460, 230)  #lateest pic
#time.sleep(1.5)
total = pa.prompt(text='Number of Pics', title='Total Pictures' , default='0')
for pic in range(int(total)):
    pa.click(1830, 55) #download
    time.sleep(0.5)
    pa.press('enter')
    time.sleep(0.5)
    pa.press('left')

# can hold and drag middle mouse button to scroll.

