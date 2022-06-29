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

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
            return

        current = self.root

        while current != None:
            if key < current.key:
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

    # Time Complexity: O(LogN)
    # Space Complexity: O(1)
    def find(self, key):
        current = self.root

        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None
    
    # This method returns an array of all the elements in the tree, in order.
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def inorder(self):
        """
        if this is null
        return
        inOrder(left)
        visit this
        inOrder(right)
        """
        current = self.root
        result = []

        return self.inorder_helper(current, result)

    def inorder_helper(self, current, result):
        if current is None:
            return result

        current.left = self.inorder_helper(current.left, result)
        result.append({"key": current.key, "value": current.value})
        current.right = self.inorder_helper(current.right, result)
        return result

    # This method returns an array of all the elements in a preorder fashion (root, left, right)
    # Time Complexity: O(N)
    # Space Complexity:  O(N)     
    def preorder(self):
        current = self.root
        result = []

        return self.preorder_helper(current, result)

    def preorder_helper(self, current, result):
        if current is None:
            return result

        result.append({"key": current.key, "value": current.value})
        current.left = self.preorder_helper(current.left, result)
        current.right = self.preorder_helper(current.right, result)

        return result
        
    # This method returns an array of all the elements in a postorder fashion (left, right , root).
    # Time Complexity: O(N)
    # Space Complexity: O(N)   
    def postorder(self):
        current = self.root
        result = []

        return self.postorder_helper(current, result)

    def postorder_helper(self, current, result):
        if current is None:
            return result

        current.left = self.postorder_helper(current.left, result)
        current.right = self.postorder_helper(current.right, result)
        result.append({"key": current.key, "value": current.value})

        return result

    # This method returns the height of the binary search tree
    # Time Complexity: O(N)
    # Space Complexity: O(N)    
    def height(self):
        height = 0
        current = self.root

        if current is None:
            return height
        
        return self.height_helper(current, height)
    
    def height_helper(self, current, height):
        if current is None:
            return height

        leftAns = self.height_helper(current.left, height)
        rightAns = self.height_helper(current.right, height)

        return max(leftAns, rightAns) + 1    
    # # Recursively call height of each node
    #     leftAns = height(self.root.left)
    #     rightAns = height(self.root.right)
 
    # # Return max(leftHeight, rightHeight) at each iteration
    #     return max(leftAns, rightAns) + 1


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
