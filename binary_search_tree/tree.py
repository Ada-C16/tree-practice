from unittest import result


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

    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)
        
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(logn)
    # Space Complexity: O(logn)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left
        return None

    def inorder_helper(self, current, items):
        if current != None:
            self.inorder_helper(current.left, items)
            items.append({"key": current.key, "value": current.value})
            self.inorder_helper(current.right, items)

    # Time Complexity: O(logn)
    # Space Complexity: O(logn)
    def inorder(self):
        items = []
        self.inorder_helper(self.root, items)
        return items

    def preorder_helper(self, current, items):
        if current != None:
            items.append({"key": current.key, "value": current.value})
            self.preorder_helper(current.left, items)
            self.preorder_helper(current.right, items)

    # Time Complexity: O(logn)
    # Space Complexity: O(logn)   
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items

    def postorder_helper(self, current, items):
        if current != None:
            self.postorder_helper(current.left, items)
            self.postorder_helper(current.right, items)
            items.append({"key": current.key, "value": current.value})

    # Time Complexity: O(logn)  
    # Space Complexity: O(logn)  
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        return items

    def height_helper(self, current):
        if current == None:
            return 0
        else:
            return max(self.height_helper(current.left), self.height_helper(current.right)) + 1

    # Time Complexity: O(logn)
    # Space Complexity: O(1)?    
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
