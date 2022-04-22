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
    def __init__(self, root=None):
        self.root = root
    def add_helper(self, current, key, value):
        if current == None:
            return TreeNode(key, value)
        elif current.key >= key:
            current.left = self.add_helper(current.left, key, value)
        else:
            current.right = self.add_helper(current.right, key, value)
        return current
    # Time Complexity: 0(log n)
    # Space Complexity: 0(log n)
    def add(self, key, value =None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.add_helper(self.root, key, value)

    # Time Complexity: 0(log n)
    # Space Complexity: 0(log n)
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

    # Time Complexity: 0(n)
    # Space Complexity: 0(n)
    def inorder_helper(self, current, items):
        if current is not None:
            self.inorder_helper(current.left, items)
            items.append({"key": current.key, "value": current.value})
            self.inorder_helper(current.right, items)
    
    def inorder(self):
        items = []

        self.inorder_helper(self.root, items)

        return items

    # Time Complexity: O(n)
    # Space Complexity: 0(n)
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
        

    # Time Complexity: 0(n)
    # Space Complexity:0(n)
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

    # Time Complexity: 0(log n)
    # Space Complexity: 0(log n) 
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
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
