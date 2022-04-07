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

    # Time Complexity:
    # Space Complexity:
    def find(self, key):
        pass

    def inorder_helper(self, current_root, items):
        if current_root is not None:
            self.inorder_helper(current_root.left, items)
            items.append({"key": current_root.key,
                         "value": current_root.value})
            self.inorder_helper(current_root.right, items)

    # Time Complexity:
    # Space Complexity:
    def inorder(self):
        items = []

        self.inorder_helper(self.root, items)
        return items

    # Time Complexity:
    # Space Complexity:
    def preorder(self):
        # Root
        # Left
        # Right
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
