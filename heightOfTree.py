from binaryTree import BinaryTree

def heightOfTree(root):
    if root is None:
        return 0
    rootHeight = 1
    lstHeight = heightOfTree(root.left)
    rstHeight = heightOfTree(root.right)

    stHeight = lstHeight if lstHeight > rstHeight else rstHeight
    return rootHeight + stHeight

"""     1
     /    \
    2      3
   / \      \
  4   5      6 
       \
        9 """

if __name__ == "__main__":
    array = [1,2,4,-1,-1,5,-1,9,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    rootNode = tree.buildTree(array)

    print(heightOfTree(rootNode))
