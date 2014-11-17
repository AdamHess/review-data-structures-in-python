import node

class Queue:
	def __init__(self):
		self.__length = 0
		self.__tail = None
		self.__head = None 
	def push(self, nextNode):
		if self.__length > 0:
			self.__tail.setNext(nextNode)
		else :
			self.__head = self.__tail = nextNode
		self.__tail = nextNode; 
		self.__length += 1
	def pop(self): 
		currNode = self.__head
		self.__head = currNode.getNext()
		self.__length -= 1;
		return currNode
	def getLength(self):
		return self.__length


def testQueue():
	a = node.Node(1)
	b = node.Node(2)
	c = node.Node(3)
	q = Queue()
	q.push(a)
	q.push(b)
	q.push(c)
	for i in range(q.getLength()):
		print("Queue Popped %s" % q.pop().getValue())


