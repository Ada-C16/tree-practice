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

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        node = TreeNode(key, value)
        if self.root is None:
            self.root = node
            return self
        
        current = self.root
        while current:
            if current.key > key:
                # Go left
                if current.left is None:
                    current.left = node
                    return self
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return self
                else:
                    current = current.right

    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        if self.root is None:
            return None
        if self.root.key == key:
            return self.root.value
        
        current = self.root
        while current:
            if key < current.key:
                if not current.left:
                    return None
                elif current.left.key == key:
                    return current.left.value
                else:
                    current = current.left
            else:
                if not current.right:
                    return None
                elif current.right.key == key:
                    return current.right.value
                else:
                    current = current.right
                    
    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        pass

    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        pass

    # Time Complexity: 
    # Space Complexity:     
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
