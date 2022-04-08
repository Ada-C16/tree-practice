class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        else:
            return 1


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        node = TreeNode(key, value)
        # if no root
        if self.root is None:
            self.root = node
            
        else:
            parent = None
            current = self.root
            while current != None:
                parent = current
                if current.key > key:
                    current = current.left
                else:
                    current = current.right
            
            if parent.key > key:
                parent.left = node

            else:
                parent.right = node
        


    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        # no tree
        if self.root is None:
            return 
        parent = None
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None


    def inorder_helper(self, current, items):
        if current is not None:
            self.inorder_helper(current.left, items)
            items.append({"key": current.key, "value": current.value})
            self.inorder_helper(current.right, items)
    
    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        items = []
        self.inorder_helper(self.root, items)
        return items
        

    def preorder_helper(self, current, items):
        if current is not None:
            items.append({"key": current.key, "value": current.value})
            self.preorder_helper(current.left, items)
            self.preorder_helper(current.right, items)
    # Time Complexity: 
    # Space Complexity:     
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items
        

    
    def postorder_helper(self, current, items):
        if current is not None:
            self.postorder_helper(current.left, items)
            self.postorder_helper(current.right, items)
            items.append({"key": current.key, "value": current.value})

    # Time Complexity: 
    # Space Complexity:     
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        return items

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        if self.root:
            return self.root.height()
        else:
            return 0


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
