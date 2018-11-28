import numpy as np
from matplotlib import pyplot #used to plot

class networkNode (object):
    # Class to make node in a network 
    # id = number of individual node
    # Neighbors = dictionary of neighboring nodes
    # failProb = probabilty of the node failing
    # failFlag = boolean flag to determine if node has failed
    # deadendFlag = boolean flag to determine if node has no further neighbors

    def __init__(self, id, failProb = 0.5, failFlag = False, deadendFlag = False):
        self.neighbors = id
        self.neighbors = {}
        self.failProb = failProb
        self.failFlag = failFlag
        self.deadendFlag = deadendFlag
    
    def addNeighbor(self, neighborNode):
        self.neighbors[neighborNode]