import pytest
from src.snake import Snake


def test_colide_cauda():
    snake = Snake()
    directions = ["RIGHT", "DOWN", "LEFT", "UP"]

    for direction in directions:
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
