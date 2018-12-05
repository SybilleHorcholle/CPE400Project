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
        return int(self.ID)

    def getStatus(self):
        return bool(self.active)

    def setStatus(self,status):
        self.active = status
    
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

    

   

# function to find the shortest path between two given nodes
# considers the probability of the node failing to find best path


def minDistance(distances, path):
    min = np.inf
    min_index = 0
    for i in range(num_nodes):
        if path[i] == False and distances[i] < min:
            min = distances[i]
            min_index = i
    return min_index

def shortestPath(start_node, dest_node, edge_matrix):
    distances = [np.inf] * num_nodes #holds the shortest distances from start_node to dest_node
    path = [False] * num_nodes  #holds nodes that are part of shortest path
    distances[start_node] = 0 # set distance from source node as 0
    
    for i in range(num_nodes):
        min_node = minDistance(distances, path)
        path[min_node] = True
        for j in range(num_nodes):
            if edge_matrix[min_node][j] > 0 and path[j] == False and distances[j] > distances[min_node] + edge_matrix[min_node][j]:
                distances[j] = distances[min_node] + edge_matrix[min_node][j]
    return distances

def checkPaths(edge_matrix,node_list):
    for i in range(len(edge_matrix[0])):
            if node_list[i].getStatus() == False: #check if node is not active
                for j in range(len(edge_matrix[1])):
                    edge_matrix[i][j] = np.inf
    return edge_matrix
# ------------ MAIN PROGRAM -----------

edge_matrix = [[0,4,np.inf,np.inf,np.inf,np.inf,np.inf],[4,0,8,np.inf,np.inf,11,np.inf],[np.inf,8,0,7,np.inf,np.inf,np.inf],[np.inf,np.inf,7,0,2,9,np.inf],[np.inf,np.inf,np.inf,2,0,np.inf,np.inf],[np.inf,11,np.inf,9,np.inf,0,6],[np.inf,np.inf,np.inf,np.inf,np.inf,6,0]]

node_file = open('nodes.txt', 'r') #open network data file
lines = node_file.readlines()
node_list = []
new_node = []
offset = 0

global num_nodes 

while offset < len(lines):
    for j in range(3):
        clean_line = lines[j+offset].rstrip() #remove new line character from string
        string = clean_line.split(':')
        new_node.append(string[1])
    
    temp_node = node(new_node[0],False,True,False,new_node[1],new_node[2])
    node_list.append(temp_node)
    print("printing id: ",temp_node.getID())
    print(new_node)
    new_node.clear()
    offset += 3

node_file.close()

num_nodes = len(node_list)
#-------need to implement failed node algorithm-------
node_list[0].setStatus(False)

print(checkPaths(edge_matrix,node_list))
#dijkstraPath(node_list[0].getID()-1,node_list[4].getID()-1,edge_matrix)

