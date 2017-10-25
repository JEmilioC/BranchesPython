# Automatizacion desde INICIO
import pyautogui as p
import time as t

from MainFunctions.countryCode import cc as cc
from Open.mainOpen import open as Mopen
from Open.welcome import welcomegd as welcomegd
from MainFunctions.confirmacion import confirm as confirm
from MainFunctions.action import actions1 as actions1
from MainFunctions.action import actions2 as actions2
from CountryCodes import actionsCC as actions


def action():
#Abrir la ventana deseada con mainOpen.py
    a=Mopen()
#Acción dependiendo de la ventana que se abrió action.py
#Envía la opcion elegida al inicio y el countryCode
# actions1(a,cd)
# actions2(a,cd)
    actions(a)
#This isnt a big change
