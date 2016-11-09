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

import game

legal = state.getLegalPacmanActions()
#running from ghost
        g1r, g1c = state.getGhostPosition(1)
        g2r, g2c = state.getGhostPosition(2)
        pr, pc = state.getPacmanPosition(0)

        possibleActions = state.getLegalPacmanActions()
        if g1r, g1c in state.getLegalPacmanActions():









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