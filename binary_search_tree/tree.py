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

    def add(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
            return

        new_node = TreeNode(key, value)
        self.add_helper(self.root, new_node)

    # Time Complexity: if tree is balanced O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        node = TreeNode(key, value)
        if self.root is None:
            self.root = node
            return

        current = self.root

        while current:
            if current.key > key:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right

    # Time Complexity: if tree is balanced O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        current = self.root

        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    def inorder_helper(self, current_node, items):
        if current_node is not None:
            self.inorder_helper(current_node.left, items)
            items.append({ "key": current_node.key, "value": current_node.value })
            self.inorder_helper(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []
        self.inorder_helper(self.root, items)

        return items

    def preorder_helper(self, current_node, items):
        if current_node is not None:
            items.append({ "key": current_node.key, "value": current_node.value })
            self.preorder_helper(current_node.left, items)
            self.preorder_helper(current_node.right, items)


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)

        return items

    def postorder_helper(self, current_node, items):
        if current_node is not None:
            self.postorder_helper(current_node.left, items)
            self.postorder_helper(current_node.right, items)
            items.append({ "key": current_node.key, "value": current_node.value })

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)

        return items

    def height_helper(self, current_node):
        if current_node is not None:
            height_left = self.height_helper(current_node.left)
            height_right = self.height_helper(current_node.right)
            return (max(height_left, height_right) +1)
        else:
            return 0

    # Time Complexity: O(n)
    # Space Complexity: O(n)  if balanced O(log n)
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
