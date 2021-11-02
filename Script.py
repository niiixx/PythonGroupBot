import pyautogui as pa
import time
from pynput import keyboard
import csv
        
def creadorGrupo(nombreDeGrupo, mensajeBienvenida, nombre):
    time.sleep(3)
    pa.moveTo(x=689, y=133)
    pa.click()
    pa.moveTo(x=660, y=190)
    pa.click()

    with open(nombre) as File:  
        entrada = csv.reader(File)
        for linea in entrada:
            nombre = ''.join(linea)
            pa.typewrite(nombre)
            pa.press('enter')

    pa.moveTo(x=506,y=1002)
    pa.click()

    pa.typewrite(nombreDeGrupo)
    pa.press('enter')

    time.sleep(5)
    pa.typewrite(mensajeBienvenida)
    pa.press('enter')

    
creadorGrupo("Prueba","Mensaje de prueba","prueba.csv")
