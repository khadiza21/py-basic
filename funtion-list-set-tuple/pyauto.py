# https://pypi.org/
# pip --version
# python --version 
# pip install PyAutoGUI
import pyautogui
import time
pyautogui.alert("This is an alert box.")
pyautogui.write('Hello world! ', interval=0.25)
time.sleep(6)
for i in range(1,5):
    time.sleep(3)
    pyautogui.write('I love Python!', interval=0.25)
    pyautogui.press('enter')