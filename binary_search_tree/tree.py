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

    # Time Complexity: O(log(n))
    # Space Complexity: O(n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
            return
        
        current = self.root
        while current != None:
            if current.key > key:
                if current.left == None:
                    current.left = TreeNode(key, value)
                    return
                else:
                    current = current.left
            else:
                if current.right == None:
                    current.right = TreeNode(key, value)
                    return
                else:
                    current = current.right
    
    # Time Complexity: o(1)
    # Space Complexity: O(n)
    # search for a node in the tree
    def find(self, key):
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif current.key > key:
                current = current.left
            else:
                current = current.right
        return None

        

    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def inorder_helper(self, current, result):
        if current == None:
            return result
        else:
            result = self.inorder_helper(current.left, result)
            result.append({"key":current.key, "value":current.value})
            result = self.inorder_helper(current.right, result)
            return result
    
    def inorder(self):
        result = []
        current = self.root
        if current == None:
            return result
        else:
            result = self.inorder_helper(current, result)
            return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder_helper(self, current, result):
        if current == None:
            return result
        else:
            result.append({"key":current.key, "value":current.value})
            result = self.preorder_helper(current.left, result)
            result = self.preorder_helper(current.right, result)
            return result
    def preorder(self):
        result = []
        current = self.root
        if current == None:
            return result
        else:
            result = self.preorder_helper(current, result)
            return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder_helper(self, current, result):
        if current == None:
            return result
        else:
            result = self.postorder_helper(current.left, result)
            result = self.postorder_helper(current.right, result)
            result.append({"key":current.key, "value":current.value})
            return result   

    def postorder(self):
        result = []
        current = self.root
        if current == None:
            return result
        else:
            result = self.postorder_helper(current, result)
            return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height_helper(self, current):
        if current == None:
            return 0
        else:
            left_height = self.height_helper(current.left)
            right_height = self.height_helper(current.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def height(self):
        current = self.root
        if current == None:
            return 0
        else:
            return self.height_helper(current)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
