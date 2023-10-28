from binaryTree import BinaryTree

# DFS (Depth first search)

def preOrderTraverse(root):

    if root is None:
        return
    
    print(root.data)

    preOrderTraverse(root.left)
    preOrderTraverse(root.right)

def inOrderTraversal(root):
    if root is None:
        return
    
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)

def postOrderTraversal(root):
    if root is None:
        return
    
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)

# BFS (Bredth first search)

def levelOrderTraversal(root):
    if root is None:
        return

    queue = list([root, None])

    while len(queue) > 0:
        currentNode = queue.pop(0)

        if currentNode is None:
            print("")
            if len(queue) == 0:
                break
            else:
                queue.append(None)
        else:
            print(currentNode.data, end=" ")
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

"""     1
     /    \
    2      3
   / \      \
  4   5      6 """

if __name__ == "__main__":
    array = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    rootNode = tree.buildTree(array)

    print("DFS")
    print("Pre Order Traversal")
    preOrderTraverse(rootNode)

    print("In Order Traversal")
    inOrderTraversal(rootNode)

    print("Post Order Traversal")
    postOrderTraversal(rootNode)

    print("BFS")
    print("Level Order Taversal")
    levelOrderTraversal(rootNode)