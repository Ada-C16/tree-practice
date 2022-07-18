class TreeNode:
    def __init__(self, key, val=None):

        """
        key is used to compare values
        value can be any kind of object
        """

        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n) if ordered, O(n) if unordered
    # Space Complexity: O(1)
    def add(self, key, value=None):
        node = TreeNode(key, value)
        if self.root is None:
            self.root = node
            return

        current = self.root
        while current:
            if current.key > key:
                # go left
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                # go right
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right

    # Time Complexity: O(log n) if ordered, O(n) if unordered
    # Space Complexity: O(1)
    def find(self, key):
        if self.root is None:
            return None

        if self.root.key == key:
            return self.root.value

        current = self.root
        while current:
            if key < current.key:
                if not current.left:
                    return None
                elif current.left.key == key:
                    return current.left.value
                current = current.left
            else:
                if not current.right:
                    return None
                elif current.right.key == key:
                    return current.right.value
                current = current.right

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        node_list = []
        current = self.root
        if current == None:
            return node_list

        while current:
            node_list.insert(0, {"key": current.key, "value": current.value})
            current = current.left

        current = self.root.right
        while current:
            node_list.append({"key": current.key, "value": current.value})
            current = current.right

        return node_list

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        node_list = []
        current = self.root
        if current == None:
            return node_list
        while current:
            node_list.append({"key": current.key, "value": current.value})
            current = current.left

        current = self.root.right
        while current:
            node_list.append({"key": current.key, "value": current.value})
            current = current.right
        return node_list

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        node_list = []
        current = self.root
        if current == None:
            return node_list
        self.postorder_helper(current, node_list)
        return node_list

    def postorder_helper(self, current, node_list):
        if current:
            self.postorder_helper(current.left, node_list)
            self.postorder_helper(current.right, node_list)
            node_list.append({"key": current.key, "value": current.value})
        return node_list

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height(self):
        current = self.root

        if current is None:
            return 0

        return self.height_helper(current)

    def height_helper(self, current):
        if current is None:
            return 0

        left_height = self.height_helper(current.left)
        right_height = self.height_helper(current.right)

        return max(left_height, right_height) + 1

    # ======================================================================================

    #   # Optional Method
    #   # Time Complexity:
    #   # Space Complexity:
    def bfs(self):
        pass

    #   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
