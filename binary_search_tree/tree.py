from regex import R


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
        if current_root is None:
            return new_node

        if new_node.key < current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        else:
            current_root.right = self.add_helper(current_root.right, new_node)
        return current_root

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value=None):
        new_node = TreeNode(key, value)

        if self.root is None:
            self.root = new_node
            return
        self.add_helper(self.root, new_node)

    # Time Complexity: O(1)
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

    ####

    def inorder_helper(self, current, items):
        if current is not None:
            self.inorder_helper(current.left, items)
            items.append({"key": current.key, "value": current.value})
            self.inorder_helper(current.right, items)

    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def inorder(self):
        items = []

        self.inorder_helper(self.root, items)

        return items

    # Time Complexity: O(1)
    # Space Complexity:  O(n)

    def preorder_helper(self, current, items):
        if current is not None:
            # Root
            items.append({"key": current.key, "value": current.value})
            # Left
            self.preorder_helper(current.left, items)
            # Right
            self.preorder_helper(current.right, items)

    def preorder(self):
        items = []

        self.preorder_helper(self.root, items)

        return items

    # Time Complexity: O(1)
    # Space Complexity: O(n)

    def postorder_helper(self, current, items):
        if current is not None:
            # Left
            self.postorder_helper(current.left, items)
            # Right
            self.postorder_helper(current.right, items)
            # Rootcd
            items.append({"key": current.key, "value": current.value})

    def postorder(self):

        items = []

        self.postorder_helper(self.root, items)

        return items

    def height_helper(self, current):
        if current is None:
            return 0

        return 1 + max(self.height_helper(current.left), self.height_helper(current.right))

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height(self):
        if self is None:
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
