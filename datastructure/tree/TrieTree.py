from BinaryTreeNode import TrieNode
class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        i ,p= 0,self.root
        while i < len(word):
            ind = ord(word[i]) - 97
            if p.children[ind] is None:
                p.children[ind] = TrieNode(word[i])
            i += 1
            p = p.children[ind]
        p.words += 1
        self.root.words += 1
        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        i,p = 0, self.root
        while i< len(word):
            ind = ord(word[i]) - 97
            if p.children[ind] is None:
                return False
            else:
                i += 1
                p = p.children[ind]
        if p.words > 0: 
            return True
        return False
        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):  
        i,p = 0, self.root
        while i< len(prefix):
            ind = ord(prefix[i]) - 97
            if p.children[ind] is None:
                return False
            else:
                i += 1
                p = p.children[ind] 
        return True

                
        
        
        
        
        