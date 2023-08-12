import numpy as np
import matplotlib.pyplot as plt


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


def plot(visited, size):

    size = 2 * size - 1
    maze = np.zeros((size, size))

    path = [
        (cell[0] * 2, cell[1] * 2) for cell in visited
    ]

    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        maze[size - 1 - y1, x1] = 1
        maze[size - 1 - y2, x2] = 1

        maze[size - 1 - (y1+y2)//2, (x1+x2)//2] = 1

    plt.imshow(np.pad(maze, 1))
    plt.gca().axis('off')


plot(visited, m.size)