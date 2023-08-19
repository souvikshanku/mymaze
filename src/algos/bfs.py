from collections import defaultdict


def bfs(adj_list, start, end):
    distance_from_start = defaultdict(int)
    queue = [start]
    visited = [start]
    distance_from_start[start] = 0

    while len(queue) > 0:
        distance = distance_from_start[queue[0]]
        next = queue.pop(0)
        nbrs = adj_list[next]
        visited.append(next)

        for nbr in nbrs:
            if nbr not in visited:
                queue.append(nbr)
                distance_from_start[nbr] = distance + 1

            if nbr == end:
                return distance_from_start

    return distance_from_start
