import win32gui
from pymem import *
import win32com.client
import pyautogui
import keyboard
from clicks import shiftclick
import move as b
import time
from monster_map import mob_map

hwndscr = win32gui.FindWindow(None, 'Epoch of Worlds')
pm = pymem.Pymem("MUDClient.exe")


player_mn = 0x005680FC
player_hp = 0x005680F8
player_hp_percent = pm.read_int(0x578C20)/10
player_y = 0x01355EB8
player_x = 0x0056E6C8
cur_map = 0x51DF44
cur_exp = 0x0056810C
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

    def goto(self, x, y):
        while self.x != x or self.y != y:
            self.y = pm.read_int(player_y)
            self.x = pm.read_int(player_x)
            if self.x < x and self.y < y:  # pgdn num3
                b.go_right_down()

            elif self.x > x and self.y < y:  # num1
                b.go_left_down()

            elif self.x > x and self.y > y:  # num7
                b.go_left_up()

            elif self.x < x and self.y > y:  # num9
                b.go_right_up()

            if self.x < x:
                b.go_right()

            elif self.x > x:
                b.go_left()

            elif self.y > y:
                b.go_up()

            elif self.y < y:
                b.go_down()

            # print([self.x, self.y])

    def goto2(self, x, y):
        while self.x != x or self.y != y:
            previous_coord = []
            self.y = pm.read_int(player_y)
            self.x = pm.read_int(player_x)

            if self.x < x:
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
            x1 = pm.read_int(player_x)
            y1 = pm.read_int(player_y)

            if x != x1 or y != y1:
                print('x', x, 'y', y)
                time.sleep(1)
                coord_list.append(str(x1) + ',' + str(y1) + '\n')
                print(str(x1) + ',' + str(y1))
                x = x1
                y = y1
            elif

            if keyboard.is_pressed('q'):
                for coord in coord_list:
                    f.write(str(coord))

                break


def play():
    with open('coordinates.txt', 'r') as f:

        for xy in f:
            # #get_target()
            # for coord, address in mob_map.values():
            #     mob_hp_percent = pm.read_int(address)/10
            #
            #     while mob_hp_percent > 0:
            #         for coord, address in mob_map.values():
            #             mob_hp_percent = pm.read_int(address) / 10
            #             print(mob_hp_percent, coord)
            #     else:
            #         continue


            coords = xy.split(',')
            x = int(coords[0])
            y = int(coords[1])
            print([x, y])
            player.goto2(x, y)





player = Move()




def get_target():
    for coord, address in mob_map.values():
        mob_hp_percent = pm.read_int(address)
        if mob_hp_percent > 0:
            shiftclick(*coord)
            print(coord)
            return True

def get_target_hp():
    for coord, address in mob_map.values():
        mob_hp_percent = pm.read_int(address)
        if mob_hp_percent >0:
            return mob_hp_percent


#play()

record()