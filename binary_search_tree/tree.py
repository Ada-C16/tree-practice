from queue import Queue

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

    # Time Complexity: O(log n) - looping solution if tree is balanced
    # Space Complexity: O(1) - looping solution
    # def add(self, key, value = None):
    #     # Looping solution
    #     node = TreeNode(key, val=None)
    #     if self.root is None:
    #         self.root = node
    #         return

    #     current = self.root

    #     while current:
    #         if current.key > key:
    #             # Go left
    #             if current.left is None:
    #                 # Add node to the left
    #                 current.left = node
    #                 return
    #             else:
    #                 current = current.left
    #         else:
    #             # Go right
    #             if current.right is None:
    #                 # Add the node on the right
    #                 current.right = node
    #                 return
    #             else:
    #                 current = current.right

    def add_helper(self, current_root, new_node):
        if current_root is None:
            return new_node
        
        if new_node.key <= current_root.key:
            current_root.left = self.add_helper(current_root.left, new_node)
        else:
            current_root.right = self.add_helper(current_root.right, new_node)
        
        return current_root

    # Time Complexity: O(log n) - if tree is balanced, O(n) - if unbalanced
    # Space Complexity: O(log n) - if tree is balanced, O(n) - if unbalanced
    def add(self, key, value = None):
        # Recursive solution
        node = TreeNode(key, value)
        if self.root is None:
            self.root = node
            return

        self.add_helper(self.root, node)

    def find_helper(self, current_node, key):
        if current_node.key == key:
            return current_node.value
        elif current_node.key >= key:
            if current_node.left:
                return self.find_helper(current_node.left, key)
        else:
            if current_node.right:
                return self.find_helper(current_node.right, key)
        
        return None

    # Time Complexity: O(log n) - if tree is balanced, O(n) - if unbalanced
    # Space Complexity: O(log n) - if tree is balanced, O(n) - if unbalanced
    def find(self, key):
        if self.root is None:
            return None

        return self.find_helper(self.root, key)

    def inorder_helper(self, current_node, items):
        if current_node is not None:
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
        if current_node is not None:
            items.append({"key": current_node.key, "value": current_node.value})
            self.preorder_helper(current_node.left, items)
            self.preorder_helper(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)   
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)

        return items

    def postorder_helper(self, current_node, items):
        if current_node is not None:
            self.postorder_helper(current_node.left, items)
            self.postorder_helper(current_node.right, items)
            items.append({"key": current_node.key, "value": current_node.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)

        return items
    
    def height_helper(self, current_node):
        if current_node:
            height_left = self.height_helper(current_node.left)
            height_right = self.height_helper(current_node.right)
            return (max(height_left, height_right) + 1)
        else:
            return 0

    # Time Complexity: O(n)
    # Space Complexity: not balanced - O(n), balanced - O(log n)     
    def height(self):
        return self.height_helper(self.root)


#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        if self.root is None:
            return []
        
        items = []
        q = Queue(maxsize=0)
        q.put(self.root)

        while not q.empty():
            current_node = q.get()
            if current_node.left:
                q.put(current_node.left)
            if current_node.right:
                q.put(current_node.right)
            items.append({"key": current_node.key, "value": current_node.value})
            
        return items

        # Alternative method using list instead of importing Queue:
        # def bfs(self):
        #     if self.root is None:
        #         return []
            
        #     items = []
        #     q = [self.root]

        #     while q:
        #         current_node = q.pop(0)
        #         if current_node.left:
        #             q.append(current_node.left)
        #         if current_node.right:
        #             q.append(current_node.right)
        #         items.append({"key": current_node.key, "value": current_node.value})
            
        #     return items    


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
