import pymem
import keyboard
import win32api, win32con
import time
from clicks import double_left, escape, leftclick, rightclick

pm = pymem.Pymem('mudclient.exe')

# pickaxe ID = 134
# gold iD    = 109
# cell coordinates, item_id, quantity
drop_window = {0: ((200, 240), 0x555654, 0x55574C),
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
drop_field = {
    (8, 9): ((150, 170), 0x575B60),
    (9, 9): ((170, 170), 0x576B20),
    (10, 9): ((190, 170), 0x577AE0),
    (11, 9): ((210, 170), 0x578AA0),
    (12, 9): ((230, 170), 0x579A60),
    (13, 9): ((250, 170), 0x57AA20),
    (14, 9): ((270, 170), 0x57B9E0),
    (8, 10): ((150, 190), 0x575C20),
    (9, 10): ((170, 190), 0x576BE0),
    (10, 10): ((190, 190), 0x577BA0),
    (11, 10): ((210, 190), 0x578B60),
    (12, 10): ((230, 190), 0x579B20),
    (13, 10): ((250, 190), 0x57AAE0),
    (14, 10): ((270, 190), 0x57BAA0),
    (8, 11): ((150, 210), 0x575CE0),
    (9, 11): ((170, 210), 0x576CA0),
    (10, 11): ((190, 210), 0x577C60),
    # (11, 11): ((210, 210), 0x578C20), #thats me :D
    (12, 11): ((230, 210), 0x579BE0),
    (13, 11): ((250, 210), 0x57ABA0),
    (14, 11): ((270, 210), 0x57BB60),
    (8, 12): ((150, 230), 0x575DA0),
    (9, 12): ((170, 230), 0x576D60),
    (10, 12): ((190, 230), 0x577D20),
    (11, 12): ((210, 230), 0x578CE0),
    (12, 12): ((230, 230), 0x579CA0),
    (13, 12): ((250, 230), 0x57AC60),
    (14, 12): ((270, 230), 0x57BC20),
    (8, 13): ((150, 250), 0x575E60),
    (9, 13): ((170, 250), 0x576E20),
    (10, 13): ((190, 250), 0x577DE0),
    (11, 13): ((210, 250), 0x578DA0),
    (12, 13): ((230, 250), 0x579D60),
    (13, 13): ((250, 250), 0x57AD20),
    (14, 13): ((270, 250), 0x57BCE0),
    (8, 14): ((150, 270), 0x575F20),
    (9, 14): ((170, 270), 0x576EE0),
    (10, 14): ((190, 270), 0x577EA0),
    (11, 14): ((210, 270), 0x578E60),
    (12, 14): ((230, 270), 0x579E20),
    (13, 14): ((250, 270), 0x57ADE0),
    (14, 14): ((270, 270), 0x57BDA0),

}
#   slot item_id   quantity
bag = {
    0: (0x564604, 0x5646FC,),
    1: (0x564784, 0x56487C,),
    2: (0x564904, 0x5649FC,),
    3: (0x564A84, 0x564B7C,),
    4: (0x564C04, 0x564CFC,),
    5: (0x564D84, 0x564E7C,),
    6: (0x564F04, 0x564FFC,),
    7: (0x565084, 0x56517C,),
    8: (0x565204, 0x5652FC,),
    9: (0x565384, 0x56547C,),
    10: (0x565504, 0x5655FC,),
    11: (0x565684, 0x56577C,),
    12: (0x565804, 0x5658FC,),
    13: (0x565984, 0x565A7C,),
    14: (0x565B04, 0x565BFC,),
    15: (0x565C84, 0x565D7C,),
    16: (0x565E04, 0x565EFC,),
    17: (0x565F84, 0x56607C,),
    18: (0x566104, 0x5661FC,),
    19: (0x566284, 0x56637C,),
    20: (0x566404, 0x5664FC,),
    21: (0x566584, 0x56667C,),
    22: (0x566704, 0x5667FC,),
    23: (0x566884, 0x56697C,),
    24: (0x566A04, 0x566AFC,),
    25: (0x566B84, 0x566C7C,),
    26: (0x566D04, 0x566DFC,),
    27: (0x566E84, 0x566F7C,),
    28: (0x567004, 0x5670FC,),
    29: (0x567184, 0x56727C,),
}


def find_slot(slot_number):
    if slot_number < pm.read_int(0x564580):
        clicks_count = pm.read_int(0x564580) - slot_number
        leftclick(460, 230, delay=0, amount=clicks_count)
    elif slot_number > pm.read_int(0x564580):
        clicks_count = slot_number - pm.read_int(0x564580)
        leftclick(599, 231, delay=0, amount=clicks_count)


def find_pickaxe():
    global pickaxe_slot
    for cell_num, address in bag.items():
        item_id = pm.read_int(address[0])
        if item_id == 134:
            pickaxe_slot = cell_num
            find_slot(pickaxe_slot)
    return pickaxe_slot





def free_space():
    space = 0
    for cell_num, address in bag.items():
        item_id = pm.read_int(address[0])
        if item_id == 0:
            space += 1
    return space


def dig():
    slot = find_pickaxe()
    # time.sleep(0.5)
    if slot == 28:
        rightclick(522, 231, delay=0)
        leftclick(157, 151, delay=0)
        time.sleep(9)
    elif slot == 29:
        rightclick(564, 229, delay=0)
        leftclick(157, 151, delay=0)
        time.sleep(9)
    else:
        rightclick(483, 233, delay=0)
        leftclick(157, 151, delay=0)
        time.sleep(9)


def is_not_gold():
    to_drop = []
    for cell_num, address in bag.items():
        item_id = pm.read_int(address[0])
        quantity = pm.read_int(address[1])
        if item_id not in (134, 109, 0):
            if quantity == 10 or free_space() < 2:
                to_drop.append(cell_num)
    return to_drop





def drop(to_drop: list):
    for coord, address in drop_field.values():
        rightclick(*coord, delay=0.05)
        field_free_space = 0
        for elem, coord_address in drop_window.items():
            item_id = pm.read_int(coord_address[1])
            if item_id == 0:
                field_free_space += 1

        if field_free_space >= len(to_drop):

            for item in reversed(to_drop):
                find_slot(item)
                time.sleep(0.04)
                if item == 28:
                    double_left(522, 231)
                elif item == 29:
                    double_left(564, 229)
                else:
                    double_left(483, 233)

                to_drop.pop()

        escape()

def count_gold():


while not keyboard.is_pressed('q') or free_space() == 0:
    current_free = free_space()
    print('current - ', current_free)
    dig()
    print(len(is_not_gold()))
    if len(is_not_gold()) > 0:
        drop(is_not_gold())

