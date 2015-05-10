# recursive traverse the tree


# pre order
def preOrderTraverseRecursive(root,nums):
    if root is not None:
        nums.append(root.val)
        preOrderTraverseRecursive(root.left,nums)
        preOrderTraverseRecursive(root.right, nums)
        
# in order
def inOrderRecursiveTraverse(self,root,nums):
    if root is not None:
        inOrderRecursiveTraverse(root.left,nums)
        nums.append(root.val)
        inOrderRecursiveTraverse(root.right, nums)

# post order            
def postOrderRecursiveTraverse(self,root,nums):
    if root is not None:
        postOrderRecursiveTraverse(root.left,nums)            
        postOrderRecursiveTraverse(root.right, nums)
        nums.append(root.val)


# None recursive traverse the tree
#  the only difference of  pre order and in orde is 
#  that the visit order is previous push node or pop node  
def preOrderTraverse(root):
    stack, vals = [], []
    if root is None:
        return None
    while root is not None or len(stack)!=0:
        while root is not None:
            vals.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right
    return vals
#in order        
def inOrderTraverse(root):
    stack, vals = [], []
    if root is None:
        return None
    while root is not None or len(stack) != 0:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        vals.append(root.val)
        root = root.right
    return vals
#post order
#in post order, we need an auxiliary data to indicate the 
# whether the node is the first time to visit 
def postOrderTraverse(root):
    stack,ind, vals = [], [],[]        
    if root is None:
        return None
    while root is not None or len(stack) != 0:
        while root is not None:
            stack.append(root)
            ind.append(0)
            root = root.left
        if ind[-1] == 0:
            root = stack[-1]
            ind[-1] = 1
            root = root.right
        else:
            root = stack.pop()
            vals.append(root.val)
            ind.pop()
            root = None # left traversed, then go to right directly
    return vals
# traverse the tree in lever order
def levelOrderTraverse(root):
    if root is None:
        return []
    stack,nums = [root],[]
    nums.append([root.val])
    while len(stack)!=0:
        st,ins = [],[]
        for node in stack:
            if node.left is not None:
                st.append(node.left)
                ins.append(node.left.val)
            if node.right is not None:
                st.append(node.right)
                ins.append(node.right.val)
        nums.append(ins)
        stack = st
    nums.pop()
    return nums
# deep first traverse the tree
def deepFirstTraverse(root):
    if root is None:
        return None
    stack,nums = [root],[]
    while len(stack)!= 0:
        node = stack.pop()
        nums.append(node.val)
        if node.left is not None:
            stack.apppend(node.left)
        if node.right is not None:
            stack.append(node.right)
    return nums
    