import time
import pyautogui
time.sleep(5)
u = open("hello.md",'r')
for word in u:
    pyautogui.typewrite(word)
    pyautogui.press("enter")