from xml.etree.ElementPath import find


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

    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def add(self, key, value = None):        
        if not self.root:
            self.root = TreeNode(key, value)
            return
        new_node = TreeNode(key, value)
        current = self.root
        while current: 
            if new_node.key < current.key:
                if current.left == None:
                    current.left = new_node
                    return
                else:
                    current = current.left 
            else: 
                if current.right == None:
                    current.right = new_node
                    return
                else:
                    current = current.right


    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None     

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        values = []
        self.inorder_helper(self.root, values)
        return values


    # Time Complexity: O(n)
    # Space Complexity: O(n)   
    def preorder(self):
        values = []
        self.preorder_helper(self.root, values)
        return values

    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def postorder(self):
        values = []
        self.postorder_helper(self.root, values)
        return values

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"

#  # Helper Functions
    def inorder_helper(self, current, values):
        if current is None:
            return values
        self.inorder_helper(current.left, values)
        values.append({
            "key": current.key,
            "value": current.value
        })
        self.inorder_helper(current.right, values)
        return values


    def preorder_helper(self, current, values):
        if current is None:
            return values
        
        values.append({
            "key": current.key,
            "value": current.value
        })
        self.preorder_helper(current.left, values)
        self.preorder_helper(current.right, values)
        return values


    def postorder_helper(self, current, values):
        if current is None:
            return values
        self.postorder_helper(current.left, values)
        self.postorder_helper(current.right, values)
        values.append({
            "key": current.key,
            "value": current.value
        })
        return values 


    def height_helper(self, current):
        if current == None:
            return 0
        left_height = self.height_helper(current.left)
        right_height = self.height_helper(current.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1