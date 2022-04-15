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

    # Time Complexity: O(n), balance tree = O(log n)
    # Space Complexity: O(1)
    def add(self, key, value=None):
        new_node = TreeNode(key, value)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if current.key > new_node.key:
                    # going left
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = new_node
                        return

                else:
                    # going right
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = new_node
                        return

    # Time Complexity: O(n), balance tree = O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        current = self.root
        while current is not None:
            if current.key == key:
                return current.value
            elif current.key > key:
                current = current.left
            else:
                current = current.right

        return None

    # Time Complexity: O(n)
    # Space Complexity: O(n) - if balanced O(log n), recursion uses stack space
    def inorder(self):
        return self.inorder_helper(self.root)

    def inorder_helper(self, current, output=[]):
        if current is None:
            return output
        self.inorder_helper(current.left, output)
        output.append({"key": current.key, "value": current.value})
        self.inorder_helper(current.right, output)
        return output

    # Time Complexity: O(n)
    # Space Complexity: O(n) - if balanced O(log n), recursion uses stack space
    def preorder(self):
        return self.preorder_helper(self.root)

    def preorder_helper(self, current, output=[]):
        if current is None:
            return output
        output.append({"key": current.key, "value": current.value})
        self.preorder_helper(current.left, output)
        self.preorder_helper(current.right, output)
        return output

    # Time Complexity: O(n)
    # Space Complexity: O(n) - if balanced O(log n), recursion uses stack space
    def postorder(self):
        return self.postorder_helper(self.root)

    def postorder_helper(self, current, output=[]):
        if current is None:
            return output
        self.postorder_helper(current.left, output)
        self.postorder_helper(current.right, output)
        output.append({"key": current.key, "value": current.value})
        return output

    # Time Complexity: O(n)
    # Space Complexity: O(n) - if balanced O(log n)
    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, current):
        if current is None:
            return 0
        return max(self.height_helper(current.left), self.height_helper(current.right)) + 1

#   # Optional Method
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def bfs(self):
        if self.root is None:
            return []

        output = []
        queue = [self.root]

        while len(queue):
            node = queue.pop(0)  # should be called dequeue()
            output.append({"key": node.key, "value": node.value})
            if node.left:
                queue.append(node.left)  # should be called enqueue()
            if node.right:
                queue.append(node.right)  # should be called enqueue()

        return output


#   # Useful for printing


    def to_s(self):
        return f"{self.inorder()}"
