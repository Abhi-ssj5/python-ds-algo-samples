from binaryTree import BinaryTree

def sumOfNodes(root, level) -> int:
    if root is None:
        return 0

    if level == 1:
        return root.data

    queue = list([root, None])
    k = 1
    sum = 0
    while len(queue) > 0:
        currentNode = queue.pop(0)

        if level == k and currentNode is not None:
            sum = sum + currentNode.data

        if currentNode is None:
            if len(queue) == 0:
                break
            else:
                queue.append(None)
                k += 1
                if k > level:
                    break
        else:
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
    
    return sum


"""    __9__
     /       \
    7         4
   / \       / \
  8   1     5   6 
     / \     
    2   8      """

if __name__ == "__main__":
    array = [9,7,8,-1,-1,1,2,-1,-1,8,-1,-1,4,5,-1,-1,6,-1,-1]
    tree = BinaryTree()
    rootNode = tree.buildTree(array)

    print(sumOfNodes(rootNode, 5))