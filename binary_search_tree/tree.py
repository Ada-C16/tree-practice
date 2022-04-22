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

    def add_helper (self, current, key, value):
        if current == None:
            return TreeNode(key, value)
        elif current.key >= key:
            current.left = self.add_helper(current.left, key, value)
        else: 
            current.right = self.add_helper(current.right, key, value)
        return current 
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value=None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
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
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def find(self, key):
        if self.root == None:
            return None
        else:
            return self.find_helper(self.root, key)
    def inorder_helper(self, current, result):
        if current:
            # left 
            self.inorder_helper(current.left, result)
            # current
            result.append({"key": current.key, "value": current.value})
            # right
            self.inorder_helper(current.right, result)

        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        tree = []
        return self.inorder_helper(self.root, tree)

    def preorder_helper(self, current, tree):
        if current:
            # current
            tree.append({"key": current.key, "value": current.value})
            # left
            self.preorder_helper(current.left, tree)
            # right
            self.preorder_helper(current.right, tree)
        return tree

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder(self):
        tree = []
        return self.preorder_helper(self.root, tree)

    def postorder_helper(self, current, tree):
        if current:
            #left
            self.postorder_helper(current.left, tree)
            #right
            self.postorder_helper(current.right, tree)
            #current
            tree.append({"key": current.key, "value": current.value})

        return tree

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        tree = []
        return self.postorder_helper(self.root, tree)
    def height_counter(self, current):
        if not current:
            return 0

        return(max(self.height_counter(current.left), self.height_counter(current.right))) + 1

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def height(self):
        return self.height_counter(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        values = []
        queue = []

        if self.root:
            queue.append(self.root)

        while len(queue) > 0:
            # Current becomes what was first item in queue
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            values.append({
                "key": current.key,
                "value": current.value,
            })

        return values

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
