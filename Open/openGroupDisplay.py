#Test 1 Automatizacion SBClient
import pyautogui as p
import time as t
import sys
sys.path.append('./MainFunctions')
from confirmacion import confirm as confirm

def openGroupDisplay():
    p.alert(text='This script must begin on Home Screen, click Ok and open the window. (The Script will give you ten seconds to open it)', title='WARNING', button='Aceptar')
    confirm()
    t.sleep(4)
    p.hotkey('win','up')
    t.sleep(1)
    p.press('esc')
    t.sleep(1)
    p.hotkey('win','up')
    t.sleep(1)
    p.hotkey('win','up')
    t.sleep(0.5)
    p.press('esc')
    p.moveTo(1300,500)
    p.press('right')
    p.press('right')
    p.press('right')
    t.sleep(0.5)
    p.press('down')
    p.press('down')
    p.press('down')
    p.press('down')
    t.sleep(0.3)
    p.press('enter')
    # p.press('down')
    t.sleep(0.3)
    p.press('enter')
    t.sleep(2)
