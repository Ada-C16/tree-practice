class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, tree_node = None):
        self.root = tree_node
    
    def add_helper(self, current_node, new_node):
        if current_node == None: 
            return new_node

        elif new_node.key < current_node.key: 
            current_node.left = self.add_helper(current_node.left, new_node)
        else:
            current_node.right = self.add_helper(current_node.right, new_node)
        
        return current_node
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)

        if self.root == None: 
            self.root = new_node
            return self.root

        self.add_helper(self.root, new_node)

    def find_helper(self, current_node, key):
        if current_node == None: 
            return None 

        if current_node.key == key: 
            return current_node.value

        if current_node.key > key: 
            return self.find_helper(current_node.left, key)
        else: 
            return self.find_helper(current_node.right, key)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None: 
            return None
        
        return self.find_helper(self.root, key)

    def inorder_helper(self, current_node, items):
        if current_node != None: 
            self.inorder_helper(current_node.left, items)
            items.append({"key": current_node.key, "value": current_node.value})
            self.inorder_helper(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []

        self.inorder_helper(self.root, items)

        return items

    def preorder_helper(self, current_node, items):
        if current_node != None: 
            items.append({"key": current_node.key, "value": current_node.value})
            self.preorder_helper(current_node.left, items)
            self.preorder_helper(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity:  O(n)   
    def preorder(self):
        items = []

        self.preorder_helper(self.root, items)

        return items

    def postorder_helper(self, current_node, items):
        if current_node != None: 
            self.postorder_helper(current_node.left, items)
            self.postorder_helper(current_node.right, items)    
            items.append({"key": current_node.key, "value": current_node.value})  

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        items = []

        self.postorder_helper(self.root, items)

        return items

    # Time Complexity: O(n)
    # Space Complexity: O(n)   
            
    def height_helper(self, current_node):
        if current_node == None: 
            return 0

        left_tree_height = self.height_helper(current_node.left)
        right_tree_height = self.height_helper(current_node.right)
        return max(left_tree_height, right_tree_height) + 1

    def height(self):
        if self.root == None: 
            return -1

        return self.height_helper(self.root)
            

#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        result = []
        queue = []

        if self.root == None:
            return result
        
        result.append({"key": self.root.key, "value": self.root.value})
        queue.append(self.root)

        while len(queue) != 0:
            current_node = queue[0]
            
            if current_node.left != None: 
                result.append({"key": current_node.left.key, "value": current_node.left.value})
                queue.append(current_node.left)

            if current_node.right != None:
                result.append({"key": current_node.right.key, "value": current_node.right.value})
                queue.append(current_node.right)

            del queue[0]

        return result

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
