from cell import Cell
import random


def check_nbrs(cell: Cell, stack):
    nbrs = cell.neighbours()
    for nbr in nbrs:
        if (nbr not in stack) and (not nbr.visited):
            return nbr
    
    return False


stack = []
path = []
in_path = set()

def rdfs(start: Cell):
    print(start, stack)
    if len(in_path) == start.size ** 2:
        return

    stack.append(start)
    path.append(start)
    in_path.add((start.x, start.y))

    nbrs = start.neighbours()
    random.shuffle(nbrs)

    nbr_to_visit = None
    for nbr in nbrs:
        if (nbr not in stack) and (not nbr.visited):
            nbr_to_visit = nbr
            break
    
    if nbr_to_visit:
        rdfs(nbr_to_visit)
    else:
        start.visted = True

        while True:
            next = stack.pop()
            if check_nbrs(next, stack):
                break
        
        rdfs(next)

    return stack

stack = []
path = []
in_path = set()

size = 4

m = [[
    Cell(x, y, size) for y in range(size)
] for x in range(size)]


stack = rdfs(m[0][0])
len(path)