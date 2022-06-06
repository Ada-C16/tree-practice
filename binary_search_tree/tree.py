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

    # Time Complexity: O(log N) or O(n)
    # Space Complexity: O(n)

    def insert_node_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)

        if key < current_node.key:
            current_node.left = self.insert_node_helper(current_node.left, key, value)
        else:
            current_node.right = self.insert_node_helper(current_node.right, key, value)
        return current_node

    def add(self, key, value = None):
        # BST is empty
        if self.root is None:
            self.root = TreeNode(key, value)

        # BST is not empty
        self.insert_node_helper(self.root, key, value)
        

    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        pass

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
