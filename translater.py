from pygoogletranslation import Translator #I'm using pygoogletranslation instead of googletrans cuz googletrans sometimes doesn't translate word into Turkish
#from googletrans import Translator
from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
from plyer.utils import platform
from plyer import notification
import tkinter as tk
import win32clipboard
import pyperclip

last_data = None

def getClipboard():
    r = tk.Tk()
    r.withdraw()
    return r.clipboard_get()


while True:
    try:
        text = getClipboard()#pyperclip.paste()
        
        #win32clipboard.OpenClipboard()
        #text = win32clipboard.GetClipboardData()
        temiz_txt = list([val for val in text if val.isalpha() or val.isnumeric() or val == " "])
        text = "".join(temiz_txt)
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        text = text.replace('\t', ' ')
        while text.find('  ') != -1:
            text = text.replace('  ', ' ')
        
        win32clipboard.CloseClipboard()
    except:
        print("Hata oluştu")
        pass
    translator = Translator()
    if(text != last_data):
        if(len(text) > 0 and text != " "):
            translate_text = translator.translate(text=text,src='en',dest='tr')  
            print(text,translate_text)
            notification.notify(
            title=text[:64],
            message= translate_text.text[:64],
            app_name= "-"
            )
    last_data = text
