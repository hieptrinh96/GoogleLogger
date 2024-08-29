import pyautogui
import time


len = 1680 / 2
height = 1050 / 2
pyautogui.position()
print(pyautogui.position())
pyautogui.moveTo(-1712, 361)
pyautogui.click()
pyautogui.click()
pyautogui.hotkey('command', 'r')
time.sleep(2)
pyautogui.hotkey('command', 'ctrl', 'f')