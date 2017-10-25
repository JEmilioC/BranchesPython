import pyautogui as p
import time as t

from Open.openGroupDisplay import openGroupDisplay as openGD
from Open.openCoustumerE import openCoustumerE as openCE

def open():
	message = p.confirm(text='Select ONE', title='Open Function', buttons=['Branch/Field ManagersGroup Display', 'Coustumers Engineers Update'])

	if message=='Branch/Field ManagersGroup Display':
		openGD();return 'GD'

	elif message== 'Coustumers Engineers Update':
		openCE();return 'CE'
	else:
		exit()
