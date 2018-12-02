import random

class node:
	ID = 1
	deadEnd = False
	active = True
	visited = False
	neighborID = [45,34]
	listIndex = 0
	failChance = random.random() * 100
	package = 0

	def getID():
		print(int(node.ID))

	def hasNeighbor():
		if(node.deadEnd == True):
			print("no")
			return False
		if(node.deadEnd == False):
			print("yes")
			return True

	def checkNeighbor():
		node.listIndex = len(node.neighborID)
		if(node.listIndex <= 1):
			node.deadEnd = True
		#for index in range(node.listIndex):
			#print(node.neighborID[index])

	def fail():
		num = random.random() * 100
		print(int(node.failChance))
		print(int(num))
		if(num <= node.failChance):
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



#print(node.neighborID.count(int))
#node.getID()
test = 6
node.setNeigborID(test)
node.checkNeighbor()
node.hasNeighbor()
node.fail()
#print(len(node.neighborID))
#print(random.randint(1, 100))