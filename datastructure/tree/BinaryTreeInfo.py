from Queue import Queue as queue
# depict the information of the tree

# get the tree depth 
def depthOfTree(root):
    stack,ind,depth =[], [],0
    while root is not None or len(stack) != 0:
        while root is not None:
            stack.append(root)
            ind.append(0)
            root = root.left
        if ind[-1] == 0:
            ind[-1] = 1;
            root = stack[-1].right
        else:
            if len(stack) > depth:
                depth = len(stack)
            stack.pop()
            ind.pop()
            root = None
    return depth
# get the breadth
def breadthOfTree(root):
    if root is None:
        return 0        
    p, bdh= queue(),0
    p.put(root)
    while not p.empty():
        if bdh<p.qsize():
            bdh = p.qsize()
        s = p.qsize()
        for _ in xrange(s):
            cur = p.get()
            if cur.left is not None:
                p.put(cur.left)
            if cur.right is not None:
                p.put(cur.right)
    return bdh
# get the depth in recursive way
def depthOfTreeRecursive(root):
    if root is None:
        return 0
    return max(depthOfTree(root.left),depthOfTree(root.right)) + 1  

# is a balance tree or not
def isBalanced(root):
    if root is None:
        return True
    if abs(depthOfTreeRecursive(root.left)-depthOfTreeRecursive(root.right)) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)
#check whether the tree structure is symmetric
def isSymmetric(root):
    if root is None or (root is not None and root.left is None and root.right is None):
        return True
    stack= []
    stack.append(root)
    while len(stack)!=0:
        nums,st= [],[]
        for node in stack:
            if node.left is not None:
                st.append(node.left)
                nums.append(str(node.left.val))
            else:
                nums.append("")
            if node.right is not None:
                st.append(node.right)
                nums.append(str(node.right.val))
            else:
                nums.append("")
        for i in range(len(nums)/2):
            if nums[i] != nums[-i-1]:
                return False
        stack = st
    return True
# validate p q is the same in structure and node value
def isSameTree(self,p,q):
    if p is None or q is None:
        return p == q
    sp,sq = [], []
    while (p is not None and q is not None) or (len(sp)!= 0 and len(sq)!=0):
        while p is not None and q is not None:
            if p.val == q.val:
                sp.append(p)
                sq.append(q)
                p = p.left
                q = q.left
            else:
                return False
        if p!= q:
            return False
        p = sp.pop()
        p = p.right
        q = sq.pop()
        q = q.right
    return True
