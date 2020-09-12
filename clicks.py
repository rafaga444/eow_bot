import win32gui
import win32api
import win32con
import time
from ctypes import *
import win32com.client
import win32process
from pygetwindow import Window

hWnd = win32gui.FindWindow(None, "Shadow Worlds")
coord = [153, 246]


def click2(x, y):
    hWnd = win32gui.FindWindow(None, "Shadow Worlds")
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hWnd, win32con.WM_NCLBUTTONDOWN, lParam);
    win32gui.PostMessage(hWnd, win32con.WM_NCLBUTTONUP, lParam);


def Click1(x, y):
    hWnd = win32gui.FindWindow(None, "Shadow Worlds")
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam);
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam);


def leftClick(x, y):
    #hWnd = win32gui.FindWindow(None, "Shadow Worlds")
    hWnd = win32gui.Fin(None, "Shadow Worlds")
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE, 0, lParam)
    win32api.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.PostMessage(hWnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)


def click2(x, y):
    hwndWindowTarget = win32gui.FindWindow(None, "Shadow Worlds")
    lParam = win32api.MAKELONG(x, y)
    print(hwndWindowTarget)
    win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONDOWN, lParam)
    win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONUP, lParam)


def clicknormalnyi(x: int, y: int, button: str = "left") -> None:
    """Click at pixel xy."""
    hwndWindowTarget = win32gui.FindWindow(None, "Shadow Worlds")
    lParam = win32api.MAKELONG(x, y)
    # MOUSEMOVE event is required for game to register clicks correctly
    win32gui.PostMessage(hwndWindowTarget, win32con.WM_MOUSEMOVE, 0, lParam)
    while (win32api.GetKeyState(win32con.VK_CONTROL) < 0 or
           win32api.GetKeyState(win32con.VK_SHIFT) < 0 or
           win32api.GetKeyState(win32con.VK_MENU) < 0):
        time.sleep(0.005)
    if button == "left":
        win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONDOWN,
                             win32con.MK_LBUTTON, lParam)
        win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONUP,
                             win32con.MK_LBUTTON, lParam)
    else:
        win32gui.PostMessage(hwndWindowTarget, win32con.WM_RBUTTONDOWN,
                             win32con.MK_RBUTTON, lParam)
        win32gui.PostMessage(hwndWindowTarget, win32con.WM_RBUTTONUP,
                             win32con.MK_RBUTTON, lParam)
    # Sleep lower than 0.1 might cause issues when clicking in succession


def leftclick(x, y, delay=1):
    #lbuttondown 0x0201
    # lbutton up 0x0202
    # hwnd = win32gui.FindWindow(None, "Epoch of Worlds")
    # print(hwnd)
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONDOWN, 1, lParam)
    win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONUP, 1, lParam)
    time.sleep(delay)


def double_left(x , y):
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hwndWindowTarget, win32con.WM_LBUTTONDBLCLK, 1, lParam)


def escape():
    hwndWindowTarget = win32gui.FindWindow("TForm1", "SW")
    #lParam = win32api.MAKELONG(x, y)

    win32gui.PostMessage(hwndWindowTarget, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 1)


