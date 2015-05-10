from tree.BinaryTreeNode import TreeNode
from random import shuffle
from tree.BinaryTreeTraverse import preOrderTraverse

## create a binary sorted tree [No repeat]
def createBinarySortedTree(nodes):
    if len(nodes) == 0:
        return None
    root = TreeNode(nodes[0])
    root.left, root.right = None,None
    i = 1
    while i < len(nodes):
            # find the position to insert the element
        p, pre = root, root
        while p is not None and p.val != nodes[i]:
            pre = p
            if p.val < nodes[i]:
                p = p.right
            else:
                p = p.left
        if p is None: # it means a proper position found
            if pre.val > nodes[i]:
                pre.left = TreeNode(nodes[i])
            else:
                pre.right = TreeNode(nodes[i])
        i += 1
    return root


# if value in tree return True
# else return False
def hasValue(root,val):
    if root is None:
        return False
    while root is not None and root.val != val:
        if root.val >val:
            root = root.left
        else:
            root = root.right
    if root is None:
        return False
    return True
# first check whether the value in tree
# if not , insert the node as a leaf
def insertValue(root,val):
    if root is None:
        root = TreeNode(val)
        root.left,root.right = None,None
        return root
    p,pre = root, root
    while p is not None and p.val != val:
        pre = p
        if p.val> val:
            p = p.left
        else:
            p = p.right
    if p is None:
        if pre.val > val:
            pre.left = TreeNode(val)
            pre.left.left,pre.left.right=None,None
        else:
            pre.right = TreeNode(val)
            pre.right.left,pre.right.right = None,None
    return root
def deleteValue(root,val):
    if root is None:
        return None
    p,pre = root,root
    while p is not None and p.val != val:
        pre = p
        if p.val > val:
            p = p.left
        else:
            p = p.right
    if p is not None:
        if p.right is None:
            if p.left is None:
                if p == pre.left:
                    pre.left = None
                elif p == pre.right:
                    pre.right = None
            else:
                if p == pre.left:
                    pre.left = p.left
                elif p == pre.right:
                    pre.rigth = p.left
        else:
            if p.left is None:
                if p == pre.left:
                    pre.left = p.right
                elif p == pre.right:
                    pre.right = p.right
            else:
                pr,q = p.right,p.right
                while q.left is not None:
                    pr = q
                    q = q.left
                if pr == p.right:
                    p.val = pr.val
                    p.right = pr.right
                else:
                    p.val = q.val
                    pr.left = q.right
    #return root
                    
                    
                    
                
    
    







