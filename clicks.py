import win32gui
import win32api
import win32con
import time


hWnd = win32gui.FindWindow(None, "Epoch of Worlds")



def leftclick(x, y, delay=0.03, amount=1):
    # lbuttondown 0x0201
    # lbutton up 0x0202
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    lParam = win32api.MAKELONG(x, y)
    for i in range(amount):
        win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONDOWN, 1, lParam)
        win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONUP, 1, lParam)
        time.sleep(delay)

def rightclick(x, y, delay=0.03, amount=1):
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    lParam = win32api.MAKELONG(x, y)
    for i in range(amount):
        win32gui.PostMessage(hwndWindowTarget, win32con.WM_RBUTTONDOWN, 1, lParam)
        win32gui.PostMessage(hwndWindowTarget, win32con.WM_RBUTTONUP, 1, lParam)
        time.sleep(delay)

def double_left(x, y):
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONDBLCLK, 1, lParam)


def escape():
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    # lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hwndWindowTarget, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 1)
    win32gui.PostMessage(hwndWindowTarget, win32con.WM_KEYUP, win32con.VK_ESCAPE, 1)


def shiftclick(x, y, delay=0.3):
    # lbuttondown 0x0201
    # lbutton up 0x0202
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONDOWN, win32con.MK_SHIFT, lParam)
    win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONUP, win32con.MK_SHIFT, lParam)
    time.sleep(delay)

def f8():
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    # lParam = win32api.MAKELONG(x, y)
    win32gui.PostMessage(hwndWindowTarget, win32con.WM_KEYDOWN, win32con.VK_F8, 1)
    win32gui.PostMessage(hwndWindowTarget, win32con.WM_KEYUP, win32con.VK_F8, 1)
    time.sleep(0.5)



