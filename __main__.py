import pyautogui as p

from __init__ import action as act1
from __init2__ import action as act2

message = p.confirm(text='Select ONE', title='Excecute', buttons=['Excecute from Home', 'Excecute from already open window'])

if message=='Excecute from Home':
    act2()
elif message=='Excecute from already open window':
    act1()
