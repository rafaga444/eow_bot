import win32gui
import win32api
import win32con
import time
import pyautogui
import keyboard
from clicks import escape

hwnd = win32gui.FindWindow("TForm1", "SW")
hwndscr = win32gui.FindWindow(None, 'Shadow Worlds')

def leftclick(x, y, delay=1):
    #lbuttondown 0x0201
    # lbutton up 0x0202
    # hwnd = win32gui.FindWindow(None, "Epoch of Worlds")
    # print(hwnd)
    global hwnd
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 1, lParam)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 1, lParam)
    time.sleep(delay)

def click_on_pic(picture, confidence=0.6):
    try:
        rect = win32gui.GetWindowRect(hwndscr)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        picclick = pyautogui.locateOnScreen(picture, region=(x, y, w, h), grayscale=True, confidence=0.6)
        if picclick is not None:
            point = pyautogui.center(picclick)
            click_x = point.x - x
            click_y = point.y - y
            print(click_x, click_y)
            leftclick(click_x, click_y, delay=0.02)
        else:
            print(f'cannot find the picture: {picture}')
    except AttributeError:
        print("none")


while True:
    if keyboard.is_pressed('q'):
        while not keyboard.is_pressed('q'):
            click_on_pic('rafaga.png')
            if keyboard.is_pressed('esc'):
                escape()

