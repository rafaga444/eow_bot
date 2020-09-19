import pymem
import keyboard
import win32api, win32con
import time
from clicks import double_left, escape, rightclick

pm = pymem.Pymem('mudclient.exe')

# cell coordinates, item_id, quantity
drop_field = {0: ((200, 240), 0x555654, 0x55574C),
              1: ((241, 240), 0x5557D4, 0x5558CC),
              2: ((273, 242), 0x555954, 0x555A4C),
              3: ((307, 241), 0x555AD4, 0x555BCC),
              4: ((342, 242), 0x555C54, 0x555D4C),
              5: ((379, 239), 0x555DD4, 0x555ECC),
              6: ((200, 276), 0x555F54, 0x55604C),
              7: ((239, 276), 0x5560D4, 0x5561CC),
              8: ((272, 276), 0x556254, 0x55634C),
              9: ((307, 279), 0x5563D4, 0x5564CC),
              10: ((343, 279), 0x556554, 0x55664C),
              11: ((374, 279), 0x5566D4, 0x5567CC),
              12: ((197, 311), 0x556854, 0x55694C),
              13: ((235, 310), 0x5569D4, 0x556ACC),
              14: ((269, 309), 0x556B54, 0x556C4C),
              15: ((307, 312), 0x556CD4, 0x556DCC),
              16: ((342, 312), 0x556E54, 0x556F4C),
              17: ((380, 312), 0x556FD4, 0x5570CC),
              18: ((199, 344), 0x557154, 0x55724C),
              19: ((237, 344), 0x5572D4, 0x5573CC),
              20: ((267, 345), 0x557454, 0x55754C),
              21: ((307, 347), 0x5575D4, 0x5576CC),
              22: ((340, 348), 0x557754, 0x55784C),
              23: ((376, 346), 0x5578D4, 0x5579CC),
              24: ((198, 383), 0x557A54, 0x557B4C),
              25: ((234, 381), 0x557BD4, 0x557CCC),
              26: ((272, 381), 0x557D54, 0x557E4C),
              27: ((304, 380), 0x557ED4, 0x557FCC),
              28: ((339, 381), 0x558054, 0x55814C),
              29: ((378, 380), 0x5581D4, 0x5582CC),
              }


def loot():
    for elem, coord_address in drop_field.items():
        coord = coord_address[0]
        item_id = pm.read_int(coord_address[1])
        is_gold = pm.read_int(coord_address[2])

        if is_gold > 1:
            if keyboard.is_pressed('q'):
                break
            else:
                print(f'picking up {elem} = {item_id, is_gold} on coord {coord}')
                double_left(*coord)
                double_left(*coord)
                time.sleep(0.01)

    escape()


state_right = win32api.GetKeyState(win32con.VK_RBUTTON)  # Left button down = 0 or 1. Button up = -127 or -128
print(state_right)
# while True or not keyboard.is_pressed('q'):
#     a = win32api.GetKeyState(win32con.VK_RBUTTON)
#     if a != state_right:  # Button state changed
#         state_right = a
#
#         if a < 0:
#             print('Right Button Pressed')
#         else:
#             print('Right Button Released')
#
#             time.sleep(0.001)
#             loot()

# for elem, coord_address in drop_field.items():
#     coord = coord_address[0]
#     item_id = pm.read_int(coord_address[1])
#     is_gold = pm.read_int(coord_address[2])
#     print(item_id, is_gold)

# print(coord_address[0], coord_address[1], coord_address[2])


