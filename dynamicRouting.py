import numpy as np
from matplotlib import pyplot #used to plot
import random

    # Class to make node in a network 
    # id = number of individual node
    # Neighbors = dictionary of neighboring nodes
    # failProb = probabilty of the node failing
    # failFlag = boolean flag to determine if node has failed
    # deadendFlag = boolean flag to determine if node has no further neighbors
#random.random() * 100

class node:
    def __init__(self, id_num, deadEnd=False, active=True, visited=False, neighbors={}, failChance=.5):
        self.ID = id_num
        self.deadEnd = deadEnd
        self.active = active
        self.visited = visited
        self.neighborID = [neighbors]
        self.failChance = failChance
	    #package = 0

    def getID(self):
        return self.ID

    def hasNeighbor():
        if(node.deadEnd == True):
            print("no")
        return False
        if(node.deadEnd == False):
            print("yes")
        return True

    def checkNeighbor():
        listIndex = len(node.neighborID)
        if (listIndex <= 1):
            node.deadEnd = True
		    #for index in range(node.listIndex):
			    #print(node.neighborID[index])

    def fail():
        num = random.random() * 100
        print(int(node.failChance))
        print(int(num))
        if (num <= node.failChance):
            node.active = False
            print("Fail")
        else:
            print("Active")

    def setVisit():
        node.visited = True

    def checkVisit():
        return node.visited

    def setNeigborID(test):
        node.neighborID.append(test)


node_file = open('nodes.txt', 'r')
lines = node_file.readlines()
#print(lines[0])
node_list = []
new_node = []
for i in range(3):
    clean_line = lines[i].rstrip()
    string = clean_line.split(':')
    #print(string[1])
    new_node.append(string[1])

print(new_node)
temp_node = node(new_node[0],False,True,False,new_node[1],new_node[2])
print("printing id: ",temp_node.getID())
#node_list.append(temp_node)
#print(node_list)
node_file.close()

#for i in range(6):
   # nodes = node(i,{ )

#print(node.neighborID.count(int))
#node.getID()
       
#print(len(node.neighborID))
#print(random.randint(1, 100))
