import random
from snake import Snake
from ioHandler import io_handler


class Game:
    def __init__(self, io_handler: io_handler):
        self.width = io_handler.x_size
        self.height = io_handler.y_size
        self.io = io_handler
        self.snake = Snake(screen_size=(self.width, self.height), initial_position=(self.width//2, self.height//2))
        self.frutas = []
        self.gerar_frutas_iniciais()

    def gerar_frutas_iniciais(self):
        """Cria a quantidade inicial de frutas (1)."""
        self.frutas = [self._gerar_fruta()]

    def _gerar_fruta(self):
        """Gera uma fruta em posição aleatória que não colida com a cobra."""
        while True:
            fruta = (
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1),
            )
            if fruta not in self.snake.body:
                return fruta

    def atualizar_frutas(self):
        """Atualiza a quantidade de frutas com base no tamanho da cobra."""
        tamanho = len(self.snake.body)
        # a cada múltiplo de 10, mais uma fruta (1 fruta base + tamanho // 10)
        frutas_necessarias = 1 + tamanho // 10
        while len(self.frutas) < frutas_necessarias:
            self.frutas.append(self._gerar_fruta())
        # remove frutas excedentes (se houver)
        self.frutas = self.frutas[:frutas_necessarias]

    def atualizar(self) -> list[list[int]]:
        """Avança o estado do jogo (movimento, colisões, frutas, etc)."""
        self.snake.move()
        self._verificar_colisoes()
        self.atualizar_frutas()

    def _verificar_colisoes(self):
        """Verifica colisões com frutas e consigo mesma."""
        # Comer fruta
        for fruta in list(self.frutas):
            if self.snake.colide_fruta(fruta):
                self.snake.grow()
                self.frutas.remove(fruta)
        # Colisão com o próprio corpo (reinicia)
        if self.snake.colide():
            self._reiniciar()

    def _reiniciar(self):
        """Reinicia o jogo após colisão."""
        self.snake = Snake(screen_size=(self.width, self.height), initial_position=(self.width//2, self.height//2))
        self.gerar_frutas_iniciais()
    
    def get_gamestate(self) -> list[list[int]]:
        """
        Retorna o estado atual do jogo como uma matriz 2D:
        0 = vazio
        1 = corpo da cobra
        2 = cabeça da cobra
        3 = fruta
        """
        # Cria matriz vazia
        matrix = [[0 for _ in range(self.width)] for _ in range(self.height)]

        # Marca corpo da cobra
        for x, y in self.snake.body[1:]:
            if 0 <= x < self.width and 0 <= y < self.height:
                matrix[y][x] = 1

        # Marca cabeça
        head_x, head_y = self.snake.head()
        if 0 <= head_x < self.width and 0 <= head_y < self.height:
            matrix[head_y][head_x] = 2

        # Marca frutas
        for fx, fy in self.frutas:
            if 0 <= fx < self.width and 0 <= fy < self.height:
                matrix[fy][fx] = 3

        return matrix
