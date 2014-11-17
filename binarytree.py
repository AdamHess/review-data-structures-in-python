class BinaryTreeNode: 
	def __init__(self, value = None):
		self.__right = None
		self.__left =  None
		self.__value = value
	def getLeft(self):
		return self.__left
	def setLeft(self, leftNode):
		self.__left = leftNode
	def getRight(self): 
		return self.__right
	def setRight(self, rightNode):
		self.__right = rightNode
	def getValue(self):
		return self.__value
	def  setValue(self, val) :
		self.__value = val


def insertNode(aNode, aNewValue):	
	if aNode.getValue() > aNewValue:
		if aNode.getLeft() == None:
			abst_node = BinaryTreeNode(aNewValue)
			aNode.setLeft(abst_node)
		else:
			insertNode(aNode.getLeft(), aNewValue)
	else :
		if aNode.getRight() == None:
			abst_node = BinaryTreeNode(aNewValue)
			aNode.setRight(abst_node)
		else:
			insertNode(aNode.getRight(), aNewValue)	

def inOrderTraversal(aNode):
	if aNode == None:
		return
	inOrderTraversal(aNode.getLeft())
	print("in-order tree traversal: %s" % aNode.getValue())
	inOrderTraversal(aNode.getRight())


def testingBinaryTree() :
	abt_node = BinaryTreeNode(value = 50)
	insertNode(abt_node, 10)
	insertNode(abt_node, 40)
	insertNode(abt_node, 3)
	insertNode(abt_node, 100)
	insertNode(abt_node, 51)
	insertNode(abt_node, 103)
	insertNode(abt_node, 44)
	insertNode(abt_node, 323)
	insertNode(abt_node, 500)
	insertNode(abt_node, 1)
	inOrderTraversal(abt_node)




