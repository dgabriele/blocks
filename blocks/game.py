import pygame as pg

from pygame import Surface, Rect, Color

from pybiz.contrib.pygame import PygameGame


class Game(PygameGame):
    def on_update(self, tick):
        if not tick:
            # on first iteration of main loop...
            self.state.bg = [255, 0, 0]
            self.state.block = self.biz.Block(
                x=0, y=0, w=100, h=100, c=[0, 0, 255]
            )

    def on_draw(self, tick):
        screen = self.state.screen
        block = self.state.block
        screen.fill(self.state.bg)
        pg.draw.rect(screen, block.color, block.rect)
