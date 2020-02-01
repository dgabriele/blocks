from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN
from .game import Game

game = Game()


@game(key=K_LEFT)
def move_left(event):
    game.state.block.x -= 100

@game(key=K_RIGHT)
def move_right(event):
    game.state.block.x += 100

@game(key=K_DOWN)
def move_down(event):
    game.state.block.y += 100

@game(key=K_UP)
def move_up(event):
    game.state.block.y -= 100
