import pydirectinput as pyat
from clicks import leftclick


def go_up():
    leftclick(215, 180)


def go_left_up():
    leftclick(183, 181)


def go_right_up():
    leftclick(237, 180)


def go_left_down():
    leftclick(183, 237)


def go_right_down():
    leftclick(237, 237)


def go_left():
    leftclick(172, 212)


def go_right():
    leftclick(240, 213)


def go_down():
    leftclick(210, 241)
