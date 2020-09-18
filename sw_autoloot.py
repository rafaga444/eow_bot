import pymem
import keyboard
import win32api, win32con
import time
from clicks import double_left, escape

pm = pymem.Pymem("MUDClient.exe")



drop_field = {0: ((199, 240), 0x58398C),
              1: ((235, 243), 0x583990),
              2: ((272, 243), 0x583994),
              3: ((307, 241), 0x583998),
              4: ((342, 241), 0x58399C),
              5: ((375, 241), 0x5839A0),
              6: ((199, 279), 0x5839A4),
              7: ((236, 276), 0x5839A8),
              8: ((270, 276), 0x5839AC),
              9: ((303, 276), 0x5839B0),
              10: ((342, 276), 0x5839B4),
              11: ((378, 277), 0x5839B8),
              12: ((199, 312), 0x5839BC),
              13: ((235, 311), 0x5839C0),
              14: ((271, 310), 0x5839C4),
              15: ((305, 311), 0x5839C8),
              16: ((340, 313), 0x5839CC),
              17: ((377, 312), 0x5839D0),
              18: ((198, 346), 0x5839D4),
              19: ((237, 348), 0x5839D8),
              20: ((273, 346), 0x5839DC),
              21: ((304, 346), 0x5839E0),
              22: ((339, 348), 0x5839E4),
              23: ((378, 347), 0x5839E8),
              24: ((199, 384), 0x5839EC),
              25: ((237, 385), 0x5839F0),
              26: ((271, 385), 0x5839F4),
              27: ((304, 384), 0x5839F8),
              28: ((340, 383), 0x5839FC),
              29: ((378, 383), 0x583A00),
              }

state_right = win32api.GetKeyState(win32con.VK_RBUTTON)  # Left button down = 0 or 1. Button up = -127 or -128
print(state_right)
while True or not keyboard.is_pressed('q'):
    a = win32api.GetKeyState(win32con.VK_RBUTTON)
    if a != state_right:  # Button state changed
        state_right = a

        if a < 0:
            print('Right Button Pressed')
        else:
            print('Right Button Released')

            time.sleep(0.001)
            for elem, coord_address in drop_field.items():
                coord = coord_address[0]
                address = coord_address[1]
                if pm.read_int(coord_address[1]) > 1000:
                    while pm.read_int(coord_address[1]) != 0:
                        if keyboard.is_pressed('q'):
                            break
                        else:
                            print(f'picking up {elem} = {pm.read_int(coord_address[1])} on coord {coord}')
                            double_left(*coord)
                            time.sleep(0.06)

            escape()
