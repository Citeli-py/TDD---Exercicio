class Snake:
    def __init__(self, initial_position=(0, 0)):
        self.body = [initial_position]  # lista de tuplas (x,y)
        self.direction = "UP"
        self.grow_pending = False

    def change_direction(self, new_direction):
        # impede que a cobra faça 180° direto
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if opposite[self.direction] != new_direction:
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)

        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending = True
