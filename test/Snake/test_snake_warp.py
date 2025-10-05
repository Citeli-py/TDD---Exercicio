import pytest
from src.snake import Snake

def test_snake_wrap_right_wall():
    """
    Verifica se a cobra atravessa a parede da direita e aparece no lado esquerdo
    """
    snake = Snake(initial_position=(9, 5), screen_size=(10, 10))
    snake.change_direction("RIGHT")
    snake.move()
    assert snake.head() == (0, 5)


def test_snake_wrap_left_wall():
    """
    Verifica se a cobra atravessa a parede da esquerda e aparece no lado direito
    """
    snake = Snake(initial_position=(0, 5), screen_size=(10, 10))
    snake.change_direction("LEFT")
    snake.move()
    assert snake.head() == (9, 5)


def test_snake_wrap_top_wall():
    """
    Verifica se a cobra atravessa a parede de cima e aparece embaixo
    """
    snake = Snake(initial_position=(5, 0), screen_size=(10, 10))
    snake.change_direction("UP")
    snake.move()
    assert snake.head() == (5, 9)


def test_snake_wrap_bottom_wall():
    """
    Verifica se a cobra atravessa a parede de baixo e aparece em cima
    """
    snake = Snake(initial_position=(5, 9), screen_size=(10, 10))
    snake.change_direction("DOWN")
    snake.move()
    assert snake.head() == (5, 0)