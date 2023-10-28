from binaryTree import BinaryTree
from binaryTree import Node

"""     1
     /    \
    2      3
   / \      \
  4   5      6 """

def sumOfNodes(root):
    if root is None:
        return 0
    
    return root.data + sumOfNodes(root.left) + sumOfNodes(root.right)

if __name__ == "__main__":
    array = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    rootNode = tree.buildTree(array)

    print(sumOfNodes(rootNode))