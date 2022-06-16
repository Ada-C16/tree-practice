from collections import deque
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

    # Time Complexity: 
    # Space Complexity: 
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if self.root is None:
            self.root = new_node
            return self.root
        return self.add_helper(self.root, new_node)

    def add_helper(self, curr, new_node):
        if curr is None:
            curr = new_node
        elif new_node.key < curr.key:
            curr.left = self.add_helper(curr.left, new_node)
        else:
            curr.right = self.add_helper(curr.right, new_node)
        return curr

    # Time Complexity: 
    # Space Complexity: 
    def find(self, key):
        return self.find_helper(self.root, key)

    def find_helper(self, curr, key):
        if curr is None:
            return None
        if curr.key == key:
            return curr.value
        if key < curr.key:
            return self.find_helper(curr.left, key)
        return self.find_helper(curr.right, key)

    # Time Complexity: 
    # Space Complexity: 
    def inorder(self):
        arr = []
        self.inorder_helper(self.root, arr)
        return arr

    def inorder_helper(self, curr, arr):
        if curr is not None:
            self.inorder_helper(curr.left, arr)
            arr.append({"key": curr.key, "value": curr.value})
            self.inorder_helper(curr.right, arr)

    # Time Complexity:
    # Space Complexity:     
    def preorder(self):
        arr = []
        self.preorder_helper(self.root, arr)
        return arr

    def preorder_helper(self, curr, arr):
        if curr is not None:
            arr.append({"key": curr.key, "value": curr.value})
            self.preorder_helper(curr.left, arr)
            self.preorder_helper(curr.right, arr)
    # Time Complexity:
    # Space Complexity:     
    def postorder(self):
        arr = []
        self.postorder_helper(self.root, arr)
        return arr

    def postorder_helper(self, curr, arr):
        if curr is not None:
            self.postorder_helper(curr.left, arr)
            self.postorder_helper(curr.right, arr)
            arr.append({"key": curr.key, "value": curr.value})

    # Time Complexity: 
    # Space Complexity:     
    def height(self):
        return self.height_helper(self.root, 0)

    def height_helper(self, curr, count):
        if curr is None:
            return count
        left_height = self.height_helper(curr.left, count + 1)
        right_height = self.height_helper(curr.right, count + 1)
        return max(left_height, right_height)

    # Optional Method
    # Time Complexity:
    # Space Complexity:
    def bfs(self):
        visited = []
        if self.root is None:
            return visited
        q = deque()
        q.append(self.root)
        while q:
            curr = q.popleft()
            visited.append({"key": curr.key, "value": curr.value})
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        return visited



#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
