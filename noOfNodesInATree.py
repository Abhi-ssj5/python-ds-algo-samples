from binaryTree import BinaryTree

"""     1
     /    \
    2      3
   / \      \
  4   5      6 """

def noOfNodes(root):
    if root is None:
        return 0
    
    return 1 + noOfNodes(root.left) + noOfNodes(root.right)

if __name__ == "__main__":
    array = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    rootNode = tree.buildTree(array)

    print(noOfNodes(rootNode))