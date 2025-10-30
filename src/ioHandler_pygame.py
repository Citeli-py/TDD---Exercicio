import pygame
import sys

class IoHandlerPygame:
    def __init__(self, num_cols=15, num_rows=15, cell_size=40, fps=10):
        pygame.init()

        self.x_size = num_cols
        self.y_size = num_rows
        self.cell_size = cell_size
        self.fps = fps
        self.game_speed = 1 / fps

        self.width = num_cols * cell_size
        self.height = num_rows * cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("🐍 Snake Game")

        self.clock = pygame.time.Clock()
        self.last_input = "UP"

        # Cria a matriz com None (vazia)
        self.matrix = [[None for _ in range(num_cols)] for _ in range(num_rows)]

        # Fonte opcional para debug (ex.: pontuação)
        self.font = pygame.font.SysFont("consolas", 20)

    # ----------------------------------------------------------------------
    # Input handling
    # ----------------------------------------------------------------------
    def record_inputs(self):
        """Atualiza a direção de movimento conforme o teclado."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    self.last_input = "UP"
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    self.last_input = "DOWN"
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    self.last_input = "LEFT"
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.last_input = "RIGHT"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    # ----------------------------------------------------------------------
    # Rendering
    # ----------------------------------------------------------------------
    def display(self, title_info=None):
        """Renderiza todos os objetos presentes na matriz."""
        self.screen.fill((20, 20, 20))

        for y in range(self.y_size):
            for x in range(self.x_size):
                obj = self.matrix[y][x]
                
                if obj:
                    self.screen.blit(obj, (x * self.cell_size, y * self.cell_size))
                    # Se for cor (tuple RGB), desenha um retângulo
                else:
                    rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (0,0,0), rect)

                pygame.draw.rect(
                    self.screen,
                    (50, 50, 50),
                    pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size),
                    1,
                )


        pygame.display.flip()

    # ----------------------------------------------------------------------
    # Utility
    # ----------------------------------------------------------------------
    def insert_object(self, obj, x, y):
        """Insere um objeto (sprite, cor ou Surface) na posição x, y."""
        if 0 <= x < self.x_size and 0 <= y < self.y_size:
            self.matrix[y][x] = obj

    def clear_matrix(self):
        """Reseta a matriz."""
        self.matrix = [[None for _ in range(self.x_size)] for _ in range(self.y_size)]
