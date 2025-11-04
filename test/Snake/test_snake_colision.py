import pytest
from src.snake import Snake

import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame
pygame.init()
pygame.display.set_mode((1, 1))  # janela dummy

def test_colide_cauda():
    snake = Snake()

    snake.body = [(0,0)]
    directions = ["RIGHT", "DOWN", "LEFT", "UP"]

    for direction in directions:
        print(snake.body)
        assert not snake.colide()
        
        snake.change_direction(direction)
        snake.grow()
        snake.move()

    assert snake.colide()

def test_colide_fruta():
    snake = Snake(direction="RIGHT")
    fruta = (2,0)

    assert not snake.colide_fruta(fruta)

    snake.move()
    snake.move()

    assert snake.colide_fruta(fruta)
