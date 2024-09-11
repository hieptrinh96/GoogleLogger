import pyautogui
import time


len = 1680 / 2
height = 1050 / 2
button_location = pyautogui.locateOnScreen('./pictures/testscreenshot.png')
time.sleep(1)
pyautogui.click(button_location)
pyautogui.position()
# print(pyautogui.position())
# pyautogui.moveTo(-1712, 361)
# pyautogui.click()
# pyautogui.click()
# pyautogui.hotkey('command', 'r')
# time.sleep(2)
# pyautogui.hotkey('command', 'ctrl', 'f')
