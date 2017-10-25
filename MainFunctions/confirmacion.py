import pyautogui as p
import time as t

def confirm():
	test = p.confirm(text='Continue?', title='', buttons=['Yes', 'No'])
	if test == 'No':
		exit()

	t.sleep(2)
