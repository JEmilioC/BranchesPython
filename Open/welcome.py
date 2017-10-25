#Test 1 Automatizacion SBClient
import pyautogui as p
import time as t
import sys
sys.path.append('./MainFunctions')
from confirmacion import confirm as confirm

def welcomegd():
    p.alert(text='This script must begin on Branch/Field ManagersGroup Display, click Ok and open the window. (The Script will give you ten seconds to open it)', title='WARNING', button='Aceptar')
    confirm()
    t.sleep(7)
    return 'GD'

# welcomegd()
