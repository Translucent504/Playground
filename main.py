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
import pyautogui