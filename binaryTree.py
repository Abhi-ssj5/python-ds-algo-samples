class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.index = -1

    def buildTree(self, array):
        self.index += 1

        if len(array) - 1 < self.index:
            return None
        elif array[self.index] == -1:
            return None
        
        newNode = Node(array[self.index])
        newNode.left = self.buildTree(array)
        newNode.right = self.buildTree(array)

        return newNode

"""     1
     /    \
    2      3
   / \      \
  4   5      6 """

if __name__ == "__main__":
    array = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    rootNode = tree.buildTree(array)

    print(rootNode.data)
