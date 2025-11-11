#from src.ioHandler import io_handler
from .ioHandler_pygame import IoHandlerPygame
from .game import Game
import time
import sys

def game_loop():
    # Inicializa o IO e o jogo
    #io = io_handler((20, 10), 0.2)
    io = IoHandlerPygame(fps=5)
    game = Game(io)


    while True:
        io.record_inputs()
        io.clear_matrix()
        # Atualiza direção da cobra conforme entrada
        game.snake.change_direction(io.last_input)

        # Atualiza estado do jogo
        game.atualizar()

        # Atualiza matriz do IO para refletir o estado do jogo
        gamestate = game.get_gamestate()
        io.matrix = gamestate

        # Mostra na tela
        io.display()

        # Aguarda o próximo tick
        time.sleep(io.game_speed)

if __name__ == "__main__":
    game_loop()
