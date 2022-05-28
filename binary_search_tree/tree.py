from multiprocessing.dummy import current_process
from typing import ItemsView


class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: 0(log n)
    # Space Complexity: 0(log n) 
    def add_helper(self, current_node, key, value):
        # helper takes advantage of recursive
        # if node is empty, return new node with key and value
        if current_node == None:
            return TreeNode(key, value)
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value) 
        return current_node
            
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
            

    # Time Complexity: 0(log n)
    # Space Complexity: 0(log n)
    def find(self, key):
        if self.root == None:
            return None
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif current.key <key:
                current = current.right
            else:
                current = current.left
        return None


    # Time Complexity: 0(n)
    # Space Complexity: 0(n)
    def inorder_helper(self, current_node, items):
        if current_node != None:
            self.inorder_helper(current_node.left, items)
            items.append({"key": current_node.key, "value": current_node.value})
            self.inorder_helper(current_node.right, items)
        
    def inorder(self):
        #list of items to be returned --> depth-first traversal sorted key values in an ascending order, Left,Current,Right
        items = []
        self.inorder_helper(self.root, items)
        return items


    # Time Complexity: 0(n)
    # Space Complexity: 0(n)   
    def preorder_helper(self, current_node, items):
        if current_node == None:
            return items
        else:
            items.append({"key": current_node.key, "value": current_node.value})
            self.preorder_helper(current_node.left, items)
            self.preorder_helper(current_node.right, items)
            return items
     
    def preorder(self):
        #list of items to be returned --> depth-first traversal sorted current, left, right
        items = []
        if self.root:
            self.preorder_helper(self.root, items)
        return items


    # Time Complexity: 0(n)
    # Space Complexity: 0(n)  
    def postorder_helper(self, current_node, items): 
        if current_node:
            self.postorder_helper(current_node.left, items)
            self.postorder_helper(current_node.right, items)
            items.append({"key": current_node.key, "value": current_node.value})
        return items
      
    def postorder(self): 
        #list of items to be returned --> depth-first traversal sorted left, right, current
        items = []
        if self.root:
            self.postorder_helper(self.root, items)
        return items


    # Time Complexity: 0(n)
    # Space Complexity: 0(n)  
    def height_helper(self, current_node):
        # uses stack and recursion for each node in tree 
        # plus one for the root node / the current node
        if current_node != None:
            height_left = self.height_helper(current_node.left)
            height_right = self.height_helper(current_node.right)
            return (max(height_left, height_right) + 1)
        
        else:
            return 0
         
    def height(self):
        return self.height_helper(self.root)



#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)

    def bfs_helper(self, current_node, sub_list):
        if current_node.left:
            sub_list.append(current_node.left)
        if current_node.right:
            sub_list.append(current_node.right)
        
    
    def bfs(self):
        # uses queues to create sublists for each level, pops off elements from queue from left to right until sublist is empty to creates list, then adds children of each element to queue as popping off, repeats,
        # recursion for each level
        items = []
        sub_list = []
        
        if not self.root:
            return items
        
        items.append({"key": self.root.key, "value": self.root.value})
        self.bfs_helper(self.root, sub_list)
        
        while sub_list:
            current_node = sub_list.pop(0)
            items.append({"key": current_node.key, "value": current_node.value})
            self.bfs_helper(current_node, sub_list)
        return items
    

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
