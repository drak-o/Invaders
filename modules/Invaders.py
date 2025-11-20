from modules.Entity import Entity


class Invader(Entity):
    def __init__(self, x, y, img, w, h, score=0, health=1):
        super().__init__(x, y, img, w, h, score, health)

    def generateInvaders(self):
        for row in range(1, 5):
            for col in range(1, len(self.board) - 1):
                self.board[row, col] = "O"


class Squid(Invader):
    def __init__(self, x, y, img, l, h):
        super().__init__(x, y, img, l, h, 30)  # 30 points for Squid


class Crab(Invader):
    def __init__(self, x, y, img, l, h):
        super().__init__(x, y, img, l, h, 20)  # 20 points for Crab


class Octopus(Invader):
    def __init__(self, x, y, img, l, h):
        super().__init__(x, y, img, l, h, 10)  # 10 points for Octopus
