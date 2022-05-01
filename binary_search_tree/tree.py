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

    def add_helper(self, current_node, key, value):
        if current_node is None:
            return TreeNode(key, value)

        if key < current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(
                current_node.right, key, value
            )

        return current_node

    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def add(self, key, value=None):

        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    def find_helper(self, current, key):
        if current is None:
            return None

        elif current.key == key:
            return current.value

        elif key < current.key:
            return self.find_helper(current.left, key)

        return self.find_helper(current.right, key)

    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def find(self, key):
        return self.find_helper(self.root, key)

    def inorder_helper(self, current, result):

        if current:
            self.inorder_helper(current.left, result)
            result.append({"key": current.key, "value": current.value})
            self.inorder_helper(current.right, result)

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        tree = []
        return self.inorder_helper(self.root, tree)

    def preorder_helper(self, current, tree):
        if current:
            tree.append({"key": current.key, "value": current.value})
            self.preorder_helper(current.left, tree)
            self.preorder_helper(current.right, tree)
        return tree

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        tree = []
        return self.preorder_helper(self.root, tree)

    def postorder_helper(self, current, tree):
        if current:
            self.postorder_helper(current.left, tree)
            self.postorder_helper(current.right, tree)
            tree.append({"key": current.key, "value": current.value})

        return tree

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        tree = []
        return self.postorder_helper(self.root, tree)

    def height_helper(self, current):
        if not current:
            return 0

        return (
            max(
                self.height_helper(current.left),
                self.height_helper(current.right),
            )
        ) + 1

    def height(self):
        return self.height_helper(self.root)

    # #   # Optional Method
    # #   # Time Complexity:
    # #   # Space Complexity:
    # def bfs(self):
    #     pass

    # #   # Useful for printing
    # def to_s(self):
    #     return f"{self.inorder()}"
