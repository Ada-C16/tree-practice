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

    
    def add_helper(self, current_root, new_node):
        if current_root is None:
            return new_node

        if new_node.key < current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        else:
            current_root.right = self.add_helper(current_root.right, new_node)
        
        return current_root

    # Time Complexity: O(log n) if tree is balanced, O(n) if unbalanced
    # Space Complexity: O(1)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if self.root is None:
            self.root = new_node
            return new_node
        
        self.add_helper(self.root, new_node)
    

    # Time Complexity: O(log n) if tree is balanced, O(n) if unbalanced
    # Space Complexity: O(1)
    def find(self, key):
        if self.root is None:
            return None

        current = self.root

        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return None

    def inorder_helper(self, current_node, items):
        if current_node is not None:
            self.inorder_helper(current_node.left, items)
            items.append({"key": current_node.key, "value": current_node.value})
            self.inorder_helper(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []

        self.inorder_helper(self.root, items)

        return items


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
