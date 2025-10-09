from ioHandler import io_handler
from game import Game
import time
import sys

def game_loop():
    # Inicializa o IO e o jogo
    io = io_handler((20, 10), 0.2)
    game = Game(io)

    io.record_inputs()

    while True:
        # Atualiza direção da cobra conforme entrada
        if io.last_input == 'w':
            game.snake.change_direction("UP")
        elif io.last_input == 's':
            game.snake.change_direction("DOWN")
        elif io.last_input == 'a':
            game.snake.change_direction("LEFT")
        elif io.last_input == 'd':
            game.snake.change_direction("RIGHT")
        elif io.last_input == 'end':
            print("Jogo encerrado.")
            sys.exit(0)

        # Atualiza estado do jogo
        game.atualizar()

        # Atualiza matriz do IO para refletir o estado do jogo
        gamestate = game.get_gamestate()
        io.matrix = gamestate

        # Mostra na tela
        io.display()
        print(f"Tamanho da cobra: {len(game.snake.body)} | Frutas: {len(game.frutas)}")

        # Aguarda o próximo tick
        time.sleep(io.game_speed)

if __name__ == "__main__":
    game_loop()
