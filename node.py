class Node:
	def __init__(self, value =  None):
		self.__next = None
		self.__value = value
	def setNext(self, nextNode):
		self.__next = nextNode
	def getNext(self):
		return self.__next
	def getValue(self):
		return self.__value
	def setValue(self, value): 
		self.__value = value




def testLinkedList():
	a = Node()
	b = Node()
	c = Node()


	a.setValue(1)
	a.setNext(b)
	b.setValue(2)
	b.setNext(c)
	c.setValue(3)

	aNode = a

	while aNode != None:
		print(aNode.getValue())
		aNode = aNode.getNext()

