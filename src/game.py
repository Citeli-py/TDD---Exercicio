import random
from snake import Snake
from ioHandler import io_handler


class Game:
    """Controla a lógica principal do jogo Snake."""

    def __init__(self, io: io_handler):
        self.width = io.x_size
        self.height = io.y_size
        self.io = io
        self.frutas = []

        self._inicializar_objetos()

    def _inicializar_objetos(self, ):
        self.snake = Snake(
            screen_size=(self.width, self.height),
            initial_position=(self.width // 2, self.height // 2),
        )
        self._gerar_frutas_iniciais()

    # --------------------------------------------------------------------------
    # 🔸 Frutas
    # --------------------------------------------------------------------------

    def _gerar_frutas_iniciais(self) -> None:
        """Cria a quantidade inicial de frutas (1)."""
        self.frutas = [self._gerar_fruta_valida()]

    def _gerar_fruta_valida(self) -> tuple[int, int]:
        """Gera uma fruta em posição aleatória que não colida com a cobra."""
        while True:
            fruta = (
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1),
            )
            if fruta not in self.snake.body:
                return fruta

    def _atualizar_frutas(self) -> None:
        """
        Garante que a quantidade de frutas em jogo
        corresponda ao tamanho da cobra.
        """
        frutas_necessarias = 1 + len(self.snake.body) // 10

        # Adiciona frutas faltantes
        while len(self.frutas) < frutas_necessarias:
            self.frutas.append(self._gerar_fruta_valida())

        # Remove frutas excedentes (pode ocorrer após reset)
        self.frutas = self.frutas[:frutas_necessarias]

    # --------------------------------------------------------------------------
    # 🔸 Atualização do jogo
    # --------------------------------------------------------------------------

    def atualizar(self) -> None:
        """Avança o estado do jogo (movimento, colisões, frutas, etc)."""
        self.snake.move()
        self._verificar_colisoes()
        self._atualizar_frutas()

    def _verificar_colisoes(self) -> None:
        """Verifica colisões com frutas e consigo mesma."""
        self._verificar_colisao_fruta()
        self._verificar_colisao_corpo()

    def _verificar_colisao_fruta(self) -> None:
        """Verifica se a cobra comeu alguma fruta."""
        frutas_comidas = [f for f in self.frutas if self.snake.colide_fruta(f)]
        for fruta in frutas_comidas:
            self.snake.grow()
            self.frutas.remove(fruta)

    def _verificar_colisao_corpo(self) -> None:
        """Reinicia o jogo se a cobra colidir consigo mesma."""
        if self.snake.colide():
            self._reiniciar()

    # --------------------------------------------------------------------------
    # 🔸 Reinício e estado
    # --------------------------------------------------------------------------

    def _reiniciar(self) -> None:
        """Reinicia o jogo após colisão."""
        self.snake = Snake(
            screen_size=(self.width, self.height),
            initial_position=(self.width // 2, self.height // 2),
        )
        self._gerar_frutas_iniciais()

    def get_gamestate(self) -> list[list[int]]:
        """
        Retorna o estado atual do jogo como uma matriz 2D:
        0 = vazio
        1 = corpo da cobra
        2 = cabeça da cobra
        3 = fruta
        """
        matrix = [[0] * self.width for _ in range(self.height)]

        # Corpo
        for x, y in self.snake.body[1:]:
            matrix[y][x] = 1

        # Cabeça
        head_x, head_y = self.snake.head()
        matrix[head_y][head_x] = 2

        # Frutas
        for fx, fy in self.frutas:
            matrix[fy][fx] = 3

        return matrix
