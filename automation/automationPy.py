import pyautogui
import time


pyautogui.PAUSE = 0.5 #o tempo de execução entre um comando e outro

# abrir o navegador chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=981, y=320)
pyautogui.click(x=967, y=324)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(296, 63)
pyautogui.press("enter")
pyautogui.write("jogo da velha google")
pyautogui.press("enter")  
time.sleep(2)
pyautogui.click(508, 589)
time.sleep(2)
pyautogui.click(437, 647)
time.sleep(2)
pyautogui.click(506, 585)
time.sleep(2)
pyautogui.click(525, 489)

time.sleep(2)
pyautogui.click(496, 571)
time.sleep(2)
pyautogui.click(582, 514)
time.sleep(2)
pyautogui.click(499, 524)

f,g = pyautogui.position()
print(f'A posição do cursor do mouse é: ({f}, {g})')
time.sleep(2)
r, u = pyautogui.position()
print(f'A posição do cursor do mouse é: ({r}, {u})')

