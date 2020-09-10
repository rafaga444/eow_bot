
import pyautogui
import keyboard
import win32api, win32con


def click(x, y):

    point = (x, y)

    win32api.SetCursorPos(point)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)




def click_on_pic(picture, confidence=0.6):
    try:
        if pyautogui.locateOnScreen(picture, confidence=confidence) is not None:
            pic = pyautogui.locateOnScreen(picture, confidence=confidence)
            x, y = pic.left, pic.top
            center_x = int(x + pic.width / 2)
            center_y = int(y + pic.height / 2)
            print(f'clicking on {picture}')
            click(center_x, center_y)
        else:
            print(f'cannot find the picture: {picture}')
    except AttributeError:
        print("none")


while not keyboard.is_pressed('q'):
    click_on_pic('udiwn.png')
