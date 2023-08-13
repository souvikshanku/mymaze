import numpy as np
import matplotlib.pyplot as plt

from rdfs import rdfs


class Maze:
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

    def create(self):
        self.stack = []
        self.visited = []

        rdfs(self, (0, 0), self.stack, self.visited)

    def generate_grid(self):
        size = 2 * self.size - 1
        self.grid = np.zeros((size, size))

        path = [
            (cell[0] * 2, cell[1] * 2) for cell in self.visited
        ]

        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]

            self.grid[size - 1 - y1, x1] = 1
            self.grid[size - 1 - y2, x2] = 1
            self.grid[size - 1 - (y1+y2)//2, (x1+x2)//2] = 1

        self.grid = np.pad(self.grid, 1)

        return self.grid

    def plot(self):
        grid = self.generate_grid()
        plt.gca().axis('off')
        plt.imsave("img/maze.png", grid)



if __name__ == "__main__":
    m = Maze(20)
    m.create()
    grid = m.generate_grid()

    print(grid)
    m.plot()
