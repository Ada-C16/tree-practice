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

    def add_helper_function(self, current, next):
        if next.key < current.key:
            if not current.left:
                current.left = next
                return
            self.add_helper_function(current.left, next)
        else:
            if not current.right:
                current.right = next
                return
            self.add_helper_function(current.right, next)

    def add(self, key, value = None):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            new_node = TreeNode(key, value)
            self.add_helper_function(self.root, new_node)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)

 
    def find(self, key):
        current = self.root

        while current:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)


    def inorder_helper_function(self, current, node_values):
        if not current:
            return node_values

        self.inorder_helper_function(current.left, node_values)
        node_values.append({ 
            "key": current.key,
            "value": current.value
        })
        self.inorder_helper_function(current.right, node_values)

        return node_values
    
    def inorder(self):
        values = []
        return self.inorder_helper_function(self.root, values)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)

  
    def preorder_helper_function(self, current, node_values):
        if not current:
            return node_values

        node_values.append({ 
            "key": current.key,
            "value": current.value
        })
        self.preorder_helper_function(current.left, node_values)        
        self.preorder_helper_function(current.right, node_values)

        return node_values

    def preorder(self):
        values = []
        return self.preorder_helper_function(self.root, values)        

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)


    def postorder_helper_function(self, current, node_values):
        if not current:
            return node_values

        self.postorder_helper_function(current.left, node_values)        
        self.postorder_helper_function(current.right, node_values)
        node_values.append({ 
            "key": current.key,
            "value": current.value
        })

        return node_values

    def postorder(self):
        values = []
        return self.postorder_helper_function(self.root, values)
        

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    
    
    def height_helper(self, current):
        if not current:
            return 0

        return max(self.height_helper(current.left), self.height_helper(current.right)) + 1
    
    def height(self):
        return self.height_helper(self.root)        
