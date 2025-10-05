import pytest
from src.snake import Snake

def test_snake_initial_position():
    snake = Snake(initial_position=(5, 5))
    assert snake.body == [(5, 5)]
    assert snake.direction == "UP"

def test_snake_move_up():
    snake = Snake(initial_position=(5, 5))
    snake.move()
    assert snake.body[0] == (5, 4)  # y diminui ao ir para cima

def test_snake_move_right():
    snake = Snake(initial_position=(5, 5))
    snake.change_direction("RIGHT")
    snake.move()
    assert snake.body[0] == (6, 5)

def test_snake_grow():
    snake = Snake(initial_position=(5, 5))
    snake.grow()
    snake.move()
    assert len(snake.body) == 2  # deve ter crescido
    assert snake.body[0] == (5, 4)  # cabeça nova posição
    assert snake.body[1] == (5, 5)  # cauda antiga posição
