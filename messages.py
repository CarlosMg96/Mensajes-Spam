import pyautogui as pt
import time 

limit = input("Cantidad de Mensajes ")
message = input("Mensaje: ")
i = 0

time.sleep(5)

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")
    i += 1