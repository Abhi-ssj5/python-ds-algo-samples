from heightOfTree import heightOfTree
from binaryTree import BinaryTree

class TreeInfo:

    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter

def diameterOfTree2(root) -> TreeInfo:
    if root is None:
        return TreeInfo(0, 0)

    left = diameterOfTree2(root.left)
    right = diameterOfTree2(root.right)

    height = max(left.height, right.height) + 1

    diameter1 = left.diameter
    diameter2 = right.diameter
    diameter3 = left.height + right.height + 1

    maxDiameter = max(diameter3, max(diameter1, diameter2))

    return TreeInfo(height, maxDiameter)


def diameterOfTree(root):
    if root is None:
        return 0
    
    diameter1 = diameterOfTree(root.left)
    diameter2 = diameterOfTree(root.right)
    diameter3 = heightOfTree(root.left) + heightOfTree(root.right) + 1

    return max(diameter3, max(diameter1, diameter2))


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

    print(diameterOfTree2(rootNode).diameter)

    