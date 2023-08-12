import random

from grid import Grid


stack = []
visited = []
m = Grid(4)


def check_nbeighbours(next):
    nbrs = m.neighbours(next)

    for nbr in nbrs:
        if nbr not in visited:
            return True
    
    return False


def rdfs(start):
    if len(set(visited)) == m.size ** 2:
        return

    stack.append(start)
    visited.append(start)

    nbrs = m.neighbours(start)
    random.shuffle(nbrs)

    next = None
    for nbr in nbrs:
        if (nbr not in stack) and (nbr not in visited):
            next = nbr
            break
    
    if next:
        return rdfs(next)

    else:
        while len(stack) > 0:
            next = stack.pop()
            if check_nbeighbours(next):
                return rdfs(next)

    

rdfs((0, 0))
visited