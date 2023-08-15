import random


def _nbeighbours_unvisited(next, visited, maze):
    nbrs = maze.neighbours(next)

    for nbr in nbrs:
        if nbr not in visited:
            return True
    
    return False


def rdfs(maze, start, stack, visited):
    if len(set(visited)) == maze.num_rows * maze.num_cols:
        return

    stack.append(start)
    visited.append(start)

    nbrs = maze.neighbours(start)
    random.shuffle(nbrs)

    next = None
    for nbr in nbrs:
        if (nbr not in stack) and (nbr not in visited):
            next = nbr
            break

    if next:
        return rdfs(maze, next, stack, visited)

    else:
        while len(stack) > 0:
            next = stack.pop()
            visited.append(next)

            if _nbeighbours_unvisited(next, visited, maze):
                return rdfs(maze, next, stack, visited)


if __name__ == "__main__":
    from maze import Maze

    stack = []
    visited = []
    m = Maze(10, 10)
    rdfs(m, (0, 0), stack, visited)

    print(len(set(visited)), len(visited))
