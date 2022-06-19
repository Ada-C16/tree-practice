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

    # Time Complexity: O(log N) or O(n)
    # Space Complexity: O(n)

    def insert_node_helper(self, current_node, key, value):
        if current_node == None:
            return TreeNode(key, value)

        if key < current_node.key:
            current_node.left = self.insert_node_helper(current_node.left, key, value)
        else:
            current_node.right = self.insert_node_helper(current_node.right, key, value)
        return current_node

    def add(self, key, value = None):
        # BST is empty
        if self.root is None:
            self.root = TreeNode(key, value)

        # BST is not empty
        self.insert_node_helper(self.root, key, value)
        

    # Time Complexity: O(log N) or O(n)
    # Space Complexity: O(n) 
    def find(self, key):
        if self.root == None:
            return None
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left
        return None


    # Time Complexity: 
    # Space Complexity: 
    def inorder_helper(self, current, result):
        if current is not None:
            self.inorder_helper(current.left, result)
            result.append({'key': current.key, 'value': current.value})
            self.inorder_helper(current.right, result)
            
    def inorder(self):
        result = []
        self.inorder_helper(self.root, result)
        return result        

    # Time Complexity: 
    # Space Complexity: 
    def preorder_helper(self, current, result):
        if current:
            result.append({"key": current.key, "value": current.value}) 
            self.preorder_helper(current.left, result)
            self.preorder_helper(current.right, result)   
    def preorder(self):
        result = []
        self.preorder_helper(self.root, result)
        return result


    # Time Complexity: 
    # Space Complexity:
    def postorder_helper(self, current, result):
        if current:
            self.postorder_helper(current.left, result)
            self.postorder_helper(current.right, result)
            result.append({"key": current.key, "value": current.value})     
    def postorder(self):
        result = []
        self.postorder_helper(self.root, result)
        return result

    # Time Complexity: 
    # Space Complexity: 
    def height_helper(self, current):
        if current:
            height_left = self.height_helper(current.left)
            height_right = self.height_helper(current.right)
            return max(height_left, height_right)+1    
    def height(self):
        if self.root == None:
            return 0
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 

    def bfs(self):
        result = []

        if self.root == None:
            return result

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append({"key": current.key, "value": current.value})
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
