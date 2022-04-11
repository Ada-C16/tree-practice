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

    def addHelper(self, current_root, new_node):
        if current_root is None:
            return new_node
        
        if new_node.key < current_root.key:
            current_root.left = self.addHelper(current_root.left, new_node)
        else:
            current_root.right = self.addHelper(current_root.right, new_node)

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        new_node = TreeNode(key, value)

        if self.root is None:
            self.root = new_node
            return 
        self.addHelper(self.root, new_node)

    
    def findHelper(self, current_node, key):
        if not current_node:
            return None
        if current_node.key == key:
            return current_node.value
        if current_node.key > key:
            return self.findHelper(current_node.left, key)
        if current_node.key < key:
            return self.findHelper(current_node.right, key)    

    # Time Complexity: 
    # Space Complexity:
    def find(self, key):
        #if it's empty return None
        return self.findHelper(self.root, key)

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        result = []
        if self.root.left:
            result += self.root.left.inorder()

        result.append(self.root.value)

        if self.root.right:
            result += self.root.right.inorder()

        return result

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
