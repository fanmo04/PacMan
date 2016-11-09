class PacmanProblem1:
    # grid is a 2D array
    # pacman & ghost are tuples (r,a)
    def __init__(self, grid, pacman, ghost):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.pacman = pacman
        self.ghost = ghost

    # Since this problem requires us to output the path taken
    # to reach the ghost , we'll store the path in the state
    # state has this form:
    # tuple(tuple(r,a), [tuple(r1,a1), tuple(r2,a2), ...])
    # where the first tuple is the current position of pacman
    # and the list stores the path taken to reach here
    def getStartState(self):
        return (self.pacman, [self.pacman])

    def isGoalState(self, state):
        return state[0] == self.ghost

    def getSuccessors(self, state):
        moves = []
        path = state[1]

        def getMove(r, a):
            if self.grid[r][a] != '%':
                newPath = list(path)
                move = (r, a)
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