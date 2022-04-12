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
        if current_root == None:
            return new_node
        if new_node.key < current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        else:
            current_root.right = self.add_helper(current_root.right, new_node)
        return current_root

    # Time Complexity:  O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)

        if self.root is None:
            self.root = new_node
            return
        self.add_helper(self.root, new_node)
        

    def find_helper(self, current, key):
        if current == None:
            return None
        elif current.key == key:
            return current.value
        elif current.key > key:
            return self.find_helper(current.left, key)
        elif current.key < key:
            return self.find_helper(current.right, key)

    # Time Complexity: O(log n) -- Assuming it's balanced
    # Space Complexity: O(log n)
    def find(self, key):
        if  self.root == None:
            return None
        return self.find_helper(self.root, key)
        

    def inorder_helper(self, current, items):
        if current != None:
            self.inorder_helper(current.left, items)
            items.append({"key": current.key, "value": current.value})
            self.inorder_helper(current.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []
        self.inorder_helper(self.root, items)
        return items

    def preorder_helper(self, current, items):
        if current != None:
            items.append({"key": current.key, "value": current.value})
            self.preorder_helper(current.left, items)
            self.preorder_helper(current.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items

    def postorder_helper(self, current, items):
        if current != None:
            self.postorder_helper(current.left, items)
            self.postorder_helper(current.right, items)
            items.append({"key": current.key, "value": current.value})

    # Time Complexity: O(n) 
    # Space Complexity: O(n)  
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        return items

    def height_helper(self, current):
        if current != None:
            height = max(self.height_helper(current.left), self.height_helper(current.right))
            return height + 1
        else: 
            return 0

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def height(self):
        if self.root is None:
            return 0
        return self.height_helper(self.root)
        
        
    def bfs_helper(self, current, to_visit):
        if current.left != None:
            to_visit.append(current.left)
        if current.right != None:
            to_visit.append(current.right)
    
#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        items = []
        to_visit = []

        if self.root == None:
            return items

        items.append({"key": self.root.key, "value": self.root.value})
        self.bfs_helper(self.root, to_visit)

        while to_visit: 
            current = to_visit.pop(0)
            items.append({"key": current.key, "value": current.value})
            self.bfs_helper(current, to_visit)
        return items








        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
