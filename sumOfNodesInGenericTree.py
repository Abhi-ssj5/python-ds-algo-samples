class Node:
    def __init__(self):
        self.key = 0
        self.child = []
 
# Utility function to create a new tree node
def newNode(key):
    temp = Node()
    temp.key = key
    temp.child = []
    return temp
  
# Function to compute the sum
# of all elements in generic tree
def sumNodes(root):
    Sum = 0
  
    if root == None:
        return 0
  
    Sum += root.key

    for node in root.child:
        Sum += sumNodes(node)
    
    return Sum
 
if __name__ == "__main__":
    root = newNode(20)
    (root.child).append(newNode(2))
    (root.child).append(newNode(34))
    (root.child).append(newNode(50))
    (root.child).append(newNode(60))
    (root.child).append(newNode(70))
    (root.child[0].child).append(newNode(15))
    (root.child[0].child).append(newNode(20))
    (root.child[1].child).append(newNode(30))
    (root.child[2].child).append(newNode(40))
    (root.child[2].child).append(newNode(100))
    (root.child[2].child).append(newNode(20))
    (root.child[0].child[1].child).append(newNode(25))
    (root.child[0].child[1].child).append(newNode(50))
    print(sumNodes(root))