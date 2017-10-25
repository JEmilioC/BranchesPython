def create_bots():

    countries = ['IQ','LB', 'OM','YE','TN', 'AO','GH','LS','SZ']

    for cc in countries:
        time.sleep(5)
        p.typewrite("MELECI" + cc,interval=0.1)
        p.press('tab',interval=1.5)
        test = p.confirm(text='Continue?', title='', buttons=['Yes', 'No'])
        if test == 'No':
            exit()
        p.typewrite("RCMS",interval=0.1)
        p.press('tab',interval=1.5)
        p.typewrite(cc,interval=0.1)
        p.moveTo(647,546)
        p.click()
        p.typewrite("zz",interval=0.1)
        p.press('tab',interval=1.5)
        p.typewrite("mvw",interval=0.1)
        p.press('tab',interval=1.5)
        p.moveTo(654,311)
        p.click()
        time.sleep(2)
        p.typewrite(cc+"MELE",interval=0.1)
        p.press('tab',interval=1.5)
        test = p.confirm(text='Continue?', title='', buttons=['Yes', 'No'])
        if test == 'No':
            exit()
        p.typewrite("CI",interval=0.1)
        p.press('tab',interval=1.5)
        test = p.confirm(text='Continue?', title='', buttons=['Yes', 'No'])
        if test == 'No':
            exit()
        p.press('f2')

create_bots() 
