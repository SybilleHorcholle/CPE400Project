# CPE400Project
# Names: Nick Mason, Nick Thom, Sybille Horcholle
# Project(4): Dynamic routing mechanism design in faulty networks. 
# The project will include the creation of a mesh network with nodes and links.  Nodes and links can fail during the process of communication within the network.  The code will handle node and link failure, with early detection, in order to avoid future node and link failure as a result of the first faulty link between nodes.  

Novel ideas:
	- Scenario when a node connecting to other nodes goes down and loses the link between the two groups; reroute to reconnect the two groups again
	- Label 'dead end' nodes to avoid trying to find a path through them
	- Use Dijkstra's algorithm to find the shortest path to a node

Error Handling:
	- Check probability of failing, avoid nodes that fail more often than others. 
		○ Show graph to compare the error handling with just going through nodes that have crashed

Node Class:
	- Neighbors
	- Probability of it failing: random number generator if within number range then failed
	- Flag for dead end
	- Flag if node is failed 
	
Other Parameters:
	- Timer to set failed nodes

Roles:
	- Nick M: Start writing up technical report
	- Nick T: Create class for Nodes
	- Sybille: Create function for Dijkstra's shortest path
