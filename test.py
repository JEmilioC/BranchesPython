#Test 1 Automatizacion SBClient
import pyautogui as p
import time as t

def cc():
    con=0
    flag=False
    while flag==False:
        countries = ['IQ','LB', 'OM','YE','TN', 'AO','GH','LS','SZ']
        cd=p.prompt(text='Insert the country code, either, dont write anything ', title='COUNTRY CODE' , default='')
        cd=cd.upper()
        for cc in countries:
            if cd==cc:
                flag=True
                #print (cc)
                return cd
                break
            elif con!='':
                continue
            elif con==1:
                flag=True
                p.alert('You dont have a CD, please contact to the one who can help you')
                exit()
            elif cd=='':
                con=1
                break
            
            
    

cd= cc()
print (cd)
    
