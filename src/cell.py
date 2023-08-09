class Cell:
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.lw, self.rw, self.uw, self.dw = [0] * 4

        self.visited = False

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self) -> str:
        return str((self.x, self.y))

    def neighbours(self):
        nbrs = []
        if (self.x - 1) >= 0:
            nbrs.append(Cell(self.x - 1, self.y, self.size))
        if (self.y - 1) >= 0:
            nbrs.append(Cell(self.x, self.y - 1, self.size))
        if (self.x + 1) >= 0:
            nbrs.append(Cell(self.x + 1, self.y, self.size))
        if (self.y + 1) >= 0:
            nbrs.append(Cell(self.x, self.y + 1, self.size))
        
        return nbrs
