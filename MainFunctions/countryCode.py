#Country Code
import pyautogui as p
import time as t
def cc():
    con=0
    flag=False
    cont=False
    flagTry=False

    while flag==False:
        countries = ['IQ','LB', 'OM','YE','TN', 'AO','GH','LS','SZ'
        ,'IT','NA','AZ','BZ','BY','AS','AX','AF','BF','BW','BB','MO'
        ,'MY','OM','PA','TO','TT','SE','VA']
        if flagTry==True:
            cd=p.prompt(text='Not found, insert a valid country code, either, dont write anything ', title='COUNTRY CODE' , default='')
            # print('es:'+cd)
        else:
            cd=p.prompt(text='Insert the country code, either, dont write anything ', title='COUNTRY CODE' , default='')


        # Condiciones para revisar que si no ingresó nada no pueda continuar
        if cd!='':
        	cd=cd.upper()
        if cd=='' and cont==False:
        	con=1
        	cont=True
        elif con==1 and cd=='':
           	flag=True
           	p.alert('You dont have a Country Code, please contact the one who can help you')
           	exit()

        # Una vez ingresado el texto busca el country code en el arreglo
        for cc in countries:
            if cd==cc:
                flag=True
                #print (cc)
                return cd.upper()
                break
            if flagTry==True and cc==countries[len(countries)-1]:
                p.alert('You dont have a Country Code, please contact the one who can help you')
               	exit()
            elif cc==countries[len(countries)-1]:
                flagTry=True

        #Buscar que detecte 'diferente de countries' en texto
        # for cc in countries
        	# if
