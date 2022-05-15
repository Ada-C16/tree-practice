from logging import root
import queue


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

    # Time Complexity: O(log(n)) if the tree is balanced
    # Space Complexity: O(1) (only one node is being added)
    def add_helper(self, current_root, new_node):
        if current_root == None:
            return new_node

        if new_node.key < current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        else:
            current_root.right = self.add_helper(current_root.right, new_node)

        return current_root
    
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key, value)
            return self.root

        new_node = TreeNode(key, value)
        self.add_helper(self.root, new_node)

    # def add(self, key, value = None):
    #     node = TreeNode(key, value)

    #     if self.root == None:
    #         self.root = node
    #         return self.root
        
    #     current = self.root

    #     while current:
    #         if key < current.key:
    #             # Go left
    #             if current.left == None:
    #                 # Add node to the left
    #                 current.left = node
    #                 return self.root
    #             else:
    #                 # Travel down to that side of the tree
    #                 current = current.left
    #         else:
    #             # Go right
    #             if current.right == None:
    #                 # Add node on the right
    #                 current.right = node
    #                 return self.root
    #             else:
    #                 # Travel down to that side of the tree
    #                 current = current.right
    

    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    def find_helper(self, current_root, key):
        if current_root == None:
            return None
        
        if key < current_root.key:
            return self.find_helper(current_root.left, key)
            # Remember: passing current_root.left as first parameter makes it a "root"
        elif key > current_root.key:
            return self.find_helper(current_root.right, key)
        else:
            return current_root.value
    
    def find(self, key):
        if self.root == None:
            return None
        
        result = self.find_helper(self.root, key)
        return result

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder_helper(self, current_node, items):
        if current_node != None:
            self.inorder_helper(current_node.left, items)
            items.append({"key": current_node.key, "value": current_node.value})
            self.inorder_helper(current_node.right, items)
    
    def inorder(self):
        items = []

        if self.root == None:
            return items

        self.inorder_helper(self.root, items)
        
        return items

    # Time Complexity: O(n)
    # Space Complexity: O(n)   
    def preorder_helper(self, current_node, items):
        if current_node != None:
            items.append({"key": current_node.key, "value": current_node.value})
            self.preorder_helper(current_node.left, items)
            self.preorder_helper(current_node.right, items)
            
    
    def preorder(self):
        items = []

        if self.root == None:
            return items
        
        self.preorder_helper(self.root, items)

        return items

    # Time Complexity: 
    # Space Complexity:     
    def postorder_helper(self, current_node, items):
        if current_node != None:
            self.postorder_helper(current_node.left, items)
            self.postorder_helper(current_node.right, items)
            items.append({"key": current_node.key, "value": current_node.value})
            
    
    def postorder(self):
        items = []

        if self.root == None:
            return items
        
        self.postorder_helper(self.root, items)

        return items

    # Time Complexity: O(n)
    # Space Complexity: O(1)  
    def height_helper(self, node):
        if node == None:
            return 0
        
        left_height = self.height_helper(node.left)
        right_height = self.height_helper(node.right)

        return 1 + max(left_height, right_height)
    
    def height(self):
        if self.root == None:
            return 0

        current_node = self.root

        tree_height = self.height_helper(current_node)

        return tree_height


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        items = []
        
        if self.root == None:
            return items
        
        items = [self.root]
        queue = [{"key": self.root.key, "value": self.root.value}]
        # queue = []
        
        while items:
            node = items.pop(0)

            if node.left:
                queue.append({"key": node.left.key, "value": node.left.value})
            
            if node.right:
                queue.append({"key": node.right.key, "value": node.right.value})
        
        return queue


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
