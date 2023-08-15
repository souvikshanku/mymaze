import gif
import matplotlib.pyplot as plt
import numpy as np

from maze import Maze


def _get_all_grids(num_rows, num_cols):
    maze = Maze(num_rows, num_cols)

    all_steps = []

    num_rows = 2 * num_rows - 1
    num_cols = 2 * num_cols - 1
    grid = np.zeros((num_cols, num_rows))

    path = [
        (cell[0] * 2, cell[1] * 2) for cell in maze.visited
    ]

    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        grid[num_cols - 1 - y1, x1] = 1
        grid[num_cols - 1 - y2, x2] = 1
        grid[num_cols - 1 - (y1+y2)//2, (x1+x2)//2] = 1

        current_cell = (x2, num_cols - 1 - y2)
        all_steps.append((np.pad(grid, 1), current_cell))

    return all_steps


def create_maze_gif(num_rows, num_cols):
    all_steps = _get_all_grids(num_rows, num_cols)

    gif.options.matplotlib["bbox_inches"] = "tight"

    @gif.frame
    def plot(i):
        plt.gca().axis('off')

        ax = plt.gca()
        current_cell =(all_steps[i][1][0] + 0.5, all_steps[i][1][1] + 0.5)
        rect = plt.Rectangle(current_cell, 1, 1, fill=True, color="red")
        ax.add_patch(rect)

        plt.imshow(all_steps[i][0])

    frames = [plot(i) for i in range(len(all_steps))]
    gif.save(frames, 'img/maze.gif', duration=300)


if __name__ == "__main__":
    create_maze_gif(20, 10)
