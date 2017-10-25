
import pyautogui as p
import time as t
import sys as sys
sys.path.append('./MainFunctions')
from confirmacion import confirm as confirm


teamlevelFlag=False
companyid='IBM'


def actions1(a,cc):
	if a=='GD':
		cp=cc+'LEN'
		cd= (cc+'LEN')
		p.typewrite(cd, interval=0.2)
		t.sleep(1)
		p.press('tab')
		t.sleep(2)
		confirm()
		p.typewrite(cc)
		p.press('f2')
		t.sleep(3)
		p.typewrite(companyid)
		p.press('tab')
		p.press('tab')
		p.typewrite(cc+' Lenovo', interval=0.2)
		t.sleep(0.5)
		p.press('tab')
		t.sleep(0.5)
		p.typewrite('4')
		p.press('tab')
		confirm()
		p.press('f2')
		# teamlevelFlag=True


	elif a=='CE':
		pass

def actions2(a,cc):
	if a=='GD':
		cp=cc+'LEN'
		cd= (cc+'LEN')
		p.typewrite(cd, interval=0.2)
		p.press('tab')
		t.sleep(2)
		p.press('tab')
		t.sleep(0.2)
		p.press('tab')
		t.sleep(0.2)
		p.press('tab')
		p.typewrite('5')
		p.press('tab')
		confirm()
		p.press('f2')
		# teamlevelFlag=True

# a=actions('GD','IT')
# print(a)
# actions1('GD','AS')
# actions2('GD','AS')
# print (teamlevelFlag)
