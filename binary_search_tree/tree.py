class TreeNode:
    def __init__(self, key, val=None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add_helper(self, current, key, value):
        if current == None:
            return TreeNode(key, value)
        elif current.key >= key:
            current.left = self.add_helper(current.left, key, value)
        else:
            current.right = self.add_helper(current.right, key, value)
        return current

    def add(self, key, value=None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity:
    # Space Complexity:
    def find_helper(self, current, key):
        if current.key == key:
            return current.value
        if current.key >= key:
            if not current.left:
                return None
            else:
                return self.find_helper(current.left, key)
        else:
            if not current.right:
                return None
            else:
                return self.find_helper(current.right, key)

    def find(self, key):
        if self.root == None:
            return None
        else:
            return self.find_helper(self.root, key)

    def inorder_helper(self, current, items):
        if current is not None:
            self.inorder_helper(current.left, items)
            items.append({"key": current.key, "value": current.value})
            self.inorder_helper(current.right, items)

    # Time Complexity:
    # Space Complexity:
    def inorder(self):
        items = []

        self.inorder_helper(self.root, items)

        return items

    # Time Complexity:
    # Space Complexity:
    def preorder_helper(self, current, items):
        if current is not None:
            items.append({"key": current.key, "value": current.value})
            self.preorder_helper(current.left, items)
            self.preorder_helper(current.right, items)

    def preorder(self):
        items = []

        self.preorder_helper(self.root, items)

        return items

    # Time Complexity:
    # Space Complexity:
    def postorder_helper(self, current, items):
        if current is not None:
            self.postorder_helper(current.left, items)
            self.postorder_helper(current.right, items)
            items.append({"key": current.key, "value": current.value})

    def postorder(self):
        items = []

        self.postorder_helper(self.root, items)

        return items

    # Time Complexity:
    # Space Complexity:
    def height(self):
        current = self.root
        if current == None:
            return 0
        else:
            right_tree = Tree(current.right)
            left_tree = Tree(current.left)
            return 1 + max(right_tree.height(), left_tree.height())

#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:

    def bfs(self):
        pass


#   # Useful for printing

    def to_s(self):
        return f"{self.inorder()}"
