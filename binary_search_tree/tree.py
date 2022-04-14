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

    # Time Complexity: O(log n)
    # Space Complexity: O(1) 
    def add(self, key, value = None):

        if self.root is None:
            self.root = TreeNode(key, value)
            return

        new_node = TreeNode(key, value)
        self.add_helper(self.root, new_node)

    def find_helper(self, current_root, key):
        if current_root.key == key:
            return current_root.value
        
        if  key < current_root.key:
            if current_root.left is None:
                return None
            return self.find_helper(current_root.left, key)

        if key > current_root.key:
            if current_root.right is None:
                return None
            return self.find_helper(current_root.right, key)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        if self.root is None:
            return None

        return self.find_helper(self.root, key)

    def inorder_helper(self, current_node, items):

        if current_node is not None:

            self.inorder_helper(current_node.left, items)
            items.append({"key": current_node.key, "value": current_node.value})
            self.inorder_helper(current_node.right, items)

    # This method returns an array of all the elements in the tree, in order
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []
        self.inorder_helper(self.root,items)
        return items

    def preorder_helper(self, current_node, items):

        if current_node is None:
            return
        
        items.append({"key": current_node.key, "value": current_node.value})

        self.preorder_helper(current_node.left, items)
        self.preorder_helper(current_node.right, items)

    # This method returns an array of all the elements in a preorder fashion (root, left, right)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def preorder(self):
        items = []
        self.preorder_helper(self.root, items)
        return items

    def postorder_helper(self, current_node, items):
        if current_node is None:
            return
        
        self.postorder_helper(current_node.left, items)
        self.postorder_helper(current_node.right, items)



        items.append({"key": current_node.key, "value": current_node.value})

    # This method returns an array of all the elements in a postorder fashion (left, right , root)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        items = []
        self.postorder_helper(self.root, items)
        return items

    def height_helper(self, current_node):
        if current_node is not None:
            height_left = self.height_helper(current_node.left)
            height_right = self.height_helper(current_node.right)
            return max(height_left, height_right) + 1
        
        else:
            return 0


    # This method returns the height of the binary search tree
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height(self):
        return self.height_helper(self.root)

#   # Optional Method
#   # This method returns an array with the tree elements in a level-by-level order
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
