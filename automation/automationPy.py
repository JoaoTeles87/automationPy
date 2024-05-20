import pyautogui
import time
import random


# Gerar e clicar em uma posição aleatória dentro dos jogo da velha
xMin, xMax = 437, 582  # Limites x (mínimo e máximo)
yMin, yMax = 489, 647  # Limites y (mínimo e máximo)

random_x = random.randint(xMin, xMax)
random_y = random.randint(yMin, yMax)

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
pyautogui.click(random_x, random_y)

random_x = random.randint(xMin, xMax)
random_y = random.randint(yMin, yMax)
time.sleep(1)
pyautogui.click(random_x, random_y)

random_x = random.randint(xMin, xMax)
random_y = random.randint(yMin, yMax)
time.sleep(1)
pyautogui.click(random_x, random_y)

random_x = random.randint(xMin, xMax)
random_y = random.randint(yMin, yMax)
time.sleep(1)
pyautogui.click(random_x, random_y)

random_x = random.randint(xMin, xMax)
random_y = random.randint(yMin, yMax)
time.sleep(1)
pyautogui.click(random_x, random_y)

random_x = random.randint(xMin, xMax)
random_y = random.randint(yMin, yMax)
time.sleep(1)
pyautogui.click(random_x, random_y)

random_x = random.randint(xMin, xMax)
random_y = random.randint(yMin, yMax)

time.sleep(1)
pyautogui.click(random_x, random_y)



