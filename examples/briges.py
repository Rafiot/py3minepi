#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mcpi import minecraft

mc = minecraft.Minecraft.create()


def new_pos(curpos):
    prec = curpos.clone()
    curpos += direction
    if int(prec.x) != int(curpos.x) and int(prec.z) != int(curpos.z):
        if direction.x < 0:
            mc.setBlock(curpos.x + 1, curpos.y, curpos.z, 1)
        else:
            mc.setBlock(curpos.x - 1, curpos.y, curpos.z, 1)
    return curpos


while True:
    dir_input = input("""Direction of the brige:
    1. Up
    2. Down
    3. Horizontal
    Usage: 1, 2 or 3 <space> length (Default: 30)""")

    out = dir_input.split()
    what = int(out[0])
    if len(out) == 2:
        length = int(out[1])
    else:
        length = 30

    curpos = mc.player.getPos()
    direction = mc.player.getDirection()

    # Up/Down/Horizontal is decided bu the user
    direction.y = 0
    # Try to go more or less straight
    direction.x = round(direction.x, 2)
    direction.z = round(direction.z, 2)

    # To avoid creating a block at our exact position
    curpos += curpos.down()

    if what == 1:
        for i in range(length):
            mc.setBlock(curpos.x, curpos.y, curpos.z, 1)
            curpos = new_pos(curpos)
            curpos += curpos.up()
    elif what == 2:
        for i in range(length):
            mc.setBlock(curpos.x, curpos.y, curpos.z, 1)
            curpos = new_pos(curpos)
            curpos += curpos.down()
    elif what == 3:
        for i in range(length):
            mc.setBlock(curpos.x, curpos.y, curpos.z, 1)
            curpos = new_pos(curpos)
