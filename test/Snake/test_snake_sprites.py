import pytest
from src.snake import Snake

import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame
pygame.init()
pygame.display.set_mode((1, 1))  # janela dummy

from pygame import Surface

def test_has_cabeca():
    snake = Snake()
    sprites = snake.get_sprites()

    head = sprites[0]
    assert isinstance(head[1], Surface)

    # verificar se a posição do sprite é a mesma da cabeça
    assert head[0] == snake.head()


def test_snake_igual_sprites():
    snake = Snake()
    snake.body = [(1, 1), (1, 2), (2, 2), (2, 1), (3, 1)]

    i=0
    for (pos, sprite) in snake.get_sprites():
        assert pos == snake.body[i]
        i+=1 