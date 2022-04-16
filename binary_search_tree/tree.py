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

    # For Time and Space Complexity, I am making the assumption the tree is balanced

    # Time Complexity: O(log n) because, if the tree is balanced, then we reduce the items we look through by half with each iteration
    # Space Complexity: O(1) because we are not creating more space, in the long run
    def add(self, key, value=None):
        node = TreeNode(key, value)

        if self.root is None:
            self.root = node
            return

        self.add_helper(self.root, node)

    def add_helper(self, current, new_node):
        if current is None:
            return new_node

        if new_node.key <= current.key:
            current.left = self.add_helper(current.left, new_node)
        elif new_node.key > current.key:
            current.right = self.add_helper(current.right, new_node)

        return current

    # Time Complexity: O(log n) because we cut our search in half each pass through
    # Space Complexity:  O(1)
    def find(self, key):
        current = self.root
        if current is None:
            return None

        while current != None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right

    # Time Complexity: O(n) since we visit every node to collect the value of it and append it
    # Space Complexity:O(n) since we create & increase the size of the array we return
    def inorder(self):
        current = self.root
        arr = []

        if current is None:
            return arr

        return self.inorder_helper(current, arr)

    def inorder_helper(self, current, arr):
        if current is None:
            return arr

        current.left = self.inorder_helper(current.left, arr)
        arr.append({"key": current.key, "value": current.value})
        current.right = self.inorder_helper(current.right, arr)

        return arr

    # Time Complexity: O(n)
    # Space Complexity:O(n)
    def preorder(self):
        current = self.root
        arr = []

        if current is None:
            return arr

        return self.preorder_helper(current, arr)

    def preorder_helper(self, current, arr):
        if current is None:
            return arr

        arr.append({"key": current.key, "value": current.value})
        current.left = self.preorder_helper(current.left, arr)
        current.right = self.preorder_helper(current.right, arr)

        return arr

    # Time Complexity: O(n)
    # Space Complexity:O(n)
    def postorder(self):
        current = self.root
        arr = []

        if current is None:
            return arr

        return self.postorder_helper(current, arr)

    def postorder_helper(self, current, arr):
        if current is None:
            return arr

        current.left = self.postorder_helper(current.left, arr)
        current.right = self.postorder_helper(current.right, arr)
        arr.append({"key": current.key, "value": current.value})

        return arr

    # Time Complexity: O(n) since we visit every node
    # Space Complexity:O(1) since we are not creating or modifying any data structures
    def height(self):
        height = 0
        current = self.root

        if current is None:
            return height

        return self.height_helper(current, height)

    def height_helper(self, current, height):
        if current is None:
            return height

        left = self.height_helper(current.left, height)
        right = self.height_helper(current.right, height)

        return max(left, right) + 1


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:


    def bfs(self):
        pass


#   # Useful for printing


    def to_s(self):
        return f"{self.inorder()}"
