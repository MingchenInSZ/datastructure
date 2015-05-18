class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self,value=""):
        self.head = Node(value)
    
    def insert(self,value):
        p ,pre= self.head.next,self.head
        while p is not None:
            pre = p
            p = p.next
        pre.next = Node(value)
        pre.next.next = None
    def isEmpty(self):
        if self.head.next is None:
            return True
        return False
    def getLength(self):
        p ,l= self.head.next,0
        while p is not None:
            l += 1
            p = p.next
        return l
    def delete(self,value):
        p, pre = self.head.next,self.head
        while p is not None and p.value !=value:
            pre = p
            p = p.next
        if p is not None:
            pre.next = p.next
    def getitems(self):
        p,items = self.head.next,[]
        while p is not None :
            items.append(p.value) 
            p = p.next
        return items
    def hasValue(self,value):
        p = self.head.next
        while p is not None and p.value!=value:
            p = p.next
        if p is not None and p.value == value:
            return True
        return False
    def clear(self):
        self.head.next = None

class DoubleNode:
    def __init__(self,value):
        self.pre = None
        self.next = None
        self.value = value
class DoubleLinkedList:
    def __init__(self,value=""):
        self.head = DoubleNode(value)
        self.head.pre = self.head
        
    def insert(self,value):
        node = DoubleNode(value)
        self.head.pre.next = node
        node.pre = self.head.pre
        node.next = self.head
        self.head.pre = node
        
    def delete(self,value):
        p = self.head.next
        while p != self.head and p.value!=value:
            p = p.next
        if p!=self.head:
            p.pre.next = p.next
            p.next.pre = p.pre
    def getLength(self):
        p,l=self.head.next,0
        while p!=self.head:
            l += 1
            p = p.next
        return l
    def hasValue(self,value):
        p = self.head.next
        while p !=self.head and p.value != value:
            p = p.next
        if p != self.head:
            return True
        return False 
            
    def getItems(self):
        p ,nums= self.head.next,[]
        while p != self.head:
            nums.append(p.value)
            p = p.next
        return nums
        
        
        
            
            