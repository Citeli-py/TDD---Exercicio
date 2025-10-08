import pytest
from src.game import Game
from src.snake import Snake


@pytest.fixture
def game():
    return Game(width=10, height=10)


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
    game.snake.body = [(1, 1), (2, 2), (3, 3)]
    game.atualizar_frutas()
    for fruta in game.frutas:
        assert fruta not in game.snake.body
