class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class AVLTreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.height = 0
        
class TrieNode:
    def __init__(self,label=""):
        self.children = [None]*26
        self.words = 0
        self.label = label
