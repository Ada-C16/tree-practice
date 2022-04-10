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
    # Space Complexity: O(log n) because there are log n function calls in the stack?
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
        else:
            self.helper_add(key, value, self.root)

    def helper_add(self, key, value, current):
        if key < current.key:
            if current.left == None:
                current.left = TreeNode(key, value)
                return
            else:
                self.helper_add(key, value, current.left)
        else:
            if current.right == None:
                current.right = TreeNode(key, value)
                return
            else:
                self.helper_add(key, value, current.right)

    # Time Complexity: O(log n)
    # Space Complexity: O(log n) because there are log n function calls in the stack?
    def find(self, key):
        if self.root == None:
            return None
        else:
            return self.helper_find(key, self.root)

    def helper_find(self, key, current):
        if key == current.key:
            return current.value
        elif key < current.key:
            if current.left == None:
                return None
            else:
                return self.helper_find(key, current.left)
        else:
            if current.right == None:
                return None
            else:
                return self.helper_find(key, current.right)


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        result = []
        self.helper_inorder(self.root, result)
        return result

    def helper_inorder(self, current, result):
        if current == None:
            return
        elif current.left == None and current.right == None:
            result.append({"key": current.key, "value": current.value})
        else:
            self.helper_inorder(current.left, result)
            result.append({"key": current.key, "value": current.value})
            self.helper_inorder(current.right, result)

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def preorder(self):
        result = []
        self.helper_preorder(self.root, result)
        return result
    
    def helper_preorder(self, current, result):
        if current == None:
            return
        elif current.left == None and current.right == None:
            result.append({"key": current.key, "value": current.value})
        else:
            result.append({"key": current.key, "value": current.value})
            self.helper_preorder(current.left, result)
            self.helper_preorder(current.right, result)


    # Time Complexity: O(n)
    # Space Complexity: O(n) 
    def postorder(self):
        result = []
        self.helper_postorder(self.root, result)
        return result

    def helper_postorder(self, current, result):
        if current == None:
            return
        elif current.left == None and current.right == None:
            result.append({"key": current.key, "value": current.value})
        else:
            self.helper_postorder(current.left, result)
            self.helper_postorder(current.right, result)
            result.append({"key": current.key, "value": current.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n) because there are n function calls on the stack? 
    def height(self):
        max_height = [0]
        current_height = 0
        self.helper_height(self.root, max_height, current_height)
        return max_height[0]

    def helper_height(self, current, max_height, current_height):
        if current == None:
            return
        elif current.left == None and current.right == None:
            current_height += 1
            max_height[0] = max(current_height, max_height[0])
        else:
            current_height += 1
            self.helper_height(current.left, max_height, current_height)
            self.helper_height(current.right, max_height, current_height)



#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
