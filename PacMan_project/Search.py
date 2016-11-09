
class PacmanProblem:
    # grid is a 2D array
    # pacman & capsules are tuples (r,c)
    def __init__(self, Grid, pacman, capsules):
        self.Grid = Grid
        self.rows = len(Grid)
        self.columns = len(Grid[0])
        self.pacman = pacman
        self.getCapsules = capsules

    # Since this problem requires us to output the path taken
    # to reach the food capsule, we'll store the path in the state
    # state has this form:
    # tuple(tuple(r,c), [tuple(r1,c1), tuple(r2,c2), ...])
    # where the first tuple is the current position of pacman
    # and the list stores the path taken to reach here
    def getStartState(self):
        return (self.pacman, [self.pacman])

    def isGoalState(self, state):
        return state[0] == self.getCapsules

    def getSuccessors(self, state):
        moves = []
        path = state[1]

        def getMove(r, c):
            if self.Grid[r][c] != '%':
                newPath = list(path)
                move = (r, c)
                newPath.append(move)
                moves.append((move, newPath))

        if state[0][0] > 0:  # Go UP
            getMove(state[0][0] - 1, state[0][1])
        if state[0][1] > 0:  # Go LEFT
            getMove(state[0][0], state[0][1] - 1)
        if state[0][1] < self.columns - 1:  # Go RIGHT
            getMove(state[0][0], state[0][1] + 1)
        if state[0][0] < self.rows - 1:  # Go DOWN
            getMove(state[0][0] + 1, state[0][1])
        return moves

def graphSearch(problem, strategy):
    start = problem.getStartState()
    explored = set([start[0]])
    strategy.push(start)

    while not strategy.empty():
        node = strategy.pop()
        if problem.isGoalState(node):
            return node[1]
        for move in problem.getSuccessors(node):
            if move[0] not in explored:
                explored.add(move[0])
                strategy.push(move)
    return None

from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.popleft()

    def empty(self):
        return len(self.queue) == 0


def breadthFirstGraphSearch(problem):
    return graphSearch(problem, Queue())
