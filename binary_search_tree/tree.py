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

    #----------------------- ADD ----------------------
    #from from class video 👇🏼
    def add_helper(self, current, key, value):
        if current == None:
            return TreeNode(key, value)
        elif current.key >= key:
            current.left = self.add_helper(current.left, key, value)
        else: 
            current.right = self.add_helper(current.right, key, value)
        return current 
    #from from class video 👆🏼

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):

        if self.root is None:
            self.root = TreeNode(key, value)
            return
        self.add_helper(self.root, key, value)

    #----------------------- FIND ----------------------
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def find_helper(self, current, key):
        if current.key == key:
            return current.value
        if current.key >= key:
            if not current.left:
                return None
            return self.find_helper(current.left, key)
        if not current.right:
            return None
        return self.find_helper(current.right, key)
    
    def find(self, key):
        if self.root == None:
            return None
        return self.find_helper(self.root, key)
        
    #----------------------- IN ORDER ----------------------
    # Time Complexity: O(log n)
    # Space Complexity: O(log n) 
    def inorder_helper(self, current, result):
        if current != None:
            self.inorder_helper(current.left, result)
            result.append({"key":current.key, "value": current.value})
            self.inorder_helper(current.right, result)
        return result
    
    def inorder(self):
        result = []
        return self.inorder_helper(self.root, result)

    #----------------------- PRE ORDER ----------------------
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)    
    def preorder_helper(self, current, result):
        if current != None:
            result.append({"key":current.key, "value": current.value})
            self.preorder_helper(current.left, result)
            self.preorder_helper(current.right, result)
        return result
    
    def preorder(self):
        result = []
        return self.preorder_helper(self.root, result)

    #----------------------- POST ORDER ----------------------
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)  
    def postorder_helper(self, current, result):
        if current != None:
            self.postorder_helper(current.left, result)
            self.postorder_helper(current.right, result)
            result.append({"key":current.key, "value": current.value})
        return result

    def postorder(self):
        result = []
        return self.postorder_helper(self.root, result)
    
    #----------------------- HEIGHT ----------------------
    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def height_helper(self, current,):
        height = 0
        
        if current:
            height = max(self.height_helper(current.left), self.height_helper(current.right)) + 1
        return height

    def height(self):
        return self.height_helper(self.root)

    #----------------------- OPTIONAL ----------------------
#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        return []
        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"