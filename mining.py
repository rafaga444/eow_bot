import pymem
import keyboard
import win32api, win32con
import time
from clicks import double_left, escape, leftclick

pm = pymem.Pymem('mudclient.exe')
current_first_bag_slot = pm.read_int(0x564580)
# pickaxe ID = 134
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
bag = {
    0: 0x564604,
    1: 0x564784,
    2: 0x564904,
    3: 0x564A84,
    4: 0x564C04,
    5: 0x564D84,
    6: 0x564F04,
    7: 0x565084,
    8: 0x565204,
    9: 0x565384,
    10: 0x565504,
    11: 0x565684,
    12: 0x565804,
    13: 0x565984,
    14: 0x565B04,
    15: 0x565C84,
    16: 0x565E04,
    17: 0x565F84,
    18: 0x566104,
    19: 0x566284,
    20: 0x566404,
    21: 0x566584,
    22: 0x566704,
    23: 0x566884,
    24: 0x566A04,
    25: 0x566B84,
    26: 0x566D04,
    27: 0x566E84,
    28: 0x567004,
    29: 0x567184,
}


def find_pickaxe():
    global current_first_bag_slot
    for cell_num, address in bag.items():
        item_id = pm.read_int(address)
        if item_id == 134:
            pickaxe_slot = cell_num
            if pickaxe_slot < current_first_bag_slot:
                clicks_count = current_first_bag_slot - pickaxe_slot
                leftclick(460, 230,delay=0, amount=clicks_count)
            elif pickaxe_slot > current_first_bag_slot:
                clicks_count = pickaxe_slot - current_first_bag_slot
                leftclick(599, 231,delay=0, amount=clicks_count)
            else:
                print('found')



find_pickaxe()
