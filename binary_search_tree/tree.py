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

    def add_helper(self, current, key, value):
        if current == None:
            return TreeNode(key, value)
        elif current.key >= key:
            current.left = self.add_helper(current.left, key, value)
        else:
            current.right = self.add_helper(current.right, key, value)
        return current

    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def add(self, key, value=None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity:
    # Space Complexity:
    def find(self, key):
        if self.root == None:
            return None

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
