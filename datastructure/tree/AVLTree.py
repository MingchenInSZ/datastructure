from tree.BinaryTreeNode import AVLTreeNode
from tree.BinaryTreeTraverse import preOrderTraverse



#auxiliary function for AVL tree
def getHeight(root):
    if root is None:
        return -1
    return root.height

#single left rotation
def singleLeftRotate(root):
    left = root.left
    root.left = left.right
    left.right = root
    root.height = max(root.left,root.right) + 1
    left.height = max(left.left,root.height) + 1
#single right rotation    
def singleRightRotate(root):
    right = root.right
    root.right = right.left
    right.left = root
    root.height = max(root.left,root.right) +1
    right.height = max(right.right,root.height) + 1
#double Left right    
def doubleRotateLeftRight(root):
    singleRightRotate(root.left)
    singleLeftRotate(root)
#double right left
def doubleRotateRightLeft(root):
    singleLeftRotate(root.right)
    singleRightRotate(root)
    
def insertValue(root,val):
    if root is None:
        root = AVLTreeNode(val)
        root.left,root.right = None,None
        return
    if val < root.val:
        insertValue(root.left, val)
        if abs(getHeight(root.left)-getHeight(root.right))>1:
            if val < root.left.data:
                singleLeftRotate(root)
            else:
                doubleRotateLeftRight(root)
    elif val > root.val:
        insertValue(root.right, val)
        if abs(getHeight(root.left)-getHeight(root.right))>1:
            if val> root.right.val:
                singleRightRotate(root)
            else:
                doubleRotateRightLeft(root)
    root.height = max(getHeight(root.left),getHeight(root.right))
def insert(root,val):
    insertValue(root,val)
def createAVLTree(nums):
    if len(nums) == 0:
        return None
    root = None
    for val in nums:
        insert(root, val)
    return root

        
    
    
