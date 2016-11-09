import numpy as np
import Queue


def BFS(walls, start, end):
    start = [start[0], start[1]]
    end = [end[0], end[1]]
    if start == end:
        return [start]
    neighbours = Queue()  # queue storing the next positions to explore
    neighbours.enqueue(start)
    counts = np.zeros((walls.width, walls.height), dtype=int)
    predecessors = np.zeros((counts.shape[0], counts.shape[1], 2), dtype=int)
    counts[start[0], start[1]] = 1
    # loop until the end position is found
    while not neighbours.isEmpty():
        n = neighbours.dequeue()
        print n
        if n == end:
            print "path found!", n, counts[n[0]][n[1]]
            break  # path is found
        # need to add all the valid neighbours to the list and remember from where they came from
        for neighbour in [[n[0] - 1, n[1]], [n[0] + 1, n[1]], [n[0], n[1] - 1], [n[0], n[1] + 1]]:
            if not walls[neighbour[0]][neighbour[1]] and counts[neighbour[0], neighbour[1]] == 0:
                neighbours.enqueue(neighbour)
                predecessors[neighbour[0], neighbour[1]] = n
                counts[neighbour[0], neighbour[1]] = counts[n[0], n[1]] + 1
    print 'here 0'
    if counts[end[0], end[1]] == 0:
        return []  # path is not found
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


from pacman import Directions
from pacman import GhostRules
from pacman import GameState
from game import Agent
import random, util

from game import AgentState
from pacman import Actions
from game import Grid
from layout import Layout
import  time




class ThePacmanAgent(Agent):
    def getActions(self, state, GhostRules,PriorityQueueWithFunction, legalActions):
        legal = state.getLegalPacmanActions()
#running from ghost
        g1r, g1c = state.getGhostPosition(1)
        g2r, g2c = state.getGhostPosition(2)
        pr, pc = state.getPacmanPosition(0)

        if (pr -1 == g1r and pc == g1c)or(pr +1 == g1r and pc == g1c):
            possibleActions = Directions.WEST or Directions.EAST or Directions.NORTH
            if possibleActions in state.getLegalPacmanActions():
                return random.choice(possibleActions)
            else:
                return Directions.STOP
            #not south
            #North, West or East #legal

            pr == g1r and pc -1 == g1c \
            pr == g1r and pc +1 == g1c \
            pr -1 == g2r and pc == g2c \
            pr +1 == g2r and pc == g2c \
            pr == g2r and pc -1 == g2c \
            pr == g2r and pc +1 == g2c:

            return random.choice(legal)

        elif len(state.getCapsules) == 0:
            # call the greedy agent to complete the game maze

            legal = state.getLegalPacmanActions()
            if Directions.STOP in legal: legal.remove(Directions.STOP)

            successors = [(state.generateSuccessor(0, action), action) for action in legal]
            scored = [(scoreEvaluation(state), action) for state, action in successors]
            bestScore = max(scored)[0]
            bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
            return random.choice(Agent)
            # StopIteration #Direction.STOP

        else:
    #find the shortest path to capsules
        start = state.getPacmanPosition()
        all_paths = []
            for capsule in state.getCapsules():

                capsule_path = BFS(state.walls, start, capsule)# layout or GameState or Grid to get the walls etc. in the layout?
                all_paths.append(capsule_path)
                min = len(all_paths[0])
                for capsule_path in all_paths:
                    if len(all_paths[capsule_path]) < len(all_paths[0]):
                        min = len(all_paths[capsule_path])
                    return all_paths[capsule_path]
            #return getclosestcapsule
            #deduct the capsule eaten position capsule from the list GameState.getCapsules(self).remove(capsuleEaten)

#not sure about tabs/ indentations- as to whether they are correct or not...?
            isScared = GhostRules.ghostState.scaredTimer > 0
            while isScared: #count/ time how long ghost is scared
                g1r, g1c = state.getGhostPosition(1)
                g2r, g2c = state.getGhostPosition(2)
                pr, pc = state.getPacmanPosition(0)
                #same as you do for the capsules but for the ghosts by getting a list of ghost positions

            #break when time is over and ghost is no longer scared
            #OR- another method to chase the ghost?...below...



            if len(state.getCapsules) == 0:
                # call the greedy agent to complete the game maze

                    legal = state.getLegalPacmanActions()
                    if Directions.STOP in legal: legal.remove(Directions.STOP)

                    successors = [(state.generateSuccessor(0, action), action) for action in legal]
                    scored = [(scoreEvaluation(state), action) for state, action in successors]
                    bestScore = max(scored)[0]
                    bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
                    return random.choice(Agent)
                #StopIteration #Direction.STOP


            #return Directions.STOP for the pacman?


def scoreEvaluation(state):
    return state.getScore()