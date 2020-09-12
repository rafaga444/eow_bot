from pymem import *
import win32com.client

import keyboard
import move as b
import time

player_mn = 0x005680FC
player_hp = 0x005680F8
player_y = 0x01355EB8
player_x = 0x0056E6C8



pm = pymem.Pymem("MUDClient.exe")



class Move:
    def __init__(self):
        self.x = ord(pm.read_char(player_x))
        self.y = ord(pm.read_char(player_y))

    def goto(self, x, y):
        while self.x != x or self.y != y:
            self.y = ord(pm.read_char(player_y))
            self.x = ord(pm.read_char(player_x))
            if self.x < x and self.y < y:  # pgdn num3
                b.go_right_down()
            elif self.x > x and self.y < y:  # num1
                b.go_left_down()
            elif self.x > x and self.y > y:  # num7
                b.go_left_up()
            elif self.x < x and self.y > y:  # num9
                b.go_right_up()
            elif self.x < x:
                b.go_right()
            elif self.x > x:
                b.go_left()
            elif self.y > y:
                b.go_up()
            elif self.y < y:
                b.go_down()
            # print([self.x, self.y])


def record():
    x = ord(pm.read_char(player_x))
    y = ord(pm.read_char(player_y))
    coord_list = []
    with open('coordinates.txt', mode='w', encoding='UTF-8') as f:
        f.write(str(x) + ',' + str(y) + '\n')
        while True:
            x1 = ord(pm.read_char(player_x))
            y1 = ord(pm.read_char(player_y))
            if x != x1 or y != y1:
                coord_list.append(str(x1) + ',' + str(y1) + '\n')
                x = x1
                y = y1

            if keyboard.is_pressed('q'):
                for coord in coord_list:
                    f.write(str(coord))

                break


def play():
    with open('coordinates.txt', 'r') as f:
        for xy in f:
            coords = xy.split(',')
            x = int(coords[0])
            y = int(coords[1])
            print([x, y])
            player.goto(x, y)


player = Move()

#print(pm.read_int(player_mn))

pm.read_bytes(0xf99f1c0, 1100600)