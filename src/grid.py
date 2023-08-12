import numpy as np


class Grid:
    def __init__(self, size) -> None:
        self.size = size
        self.maze = np.zeros((size , size))

    def neighbours(self, cell: tuple[int, int]):
        x, y = cell
        nbrs = []
        if (x - 1) >= 0:
            nbrs.append((x - 1, y))
        if (y - 1) >= 0:
            nbrs.append((x, y - 1))
        if (x + 1) < self.size:
            nbrs.append((x + 1, y))
        if (y + 1) < self.size:
            nbrs.append((x, y + 1))

        return nbrs