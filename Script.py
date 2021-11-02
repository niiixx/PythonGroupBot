import pyautogui as pa
import time
from pynput import keyboard


def creadorGrupo(mylist, nombreDeGrupo, mensajeBienvenida):
    time.sleep(3)
    pa.moveTo(x=689, y=133)
    pa.click()
    pa.moveTo(x=660, y=190)
    pa.click()

    for name in mylist:
        pa.typewrite(name)
        pa.press('enter')

    pa.moveTo(x=506,y=1002)
    pa.click()

    pa.typewrite(nombreDeGrupo)
    pa.press('enter')