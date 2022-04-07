class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
    
    def get_height_helper(self):
        if self.left is None and self.right is None:
            return 1 
        elif self.left is None and self.right is not None:
            return 1 + self.right.get_height_helper()
        elif self.right is None and self.left is not None:
            return 1 + self.left.get_height_helper()
        else:
            left, right = self.left.get_height_helper(), self.right.get_height_helper()
            return 1 + max(left, right)

class Tree:
    def __init__(self):
        self.root = None

    def add_helper(self, current_root, new_node):
        # base case...
        if not current_root:
            return new_node 
        
        # recursive case...
        # check if key is <= root key; if so, insert somewhere on left side 
        if new_node.key <= current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        else: # else, insert somewhere on right side 
            current_root.right = self.add_helper(current_root.right, new_node)
        
        return current_root 

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        # if there is no root...
        if not self.root:
            self.root = TreeNode(key, value) 
            return 

        new_node = TreeNode(key, value)
        self.add_helper(self.root, new_node)

    def find_helper(self, current_root, target_key):
        # Base cases: root is null or key is present at root
        if current_root is None or current_root.key == target_key:
            return current_root 
    
        # Search left 
        if current_root.key >= target_key:
          return self.find_helper(current_root.left, target_key)  
        
        # Search right 
        return self.find_helper(current_root.right, target_key)
      
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def find(self, key):
        target_node = self.find_helper(self.root, key)

        if target_node is None:
            return None 

        return target_node.value 

    # helpers 
    def inorder_helper(self, current_node, items):
        if current_node is not None:
            self.inorder_helper(current_node.left, items) 
            items.append({ "key" : current_node.key, "value" : current_node.value })
            self.inorder_helper(current_node.right, items) 

    def preorder_helper(self, current_node, items):
        if current_node is not None:
            items.append({ "key" : current_node.key, "value" : current_node.value })
            self.preorder_helper(current_node.left, items) 
            self.preorder_helper(current_node.right, items) 
    
    def postorder_helper(self, current_node, items):
        if current_node is not None:
            self.postorder_helper(current_node.left, items) 
            self.postorder_helper(current_node.right, items) 
            items.append({ "key" : current_node.key, "value" : current_node.value })

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []
        self.inorder_helper(self.root, items)
        return items 

    # Time Complexity: O(n)
    # Space Complexity: O(n)   
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items 

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        return items

    # Time Complexity: O(n)
    # Space Complexity: O(n) or O(log n) ???
    def height(self):
        if self.root is None:
          return 0 
        return self.root.get_height_helper()
        
    def bfs_helper(self, current_node, items):
        if current_node is not None:
            queue = [current_node]
            while queue: 
                node = queue.pop(0) # pop first node off queue and append it to items
                items.append({ "key" : node.key, "value" : node.value })
                if node.left is not None: # if there's a left element, append to queue
                    queue.append(node.left)
                if node.right is not None: # if there's a right element, append to queue
                    queue.append(node.right)

#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        items = []
        self.bfs_helper(self.root, items)
        return items 

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
