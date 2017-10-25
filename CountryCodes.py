#Test 1 Automatizacion SBClient
import pyautogui as p
import time as t

from MainFunctions.countryCode import cc as cc
from Open.mainOpen import open as Mopen
from Open.welcome import welcomegd as welcomegd
from MainFunctions.confirmacion import confirm as confirm
from MainFunctions.action import actions1 as actions1
from MainFunctions.action import actions2 as actions2


def actionsCC(a):
    ccodes=[]
    countcc=p.prompt(text='How many Country codes? (at least 1)', title='Country codes' , default='')
    countcc=int(countcc)

    if countcc>0:
        count=1
        while countcc>0:
            cCode=p.prompt(text='Country code #'+str(count), title='Country codes' , default='')
            ccodes.append(cCode.upper())
            countcc=countcc-1
            count=count+1

        for cd in ccodes:
            p.alert(text='This is the Country Code number '+str(ccodes.index(cd)+1) +', click ok to continue.', title='Message', button='Ok')
            actions1(a,cd)
            actions2(a,cd)
        # print(code)

    # elif countcc ==1:
    #     actions1(a,cd)
    #     actions2(a,cd)
