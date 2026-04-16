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

def parsing(treeNodeList):
	dummyNode = treeNode("DUMMY","",0)
	treeNodeList.insert(0,dummyNode)
	treeNodeList.append(dummyNode) 
	for index in range(len(treeNodeList)):
		node = treeNodeList[index]
		if node.type == "NUMBER":
			lOp = treeNodeList[index-1]
			rOp = treeNodeList[index+1]
			if rOp.precedence > lOp.precedence:
				#Right
				rOp.lChild = node
				node.parent = rOp
				if lOp.type != "DUMMY":
					lOp.rChild = rOp
					rOp.parent = lOp
			else:
				#Left
				lOp.rChild = node
				node.parent = lOp
				if rOp.type != "DUMMY":
					while lOp.parent != None:
						if lOp.parent.precedence < rOp.precedence:
							break
						lOp = lOp.parent
					
					if lOp.parent != None:
						lOp.parent.rChild = rOp
						rOp.parent = lOp.parent
					rOp.lChild = lOp
					lOp.parent = rOp 

def findRoot(treeNodeList):
	rootNode = None
	for node in treeNodeList:
		if node.parent == None and node.type != "DUMMY":
			rootNode = node
			break
	return rootNode


def parse(tokSeq):
	rootNode = None
	treeNodeList = createTreeNodeList(tokSeq)
	parsing(treeNodeList)
	rootNode = findRoot(treeNodeList)

	return rootNode

#printTree is a helper function to help you check if your tree was made correctly
def printTree(rootNode):
	if rootNode.lChild == None and rootNode.rChild == None:
		#operand
		print(rootNode.value, end="")
	else:
		#operator
		print("(", end="")
		printTree(rootNode.lChild)
		print(rootNode.value, end="")
		printTree(rootNode.rChild)
		print(")", end="")		
		
