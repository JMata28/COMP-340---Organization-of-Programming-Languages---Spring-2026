class treeNode:
	def __init__(self,type,value,precedence):
		self.type = type
		self.value = value
		self.precedence = precedence
	parent = None
	lChild = None
	rChild = None
	
def getPrecedence(type):
	precedence = 0
	if type == "PLUS" or type == "MINUS":
		precedence = 1
	elif type == "MULTIPLICATION" or type == "DIVISION":
		precedence = 2
	return precedence

def createTreeNodeList(tokSeq):
	treeNodeList = []
	for token in tokSeq:
		newNode = treeNode(token.type, token.value, getPrecedence(token.type))
		treeNodeList.append(newNode)
	return treeNodeList
