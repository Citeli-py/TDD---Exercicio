import os
import pytest
import pygame

from src.ioHandler_pygame import IoHandlerPygame

# Usa modo "headless" (sem abrir janela)
os.environ["SDL_VIDEODRIVER"] = "dummy"

@pytest.fixture
def io_handler():
    """Cria uma instância de IoHandlerPygame com tela mínima."""
    handler = IoHandlerPygame(num_cols=5, num_rows=5, cell_size=20, fps=5)
    yield handler
    pygame.quit()


# ------------------------------------------------------------------------------
# TESTES BÁSICOS DE INICIALIZAÇÃO
# ------------------------------------------------------------------------------
def test_inicializacao(io_handler):
    """Verifica se a matriz e atributos foram criados corretamente."""
    assert io_handler.x_size == 5
    assert io_handler.y_size == 5
    assert io_handler.cell_size == 20
    assert len(io_handler.matrix) == 5
    assert all(len(row) == 5 for row in io_handler.matrix)
    assert all(cell is None for row in io_handler.matrix for cell in row)
    assert isinstance(io_handler.screen, pygame.Surface)


# ------------------------------------------------------------------------------
# TESTE DE INSERÇÃO E LIMPEZA DE MATRIZ
# ------------------------------------------------------------------------------
def test_insert_e_clear_matrix(io_handler):
    """Verifica se objetos podem ser inseridos e a matriz pode ser limpa."""
    fake_surface = pygame.Surface((20, 20))
    io_handler.insert_object(fake_surface, 2, 3)
    assert io_handler.matrix[3][2] is fake_surface

    io_handler.clear_matrix()
    assert all(cell is None for row in io_handler.matrix for cell in row)


# ------------------------------------------------------------------------------
# TESTE DE ENTRADAS DE TECLADO
# ------------------------------------------------------------------------------
@pytest.mark.parametrize("key,expected", [
    (pygame.K_w, "UP"),
    (pygame.K_UP, "UP"),
    (pygame.K_s, "DOWN"),
    (pygame.K_a, "LEFT"),
    (pygame.K_d, "RIGHT"),
])
def test_record_inputs(io_handler, key, expected):
    """Simula eventos de teclado e verifica se a direção é atualizada."""
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=key))
    io_handler.record_inputs()
    assert io_handler.last_input == expected


# ------------------------------------------------------------------------------
# TESTE DE DISPLAY
# ------------------------------------------------------------------------------
def test_display_nao_crasha(io_handler):
    """Verifica se display roda sem erros mesmo com matriz vazia."""
    try:
        io_handler.display()
    except Exception as e:
        pytest.fail(f"display() lançou exceção: {e}")
