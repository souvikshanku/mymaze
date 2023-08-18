from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt

from algos import bfs, rdfs


class Maze:
    def __init__(self, num_rows, num_cols) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols

        self.create()
        self.generate_grid()

        self.solved = False
        self.adj_list = defaultdict(list)
        for i in range(len(self.visited) - 1):
            self.adj_list[self.visited[i]].append(self.visited[i + 1])

    def neighbours(self, cell: tuple[int, int]):
        x, y = cell
        nbrs = []
        if (x - 1) >= 0:
            nbrs.append((x - 1, y))
        if (y - 1) >= 0:
            nbrs.append((x, y - 1))
        if (x + 1) < self.num_rows:
            nbrs.append((x + 1, y))
        if (y + 1) < self.num_cols:
            nbrs.append((x, y + 1))

        return nbrs

    def create(self):
        self.stack = []
        self.visited = []

        rdfs(self, (0, 0), self.stack, self.visited)

    def generate_grid(self):
        num_rows = 2 * self.num_rows - 1
        num_cols = 2 * self.num_cols - 1
        self.grid = np.zeros((num_cols, num_rows))

        path = [
            (cell[0] * 2, cell[1] * 2) for cell in self.visited
        ]

        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]

            self.grid[num_cols - 1 - y1, x1] = 1
            self.grid[num_cols - 1 - y2, x2] = 1
            self.grid[num_cols - 1 - (y1+y2)//2, (x1+x2)//2] = 1

        self.grid = np.pad(self.grid, 1)

    def solve(self, start=None, end=None):
        self.shortest_path = []

        if start is None:
            start = (0, 0)
        if end is None:
            end = (self.num_rows - 1, self.num_cols - 1)

        distance_from_start = bfs(self.adj_list, start, end)

        distance = distance_from_start[end]
        current = end

        while current != start:
            adj_nbrs = self.adj_list[current]
            for nbr in adj_nbrs:
                if distance_from_start[nbr] == distance - 1:
                    self.shortest_path.append(current)
                    current = nbr
                    distance -= 1

        self.shortest_path.append(start)
        self.shortest_path = self.shortest_path[::-1]
        self.solved = True

    def _get_solved_path_grid(self):
        shortest_path = [(cell[0] * 2, cell[1] * 2) for cell in self.shortest_path]
        to_paint = []
        num_cols = 2 * self.num_cols - 1

        for i in range(len(self.shortest_path) - 1):
            x1, y1 = shortest_path[i]
            x2, y2 = shortest_path[i + 1]

            to_paint.append((x1, num_cols - 1 - y1))
            to_paint.append((x2, num_cols - 1 - y2))
            to_paint.append(((x1+x2)//2, num_cols - 1 - (y1+y2)//2))

        return to_paint

    def plot(self):
        # Unsolved Maze
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        ax.imshow(self.grid)
        ax.axis('off')
        fig.savefig("img/maze.png", bbox_inches = "tight")

        # Solved Maze
        if self.solved:
            fig = plt.figure(figsize=(10, 10))
            ax = fig.add_subplot(111)
            ax.imshow(self.grid)

            for cell in self._get_solved_path_grid():
                cell = (cell[0] + 0.5, cell[1] + 0.5)
                rect = plt.Rectangle(cell, 1, 1, fill=True, color="red")
                ax.add_patch(rect)

            ax.axis('off')
            fig.savefig("img/maze_solved.png", bbox_inches = "tight")


if __name__ == "__main__":
    m = Maze(40, 20)
    m.solve()
    print(m.grid)
    print(len(m.shortest_path))
    m.plot()
