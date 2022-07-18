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

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
            return
        current = self.root
        while current != None:
            if current.key == key:
                current.value = value
                return
            elif current.key > key:
                if current.left == None:
                    current.left = TreeNode(key, value)
                    return
                current = current.left
            else:
                if current.right == None:
                    current.right = TreeNode(key, value)
                    return
                current = current.right
        

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def find(self, key):

        if self.root == None:
            return None

        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif current.key > key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_helper(self, current_node, items):
        if current_node is None:
            return []

        self.inorder_helper(current_node.left, items)
        items.append({"key": current_node.key, "value": current_node.value})
        self.inorder_helper(current_node.right, items)


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):

        if self.root == None:
            return []
        
        items = []
        self.inorder_helper(self.root, items)
        return items

    def preorder_helper(self, current_node, items):
        if current_node is None:
            return []

        items.append({"key": current_node.key, "value": current_node.value})
        self.preorder_helper(current_node.left, items)
        self.preorder_helper(current_node.right, items)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def preorder(self):
        if self.root == None:
            return []

        items = []
        self.preorder_helper(self.root, items)
        return items

    def postorder_helper(self, current_node, items):
        if current_node is None:
            return []

        self.postorder_helper(current_node.left, items)
        self.postorder_helper(current_node.right, items)
        items.append({"key": current_node.key, "value": current_node.value})


    # Time Complexity: O(log n)
    # Space Complexity: O(log n) 
    def postorder(self):
        if self.root == None:
            return []

        items = []
        self.postorder_helper(self.root, items)
        return items


    def height_helper(self, current_node):
        if current_node is None:
            return 0
        left_height = self.height_helper(current_node.left)
        right_height = self.height_helper(current_node.right)
        return max(left_height, right_height) + 1


    # Time Complexity: O(log n)
    # Space Complexity: O(log n)  
    def height(self):
        if self.root == None:
            return 0

        return self.height_helper(self.root)


    def bfs_helper(self, current_node, items):
        if current_node is None:
            return []

        items.append({"key": current_node.key, "value": current_node.value})
        self.bfs_helper(current_node.left, items)
        self.bfs_helper(current_node.right, items)

#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        if self.root == None:
            return []

        items = []
        self.bfs_helper(self.root, items)
        return items


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
