"""
API compatibility tests based on http://www.raspberrypi.org/documentation/usage/minecraft/

We do not want to break this API - we do not want to be responsible for sad children (and adults) whose awesome Minecraft code no longer works.

Ergo this suite is a translation of that usage guide

Currently it doesn't actually test the __success__ of any of these commands, but it at least verifies that the commands still exist, which is the most likely cause of breakage
"""

import pytest

from mcpi import minecraft
from mcpi.minecraft import block
from time import sleep

@pytest.fixture(scope="module")
def mc():
    return minecraft.Minecraft.create()


def test_hello_world(mc):
    mc.postToChat("Hello world")


def test_get_pos(mc):
    x, y, z = mc.player.getPos()


def test_teleport(mc):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y+100, z)


def test_set_block(mc):
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1, y, z, 1)


def test_blocks_as_variables(mc):
    x, y, z = mc.player.getPos()

    dirt = block.DIRT.id
    mc.setBlock(x, y, z, dirt)


def test_special_blocks(mc):
    x, y, z = mc.player.getPos()

    wool = 35
    mc.setBlock(x, y, z, wool, 1)


def test_set_blocks(mc):
    stone = 1
    x, y, z = mc.player.getPos()
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)


def test_dropping_blocks_as_you_walk(mc):
    """
    'The following code will drop a flower behind you wherever you walk'

    We're not walking, and we don't want the infinite loop from the example, but this should do
    """

    flower = 38

    for i in xrange(10):
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, flower)
        sleep(0.1)
