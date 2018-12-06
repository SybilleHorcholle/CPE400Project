"""
Names: Sybille Horcholle, Nicholas Mason, Nicholas Thom
Subject: CPE400 
Project: Topic 4: Dynamic routing mechanism design in faulty network
Description: This project will utilize a percent chance of failure, along with implementing a shortest path algorithm, to find the best path from a start node to an end node.  In addition, the program will utilizes a dead end flag to show which nodes have only one neightbor, a fail flag, which determines if a node has failed, and a failure probability, which assists in the program creating the shortest path. 
"""
import numpy as np
from matplotlib import pyplot #used to plot
import random
"""
Class Name: node
Parameters: self, id_num, deadEnd, active, visited, neighbors, failChance
Functionality: This class creates a node for the mesh network. It has various member functions.
    Member Functions: 
        getID(self): Returns the ID of the given node.
        getStatus(self): Returns the status of the given node, such as active.
        setStatus(self, status): This function will set the status of the node.
        hasNeighbor(): Checks to see if a given node is a dead end node, meaning that it has only one neighbor.
        checkNeighbor(): Checks to see if the node only has one neighbor, or less than one neighbor.  If it does, then it is a dead end node.
                         Otherwise, the dead end variable stays false, so it is still available.
        fail(): Determines if a given node has failed.  It takes in a percent chance of failure, and generates a random number.
                If that random number is less than or equal to the percent chance of failure, that means the node has failed.  
Exceptions: NONE

Important Notes: 
    Class to make node in a network 
    id = number of individual node
    Neighbors = dictionary of neighboring nodes
    failProb = probabilty of the node failing
    failFlag = boolean flag to determine if node has failed
    deadendFlag = boolean flag to determine if node has no further neighbors
    random.random() * 100
"""
   
class node:
    def __init__(self, id_num, deadEnd=False, active=True, neighbors={}, failChance=.5):
        self.ID = id_num
        self.deadEnd = deadEnd
        self.active = active
        self.neighborID = [neighbors]
        self.failChance = failChance

    def getID(self):
        return int(self.ID)

    def getStatus(self):
        return bool(self.active)

    def setStatus(self,status):
        self.active = status
    
    def getFailChance(self):
        return int(self.failChance)

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

    def fail():
        num = random.random() * 100
        print(int(node.failChance))
        print(int(num))
        if (num <= node.failChance):
            node.active = False
            print("Fail")
        else:
            print("Active")

   
"""
Function Name: minDistance
Parameters: distances, path
Functionality: This function will allow the program to find the minimum distance between two given nodes.
Exceptions:NONE

Important Notes: 
    Used in finding the shortest path from a start node to an end node.
"""
def minDistance(distances, path):
    min = np.inf
    min_index = 0
    for i in range(num_nodes):
        if path[i] == False and distances[i] < min:
            min = distances[i]
            min_index = i
    return min_index
"""
Function Name: shortestPath
Parameters: start_node, dest_node, edge_matrix
Functionality: This function is used to find the shortest path between two nodes.  
                    It will use the percent chance of failure and the minDistance function to find the most efficient path in a mesh network.
Exceptions:NONE

Important Notes: 
    Considers the probabilty of the node failing to find the best path.
    Function to find the shortest path between two given nodes. 
"""
def shortestPath(start_node, dest_node, edge_matrix):
    print("srcnode: ",start_node," destnode: ",dest_node)
    visited = []
    distances = [np.inf] * num_nodes #holds the shortest distances from start_node to dest_node
    path = [False] * num_nodes  #holds nodes that are part of shortest path
    distances[start_node] = 0 # set distance from source node as 0
    current_node = start_node

    while current_node != dest_node:
        
        min_node = minDistance(distances, path)
        current_node = min_node
        path[min_node] = True
        for j in range(num_nodes):
            if edge_matrix[min_node][j] > 0 and path[j] == False and distances[j] > distances[min_node] + edge_matrix[min_node][j]:
                distances[j] = distances[min_node] + edge_matrix[min_node][j]
                visited.append(j)
    
    print('visited: ',visited)
    return distances
"""
Function Name: checkPaths
Parameters: edge_matrix, node_list
Functionality: This function checks to see if the node is active or if it has failed.
Exceptions:NONE

Important Notes: 
    This function is important in finding the most efficient path possible between two nodes.
"""
def checkPaths(edge_matrix,node_list):
    for i in range(len(edge_matrix[0])):
            if node_list[i].getStatus() == False: #check if node is not active
                for j in range(len(edge_matrix[1])):
                    edge_matrix[i][j] = np.inf
                    edge_matrix[j][i] = np.inf # remove distance for failed node in edge matrix
    return edge_matrix
# ------------ MAIN PROGRAM -----------

# matrix containing the distances to each node
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
    
    temp_node = node(new_node[0],False,True,new_node[1],new_node[2])
    node_list.append(temp_node)
    print("printing id: ",temp_node.getID())
    print(new_node)
    new_node.clear()
    offset += 3

node_file.close()

# Get input node from user
check = False
while check == False:
    sourceNode = int(input('Enter the source node ID: '))
    srcCheck = False
    for i in range(len(node_list)):
        if node_list[i].getID() == sourceNode:
            srcCheck = True
            check = True
    if srcCheck == False:
        print("Invalid source node ID \n")

# Get dest node from user
check = False
while check == False:
    destNode = int(input('Enter the destination node ID: '))
    srcCheck = False
    for i in range(len(node_list)):
        if node_list[i].getID() == sourceNode:
            srcCheck = True
            check = True
    if srcCheck == False:
        print("Invalid destination node ID \n")

num_nodes = len(node_list)

# Randomly deactive nodes
failNum = random.random() * 100

updated_matrix = [[]]
updated_matrix = checkPaths(edge_matrix,node_list)
print(updated_matrix)

print("distances: ",shortestPath(node_list[sourceNode-1].getID()-1,node_list[destNode-1].getID()-1,edge_matrix))

# ------------ END OF MAIN PROGRAM -------------------------------------------------------------------------------------------------------------------------------------------------
