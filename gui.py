import time
import sys
import pyautogui

pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

run = pyautogui.locateOnScreen('run.png')
print(run)
pyautogui.moveTo(run)
pyautogui.click()
express = None
while express is None:
    time.sleep(100)
    express = pyautogui.locateOnScreen('express.png')
print("launch express")
pyautogui.moveTo(express)
pyautogui.click()
pyautogui.click()
oklimit = None
while oklimit is None:
    time.sleep(100)
    oklimit = pyautogui.locateOnScreen('oklimit.png')
pyautogui.moveTo(oklimit)
pyautogui.click()
closesim = pyautogui.locateOnScreen('closesim.png')
pyautogui.moveTo(closesim)
pyautogui.click()