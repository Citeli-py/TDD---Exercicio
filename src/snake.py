DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

class Snake:
    def __init__(self, initial_position=(0, 0), screen_size = (10, 10), direction="UP"):
        self.body = [initial_position]
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]
        self.direction = direction
        self.grow_pending = False

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
