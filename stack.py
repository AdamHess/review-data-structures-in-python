import node

class Stack:
	def __init__(self):
		self.__length = 0
		self.__tail = None
	def push(self, nextNode):
		if self.__tail != None:
			nextNode.setNext(self.__tail)
		self.__tail = nextNode; 
		self.__length += 1
	def pop(self): 
		currNode = self.__tail
		self.__tail = currNode.getNext()
		self.__length -= 1;
		return currNode
	def getLength(self):
		return self.__length


def testStack():
	a = node.Node(1)
	b = node.Node(2)
	c = node.Node(3)
	s = Stack()
	s.push(a)
	s.push(b)
	s.push(c)
	for i in range(s.getLength()):
		print("Stack Poped %s" % s.pop().getValue())


