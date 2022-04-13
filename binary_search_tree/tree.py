class TreeNode:
    def __init__(self, key, val=None):
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

    # Time Complexity: O(log(n))
    # Space Complexity: O(log(n))

    def add(self, key, value=None):
        new_node = TreeNode(key, value)

        if self.root == None:
            self.root = new_node
            return
        self.add_helper(self.root, new_node)

    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def find(self, key):
        if self.root is None:
            return None

        current_root = self.root

        while current_root is not None:
            if current_root.key == key:
                return current_root.value
            elif current_root.key > key:
                current_root = current_root.left
            else:
                current_root = current_root.right
        return None

    def inorder_helper(self, current_root, items):
        if current_root is not None:
            self.inorder_helper(current_root.left, items)
            items.append({"key": current_root.key,
                         "value": current_root.value})
            self.inorder_helper(current_root.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []

        self.inorder_helper(self.root, items)
        return items

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder_helper(self, current_root, items):
        if current_root is not None:
            items.append({"key": current_root.key,
                         "value": current_root.value})
            self.preorder_helper(current_root.left, items)
            self.preorder_helper(current_root.right, items)

    def preorder(self):
        # Root
        # Left
        # Right
        items = []

        self.preorder_helper(self.root, items)
        return items

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def postorder_helper(self, current_root, items):
        if current_root is not None:
            self.postorder_helper(current_root.left, items)
            self.postorder_helper(current_root.right, items)
            items.append({"key": current_root.key,
                         "value": current_root.value})

    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        return items

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height_helper(self, current_root):
        if current_root is None:
            return 0
        return 1 + max(self.height_helper(current_root.left), self.height_helper(current_root.right))

    def height(self):
        if self.root is None:
            return 0
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:

    def bfs(self):
        pass


#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"
