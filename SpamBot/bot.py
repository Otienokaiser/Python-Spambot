import time
import pyautogui


def sendSpam():
    time.sleep(5)

    text = open("script.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")


sendSpam()