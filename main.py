import win32gui
from pymem import *

import keyboard
from clicks import shiftclick, rightclick
import move as b
import time
import datetime
from monster_map import mob_map
from eow_autoloot import loot

now = datetime.datetime.now()

hwndscr = win32gui.FindWindow(None, 'Epoch of Worlds')
pm = pymem.Pymem("MUDClient.exe")

player_mn = 0x005680FC
player_hp = 0x005680F8
player_hp_percent = pm.read_int(0x578C20) / 10
player_y = 0x01355EB8
player_x = 0x0056E6C8
cur_map = 0x51DF44
cur_exp = 0x56810C
current_first_bag_slot = 0x564580
stats_window_status = 0x0051DE28  # 1 - opened 2 - closed
first_bag_slot = 0x0564604
hota_active = 0x554D70  # 90 = active
zombie_hp_down = 0x578DA0
hp_up = 0x578AA0

print(pm.read_int(player_x), pm.read_int(player_y))


# pm.write_int(stats_window_status, 1)
# mob_map: cell coord, mouse point, cell address


class Move:
    def __init__(self):
        self.x = pm.read_int(player_x)
        self.y = pm.read_int(player_y)

    def goto2(self, x, y):
        while self.x != x or self.y != y:
            previous_coord = []
            self.y = pm.read_int(player_y)
            self.x = pm.read_int(player_x)
            if search_hp():
                attack()
            elif self.x < x:
                if self.y < y:
                    b.go_right_down()
                elif self.y == y:
                    b.go_right()
                elif self.y > y:
                    b.go_right_up()
            elif self.x > x:
                if self.y < y:
                    b.go_left_down()
                    #
                    # previous_coord.append((self.x, self.y))
                    #
                    # print((self.x, self.y), (previous_coord[0], previous_coord[1]))
                    # time.sleep(0.5)
                    # if (self.x, self.y) == (previous_coord[0], previous_coord[1]):
                    #     print('left_down')

                elif self.y > y:
                    b.go_left_up()
                    # coord_old = self.y = pm.read_int(player_y)
                    # if self.y == coord_old:
                    #     b.go_up()

                elif self.y == y:
                    b.go_left()
            elif self.x == x:
                if self.y > y:
                    b.go_up()
                elif self.y < y:
                    b.go_down()



def record():
    x = pm.read_int(player_x)
    y = pm.read_int(player_y)
    coord_list = []
    with open('coordinates.txt', mode='w', encoding='UTF-8') as f:
        f.write(str(x) + ',' + str(y) + '\n')
        while True:
            time.sleep(1.8)
            x1 = pm.read_int(player_x)
            y1 = pm.read_int(player_y)

            if x != x1:
                print('x', x, 'y', y)
                coord_list.append(str(x1) + ',' + str(y1) + '\n')
                print(str(x1) + ',' + str(y1))
                x = x1
                y = y1
            elif y != y1:
                print('x', x, 'y', y)
                coord_list.append(str(x1) + ',' + str(y1) + '\n')
                print(str(x1) + ',' + str(y1))
                x = x1
                y = y1
            if keyboard.is_pressed('q'):
                for coord in coord_list:
                    f.write(str(coord))

                break


def play():
    with open('coordinates.txt', 'r') as f:
        for xy in f:
            # hp = search_hp()
            # try:
            #     if hp:
            #         print(hp)
            #         shiftclick(*hp[0])
            #         while hp[1] > 0:
            #             hp = search_hp()
            #             print('health', hp[1])
            #             rightclick(*hp[0])
            #             loot()
            #             if hp[1] == 1000:
            #                 shiftclick(*hp[0])
            #
            #         rightclick(*hp[0])
            #         loot()
            # except TypeError:
            #     print('nonetype')
            #     continue
            coords = xy.split(',')
            x = int(coords[0])
            y = int(coords[1])
            x1 = pm.read_int(player_x)
            y1 = pm.read_int(player_y)
            time.sleep(2)
            print('сейчас на ',x1,y1)
            print('пойду     ',x, y)
            player.goto2(x, y)


def attack():
    hp = search_hp()
    try:
        if hp:
            print(hp)
            for i in range(hp[2], -1, -1):
                print('i= ', i)
                shiftclick(*hp[0])
                time_fiend_2 = hp[3]
                while hp[2] == i:
                    print('health', hp[1])
                    hp = search_hp()
                    if time_fiend_2 + datetime.timedelta(seconds=20) < datetime.datetime.now():
                        shiftclick(*hp[0])
                rightclick(*hp[0])
                loot()
                time.sleep(0.7)
                hp = search_hp()
    except TypeError:
        if pm.read_int(0x005680F8) < 800:

        print('nonetype')


def count_mobs():
    for coord, address in mob_map.values():
        mob_hp_percent = pm.read_int(address)
        if mob_hp_percent > 0:
            return mob_hp_percent


def search_hp():
    count_mobs = 0
    for coord, address in mob_map.values():
        mob_hp_percent = pm.read_int(address)
        time_fiend = datetime.datetime.now()
        if mob_hp_percent > 0:
            for coord2, address2 in mob_map.values():
                mob_hp_percent2 = pm.read_int(address2)
                if mob_hp_percent2 > 0:
                    count_mobs += 1
            print(coord, mob_hp_percent, count_mobs)
            return coord, mob_hp_percent, count_mobs, time_fiend


player = Move()
play()
# search_hp()
# record()

# while True:
#     print(pm.read_int(cur_exp))

#
# x = pm.read_int(player_x)
# y = pm.read_int(player_y)
# print(datetime.timedelta(now.strftime("%H:%M")) - datetime.timedelta(minutes=10))
# print(datetime.datetime.now() - datetime.timedelta(minutes=10))