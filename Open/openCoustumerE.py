#Test 1 Automatizacion SBClient
import pyautogui as p
import time as t
import sys
sys.path.append('./MainFunctions')
from confirmacion import confirm as confirm

def openCoustumerE():
    p.alert(text='This script must begin on Home Screen of SB Client, click Ok and open the window. (The Script will give you ten seconds to open it)', title='WARNING', button='Next')
    confirm()
    t.sleep(5)
    p.hotkey('win','up')
    t.sleep(1)
    p.press('esc')
    t.sleep(1)
    p.hotkey('win','up')
    t.sleep(1)
    p.hotkey('win','up')
    t.sleep(0.5)
    p.press('esc')
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
    p.press('down')
    p.press('down')
    t.sleep(0.3)
    p.press('enter')
    t.sleep(2)
