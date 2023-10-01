import pgzrun
import pygame
import math
from pgzhelper import *

WIDTH = 800
HEIGHT = 600
TITLE = "TANK GAME"

player = Actor("tank_red_body")


red_gun = Actor("tank_red_barrel")


def draw():
    screen.clear()
    player.draw()
    red_gun.draw()


def update():
    red_gun.pos = player.pos

    if keyboard.a:
        player.angle += 1
        red_gun.angle += 1
    if keyboard.d:
        player.angle -= 1
        red_gun.angle -= 1
    if keyboard.w:
        player.x += math.cos(math.radians(player.angle + 90)) * 4
        player.y -= math.sin(math.radians(player.angle + 90)) * 4
    if keyboard.s:
        player.move_right(4)
        


pgzrun.go()