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
            
        # else:
        #     parent = None
        #     current = self.root
        #     while current !=  None:
        #         parent = current
        #         if key <= current.key:
        #             current = current.right
        #         else:
        #             current = current.left
        #     if parent.key > key:
        #         parent.left = TreeNode(key, value)       
          
    
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
    def inorder(self):
        pass

    # Time Complexity: 0(n)
    # Space Complexity: 0(n)    
    def preorder(self):
        pass

    # Time Complexity: 0(n)
    # Space Complexity: 0(n)    
    def postorder(self): 
        pass

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        pass


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
