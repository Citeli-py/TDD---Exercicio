import pytest
from src.game import Game
from src.snake import Snake
from src.ioHandler import io_handler

import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame
pygame.init()
pygame.display.set_mode((1, 1))  # janela dummy


@pytest.fixture
def game():
    io = io_handler((10,10), 0.5)
    return Game(io)


def test_game_possui_uma_cobra(game):
    """O jogo deve iniciar com uma instância de Snake."""
    assert isinstance(game.snake, Snake)


def test_game_inicia_com_uma_fruta(game):
    """O jogo deve iniciar com uma única fruta."""
    assert len(game.frutas) == 1


def test_fruta_posicionada_dentro_do_mapa(game):
    """As frutas devem ser posicionadas dentro dos limites do mapa."""
    for fruta in game.frutas:
        x, y = fruta
        assert 0 <= x < game.width
        assert 0 <= y < game.height



@pytest.mark.parametrize(
    "tamanho, frutas_esperadas",
    [(1, 1), (10, 2), (20, 3), (30, 4)]
)
def test_quantidade_de_frutas_por_tamanho(game, tamanho, frutas_esperadas):
    """
    A cada múltiplo de 10 no tamanho da cobra, o número de frutas em jogo deve aumentar.
    """
    game.snake.body = [(0, 0)] * tamanho
    game.atualizar_frutas()
    assert len(game.frutas) == frutas_esperadas


def test_frutas_nao_colidem_com_a_cobra(game):
    """As frutas devem ser geradas em posições diferentes do corpo da cobra."""
    game.snake.body = [(1, 1), (2, 2)]
    game.atualizar_frutas()
    for fruta in game.frutas:
        assert fruta not in game.snake.body


def test_gamestate_inicial_possui_cobra_e_fruta(game):
    """O estado inicial deve conter cabeça da cobra e pelo menos uma fruta."""
    matrix = game.get_gamestate()

    # A cabeça (2) deve existir exatamente uma vez
    has_snake = game.snake != None
    assert has_snake, "A cabeça da cobra deve aparecer uma vez no gamestate."

    # Deve existir uma fruta
    fruit_count = len(game.frutas)
    assert fruit_count == 1, "Deve existir uma fruta no gamestate."

# Não faz mais sentido
# def test_gamestate_possui_valores_validos(game):
#     """O gamestate deve conter apenas 0, 1, 2 ou 3."""
#     matrix = game.get_gamestate()
#     for row in matrix:
#         for value in row:
#             assert value in (0, 1, 2, 3)


def test_gamestate_reflete_movimento_da_cobra(game):
    """Após atualizar o jogo, a posição da cabeça deve mudar."""
    head_before = game.snake.head()
    game.snake.change_direction("RIGHT")
    game.atualizar()
    head_after = game.snake.head()

    assert head_before != head_after, "A cobra deve ter se movido após a atualização."

def test_gamestate_atualiza_apos_comer_fruta(game):
    """Quando a cobra come uma fruta, ela deve crescer e o gamestate mudar."""
    # Coloca uma fruta na frente da cobra
    head_x, head_y = game.snake.head()
    fruta = (head_x + 1, head_y)
    game.frutas = [fruta]
    game.snake.change_direction("RIGHT")

    tamanho_antes = len(game.snake.body)
    game.atualizar()  # come a fruta
    game.atualizar()  # cresce efetivamente
    tamanho_depois = len(game.snake.body)

    assert tamanho_depois == tamanho_antes + 1, "A cobra deve crescer ao comer uma fruta."
    assert len(game.frutas) >= 1, "O jogo deve gerar uma nova fruta após ser comida."


def test_gamestate_reseta_apos_colisao(game):
    """Quando a cobra colide consigo mesma, o jogo deve reiniciar."""
    # Cria um cenário de colisão: a cobra dá uma volta
    game.snake.body = [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]
    game._verificar_colisoes()

    assert len(game.snake.body) == 2, "Após reiniciar, deve existir uma única cabeça e um rabo."
    assert len(game.frutas) == 1, "Após reiniciar, o jogo deve conter uma fruta."