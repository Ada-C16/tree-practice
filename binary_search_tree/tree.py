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
        if not self.root:
            self.root = node
            return self.root

        current = self.root
        previous = None
        while current:
            previous = current
            if key <= current.key:
                current = current.left
            else:
                current = current.right
        if key <= previous.key:
            previous.left = node
        else:
            previous.right = node

    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        if not self.root:
            return None
        if self.root.key == key:
            return self.root.value
        current = self.root
        while current:
            if current.key == key:
                return current.value
            if key <= current.key:
                current = current.left
            else:
                current = current.right
        return None

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
