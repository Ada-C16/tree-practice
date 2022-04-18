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
        
    def add_helper(self, current_node,key,value):
        if current_node == None:
            return TreeNode(key,value)
        if key <= current_node.key:
            current_node.left = self.add_helper(current_node.left, key, value)
        else:
            current_node.right = self.add_helper(current_node.right, key, value)
        return current_node

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key,value)
        else:
            self.add_helper(self.root,key,value)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        current = self.root
        while current is not None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left
        return None

    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def inorder_helper(self, current,output):
        if current:
            self.inorder_helper(current.left,output)
            output.append({"key":current.key, "value":current.value})
            self.inorder_helper(current.right,output)
        return output
    
    def inorder(self):
        output = []
        return self.inorder_helper(self.root,output)

    # Time Complexity: O(n) 
    # Space Complexity: O(n)  
    def preorder_helper(self, current,output):
        if current:
            output.append({"key":current.key, "value":current.value})
            self.preorder_helper(current.left,output)
            self.preorder_helper(current.right,output)
        return output     
    def preorder(self):
        output = []
        return self.preorder_helper(self.root,output)

    # Time Complexity: O(n) 
    # Space Complexity: O(n) 
    def postorder_helper(self, current,output):
        if current:
            self.postorder_helper(current.left,output)
            self.postorder_helper(current.right,output)
            output.append({"key":current.key, "value":current.value})
        return output
        
    def postorder(self):
        output = []
        return self.postorder_helper(self.root,output)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def height_helper(self, current):
        if current is None:
            return 0
        lheight = self.height_helper(current.left)
        rheight = self.height_helper(current.right)
        if (lheight > rheight):
            return lheight + 1
        else:
            return rheight + 1 
            
    def height(self):
        return self.height_helper(self.root)

#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity:O(n) 
    def bfs(self):
        if self.root is None:
            return []
        node = self.root
        queue = [node]
        output = []
        while queue:
            node = queue.pop(0)
            output.append({"key":node.key, "value":node.value})
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return output

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
