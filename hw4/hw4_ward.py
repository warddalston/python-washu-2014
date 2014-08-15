
###########
# Dalston Ward
# August 14
############

class LinkedList():
	def __init__(self, value): #complexity class 1.  
		self.head = Node(_value = value, _next = None)
		self.length = 1
		#self.tail = Node(_value = value, _next = 1)
	
	def addNode(self, new_value): #complexity class n. Has to check each element of the list to see if its the end.
		self.length += 1
		self.head.NaddNode(new_value)
		
	def addNodeAfter(self, new_value, after_node): #also complexity class N. Has to check until its at the right node, and then reassign all nodes afterwards.  
		self.head.NaddNodeAfter(new_value, after_node, length = self.length)
		self.length += 1
	
	def addNodeBefore(self, new_value, before_node): #same complexity as addNodeBefore
		self.addNodeAfter(new_value, before_node - 1) #because adding a node before is equivalent to adding a node after the node right before the given node
	
	def removeNode(self, node_to_remove): #complexity is n.  Has to check which node to remove, and once that node is found, update all subsequent nodes once. 
		self.head.NremoveNode(node_to_remove = node_to_remove, length = self.length)
		self.length -= 1
	
	def removeNodesByValue(self, value): #complexity class is n^2 (maybe nlogn).  Could have to check every node, see it needs removed, update the rest of the list, and then do it again.  
		self.length -= self.head.NremoveNodesByValue(value)
		
	def reverse(self): #also complexity higher than n.  I think n^2.  It has to add nodes equal to length (n-1) and then also remove nodes equal to length (n-1).  
		self.head.Nreverse(length = self.length, lengthCount = self.length)
	
	def __str__(self): #complexity class n.  Simply print each element once.  
		return self.head.Nprint()
		
#Could complexity be lower?  Probably, but I don't see a way.  With this structure one has to go through the whole list up to the desired node to access a node.    
		
class Node():
	def __init__(self, _value = None, _next = None):
		self.value = _value
		self.next = _next
	def __str__(self):
		return str(self.value)
		
	def NaddNode(self, new_value): #NaddNode for the node method 
		if self.next == None:
			self.next = Node(_value = new_value)
		else:
			self.next.NaddNode(new_value)
			
	def NaddNodeAfter(self, new_value, after_node, length, nodeCount = 0):
		if after_node == length:
			self.NaddNode(new_value)
		else:
			if nodeCount == after_node: #are we at the node we want?  Starts at the head, and then increases each time.  --> When it triggers, we're at the "next" element of the element after which we want to insert.   
				self.next = Node(_value = self.value, _next = self.next) #once we are where we want, it sticks the current node into the next attribute of the new node
				self.value = new_value #puts the new value into the new node
			else: 
				nodeCount +=  1
				self.next.NaddNodeAfter(new_value, after_node, length, nodeCount = nodeCount) #the recursive bit gets us into the node we are looking for.  
	
	def NremoveNode(self, node_to_remove, length, nodeCount = 1): #start with node count one
		if node_to_remove == length:
			if self.next.next == None:
				self.next = None
			else:
				self.next.NremoveNode(node_to_remove, length, nodeCount = 1)
		else: 
			if nodeCount == node_to_remove: #is the current node the one to remove?
				self.value = self.next.value #assign the next value to the current value then.
				self.next = self.next.next #and make all subsequent nodes the next node for this one. 
			else: 
				nodeCount +=  1 #if not the right one, adjust nodeCount and move on. 
				self.next.NremoveNode(node_to_remove, length, nodeCount)
		
	#can't handle linked lists where the value to remove is the last two values.  
	def NremoveNodesByValue(self, value, nodesRemoved = 0):
		if self.next.value == value and self.next.next == None: #if the last element needs to be removed, do this stuff 
			self.next = None
			nodesRemoved += 1 
		if self.value == value: 
			self.value = self.next.value
			self.next = self.next.next
			nodesRemoved += 1 #for keeping track of the length of the list 
			if self.next == None: 
				return nodesRemoved 
			return self.NremoveNodesByValue(value, nodesRemoved)
		else:
			if self.next == None: #so that we eventually get out of this function!
				return nodesRemoved #so that we can update length!
			return self.next.NremoveNodesByValue(value, nodesRemoved)
		
	#my reverse function takes the first element, places it after the last, and then removes the first.  It then repeats this process until the last element is first.  Heres how it works:
	# 1 - 2 - 3
	# 1 - 2 - 3 - 1
	# 2 - 3 - 1
	# 2 - 3 - 2 - 1
	# 3 - 2 - 1
	def Nreverse(self, length, lengthCount):
		while(lengthCount > 1):	
			self.NaddNodeAfter(new_value = self.value, after_node = lengthCount, length = length)
			self.NremoveNode(node_to_remove = 1, length = length)
			lengthCount -=1
	
	#works similar to addNode.  Creates a string object, adds the current node's value to it, and then goes to the next one.  Stops when it reaches a node with no next.  
	def Nprint(self, output = ""): 
		if self.next == None:
			return output + str(self.value)
		else:
			output = output + str(self.value) +", "
			return self.next.Nprint(output)
	
	
######## example of this in action!!!!!!! ##########	
	
	
x = LinkedList(4)
x.addNode(5)
print x
x.addNode(4)
x.addNode(7)
x.addNode(5)
x.addNode(4)
x.addNode(10)

print "How long is it?"
print x
print str(x.length) + " = length!"

print x
x.reverse()
print "backward"
print x
# x.addNode(4)
print "Remove 4!"
x.removeNodesByValue(4)
print x

print "add 66 after the 3rd node"
x.addNodeAfter(66,3)
print x

print "add 46 before the 2nd node"
x.addNodeBefore(46,2)
print x

print "remove 46"
x.removeNode(2)
print x

print "backwards again"
x.reverse()
print x
