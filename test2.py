#Test 1 Automatizacion SBClient
import pyautogui as p
import time as t
import pyperclip as py



p.alert(text='This script must begin on Home Screen of SB Client, click Ok and open the window. (The Script will give you ten seconds to open it)', title='WARNING', button='Aceptar')
t.sleep(5)
p.hotkey('ctrl','c')
#pyperclip otorga lo que se encuentra en el clipboard
a=py.paste()
print(a)
