#
# This is an adapted version of the Breadth First Search (BFS) algorithm
# to make it work on the PAC-MAN maze.
#
# Credit: Anna Bernbaum and the GTAs of Computing-2
#
# Updated Breadth First Search

import numpy as np
from multiprocessing import Queue


def shortest_path(walls, start, end):  # can access walls from agents state.data.walls gives numpy 2D array, true = walls, false = space
    start = [start[0], start[1]]
    end = [end[0], end[1]]
    if start == end:
        return [start]
    neighbours = Queue()  # queue storing the next positions to explore
    neighbours.enqueue(start)
    counts = np.zeros((walls.width, walls.height), dtype=int)  # 2D array to store the distance from the start to all visted points
    predecessors = np.zeros((counts.shape[0], counts.shape[1], 2), dtype=int)  # 2D array storing the predecessors (past points allowing path to be retraced)
    counts[start[0], start[1]] = 1
    # loop until the end position is found
    while not neighbours.isEmpty():
        n = neighbours.dequeue()
        print n
        if n == end:
            print "path found!", n, counts[n[0]][n[1]]
            break  # path found
        # add all the valid neighbours to the list and remember from where they came from
        for neighbour in [[n[0] - 1, n[1]], [n[0] + 1, n[1]], [n[0], n[1] - 1], [n[0], n[1] + 1]]:
            if not walls[neighbour[0]][neighbour[1]] and counts[neighbour[0], neighbour[1]] == 0:
                neighbours.enqueue(neighbour)
                predecessors[neighbour[0], neighbour[1]] = n
                counts[neighbour[0], neighbour[1]] = counts[n[0], n[1]] + 1
    print 'here 0'
    if counts[end[0], end[1]] == 0:
        return []  # path not found
    print 'here 1'
    path = []
    n = end
    print end, counts[end[0], end[1]]
    # reconstruct the path
    print counts
    while n != start:
        #print n
        if n == start:
            break
        path.append(n)
        n = predecessors[n[0], n[1]].tolist()
    path.append(start)
    print 'here 2'
    print counts

    return path

