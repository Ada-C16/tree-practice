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

    def add_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)

        if key < current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)

        # This returns the root_node
        # current_node never changes during this series of recursive calls
        return current_node

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)
       

    def find_helper(self, current, key):
        # Reached a leaf, nothing here
        if current == None:
            return None
        # We found the value!
        elif current.key == key:
            return current.value
        # Search to the left of the current node
        elif key < current.key:
            return self.find_helper(current.left, key)
        # Search to the right of the current node
        return self.find_helper(current.right, key)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def find(self, key):
        return self.find_helper(self.root, key)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder_helper(self, current, result):
        if current:
            # left 
            self.inorder_helper(current.left, result)
            # current
            result.append({"key": current.key, "value": current.value})
            # right
            self.inorder_helper(current.right, result)

        return result

    def inorder(self):
        tree = []
        return self.inorder_helper(self.root, tree)

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder_helper(self, current, tree):
        if current:
            # current
            tree.append({"key": current.key, "value": current.value})
            # left
            self.preorder_helper(current.left, tree)
            # right
            self.preorder_helper(current.right, tree)
        return tree

    def preorder(self):
        tree = []
        return self.preorder_helper(self.root, tree)

    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def postorder_helper(self, current, tree):
        if current:
            #left
            self.postorder_helper(current.left, tree)
            #right
            self.postorder_helper(current.right, tree)
            #current
            tree.append({"key": current.key, "value": current.value})

        return tree

    def postorder(self):
        tree = []
        return self.postorder_helper(self.root, tree)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height_counter(self, current):
        if not current:
            return 0

        return(max(self.height_counter(current.left), self.height_counter(current.right))) + 1

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
