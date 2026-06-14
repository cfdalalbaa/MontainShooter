#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame as pg

from asset.Const import WIND_WIDTH, WIND_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIND_WIDTH, WIND_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
