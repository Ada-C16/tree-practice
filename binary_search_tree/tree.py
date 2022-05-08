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

    def add_helper(self, current_root, new_node):
      if current_root is None:
          return new_node
      if new_node.key < current_root.key:
          current_root.left = self.add_helper(current_root.left, new_node)
      else:
          current_root.right = self.add_helper(current_root.right, new_node)
      return current_root
      
    def find_helper (self, key, current_node):
        if current_node == None:
            return None
        if current_node.key == key:
            return current_node.value
        if key < current_node.key:
            return self.find_helper(key, current_node.left)
        if key > current_node.key:
            return self.find_helper(key, current_node.right)
    
    def inorder_helper(self, current, items):
        if current is not None:
            self.inorder_helper(current.left, items)
            items.append({"key": current.key, "value":current.value})
            self.inorder_helper(current.right, items)
        return items
    
    def preorder_helper(self, items, current_node):
        if current_node is not None: 
            items.append({"key": current_node.key, "value":current_node.value})
            self.preorder_helper(items,current_node.left)
            self.preorder_helper(items,current_node.right)
        return items

    def postorder_helper(self, items, current_node):
        if current_node is not None: 
            self.postorder_helper(items,current_node.left)
            self.postorder_helper(items,current_node.right)
            items.append({"key": current_node.key, "value":current_node.value})
        return items

    def height_helper(self, current_node):
        if current_node is None:
            return 0
        return 1 + max(self.height_helper(current_node.left), self.height_helper(current_node.right)) 

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def add(self, key, value = None):
      new_node = TreeNode (key, value)
      if self.root is None:
          self.root = new_node
          return
      self.add_helper(self.root, new_node)
 
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root == None:
            return None
        return self.find_helper(key, self.root)

    # Time Complexity:O(n)
    # Space Complexity:O(n)
    def inorder(self): 
        # //take them and make it flat as array, start in root and visit left and when it is none, store in array
        # and pop it
        if self.root == None:
           return []
        items = []
        return self.inorder_helper(self.root, items)

    # Time Complexity:O(n)
    # Space Complexity:O(n)  
    # root, left, right  
    def preorder(self):
       items = []
       if self.root == None:
           return []
       return self.preorder_helper(items, self.root)

    # Time Complexity:O(n)
    # Space Complexity:O(n)    
    def postorder(self):
        # children will go in left then parent
       items = []
       if self.root == None:
           return []
       return self.postorder_helper(items, self.root)

    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def height(self):
        return self.height_helper(self.root)
    
#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

    
#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
