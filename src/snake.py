from pygame import image, Surface

DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

class Snake:
    def __init__(self, initial_position=(0, 0), screen_size = (10, 10), direction="UP"):
        self.body = [initial_position, (initial_position[0]+1, initial_position[1])]
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]
        self.direction = direction
        self.grow_pending = False

        # === Cabeça ===
        self.sprites_head = {
            "UP": image.load("src/assets/snake/head_up.png").convert_alpha(),
            "RIGHT": image.load("src/assets/snake/head_right.png").convert_alpha(),
            "DOWN": image.load("src/assets/snake/head_down.png").convert_alpha(),
            "LEFT": image.load("src/assets/snake/head_left.png").convert_alpha(), 
        }

        # === Corpo (segmentos intermediários) ===
        self.sprites_body = {
            "horizontal": image.load("src/assets/snake/body_horizontal.png").convert_alpha(),
            "vertical": image.load("src/assets/snake/body_vertical.png").convert_alpha(),
            "topleft": image.load("src/assets/snake/body_topleft.png").convert_alpha(),
            "topright": image.load("src/assets/snake/body_topright.png").convert_alpha(),
            "bottomleft": image.load("src/assets/snake/body_bottomleft.png").convert_alpha(),
            "bottomright": image.load("src/assets/snake/body_bottomright.png").convert_alpha(), 
        }

        # === Cauda ===
        self.sprites_tail = {
            "up": image.load("src/assets/snake/tail_up.png").convert_alpha(),
            "right": image.load("src/assets/snake/tail_right.png").convert_alpha(),
            "down": image.load("src/assets/snake/tail_down.png").convert_alpha(),
            "left": image.load("src/assets/snake/tail_left.png").convert_alpha(), 
        }


    def head(self):
        return self.body[0]

    def change_direction(self, new_direction):
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if opposite[self.direction] != new_direction:
            self.direction = new_direction

    def move(self):
        dx, dy = DIRECTIONS[self.direction]
        new_x = (self.head()[0] + dx)%self.screen_width
        new_y = (self.head()[1] + dy)%self.screen_height

        new_head = ( new_x, new_y )
        self.body.insert(0, new_head)

        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True


    def colide(self) -> bool:
        """Verifica se a cobra colidiu com ela mesma."""
        return self.head() in self.body[1:]

    def colide_fruta(self, fruta) -> bool:
        """Verifica se a cobra colidiu com a fruta."""
        return self.head() == fruta
    
    
    def _wrapped_dir(self, p1, p2) -> tuple[int, int]:
        """
        Calcula a direção entre duas coordenadas considerando warp.
        Retorna uma tupla (x,y), onde x e y podem ser -1, 0 ou 1.
        """


        def normalize(a, b, size)->int:
            diff = a - b
            if diff > size // 2:
                diff -= size
            elif diff < -size // 2:
                diff += size
            return diff
        
        size = (self.screen_width, self.screen_height)
        
        x = normalize(p1[0], p2[0], size[0])
        y = normalize(p1[1], p2[1], size[1])

        return (x, y)
    
    def _get_tail_sprite(self, ) -> tuple[tuple[int, int], Surface]:
        # === Cauda ===
        if len(self.body) > 1:
            tail = self.body[-1]
            before_tail = self.body[-2]

            dx = before_tail[0] - tail[0]
            dy = before_tail[1] - tail[1]

            if dx == 1:
                direction = "left"
            elif dx == -1:
                direction = "right"
            elif dy == 1:
                direction = "up"
            else:
                direction = "down"

        return (tail, self.sprites_tail[direction])
    
    def _get_body_sprite(self, pos: int) -> tuple[tuple[int, int], Surface]:

        prev_pos = self.body[pos - 1]
        curr_pos = self.body[pos]
        next_pos = self.body[pos + 1]

        # Vetores relativos
        dir_prev = self._wrapped_dir(prev_pos, curr_pos)
        dir_next = self._wrapped_dir(next_pos, curr_pos)
        
         # Corpo reto
        if dir_prev[0] == dir_next[0]:
            sprite = self.sprites_body["vertical"]
        elif dir_prev[1] == dir_next[1]:
            sprite = self.sprites_body["horizontal"]
        else:
            # Curvas — combinação de direções
            curva = None
            if (dir_prev, dir_next) in [((0, -1), (-1, 0)), ((-1, 0), (0, -1))]:
                curva = "topleft"
            elif (dir_prev, dir_next) in [((0, -1), (1, 0)), ((1, 0), (0, -1))]:
                curva = "topright"
            elif (dir_prev, dir_next) in [((0, 1), (-1, 0)), ((-1, 0), (0, 1))]:
                curva = "bottomleft"
            elif (dir_prev, dir_next) in [((0, 1), (1, 0)), ((1, 0), (0, 1))]:
                curva = "bottomright"

            sprite = self.sprites_body[curva]

        return (curr_pos, sprite)


    
    def get_sprites(self) -> list[tuple[tuple[int, int], Surface]]:
        sprites = []

        # === Cabeça ===
        head_pos = self.body[0]
        sprites.append((head_pos, self.sprites_head[self.direction]))

        # === Corpo (exceto cabeça e cauda) ===
        for i in range(1, len(self.body) - 1):
            sprites.append(self._get_body_sprite(i))

        sprites.append(self._get_tail_sprite())

        return sprites


