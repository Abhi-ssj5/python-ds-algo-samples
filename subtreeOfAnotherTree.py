from binaryTree import BinaryTree

def isEqual(root, subRoot) -> bool:
    if root is None and subRoot is None:
        return True

    if root is None or subRoot is None:
        return False

    if root.data == subRoot.data:
        return isEqual(root.left, subRoot.left) and isEqual(root.right, subRoot.right)
    else:
        return False


def isSubtree(root, subRoot) -> bool:
    if subRoot is None:
        return True

    if root is None:
        return False
    
    if root.data == subRoot.data:
        if isEqual(root, subRoot):
            return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


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

    subTreeArray = [1,2,-1,-1,9,-1,-1]
    subTree = BinaryTree()
    subTreeRoot = subTree.buildTree(subTreeArray)

    print(isSubtree(rootNode, subTreeRoot))