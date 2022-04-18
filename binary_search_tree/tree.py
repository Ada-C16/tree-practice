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

    
    def add_helper_func(self, current_root, new_node):
        if current_root is None:
            return new_node

        if new_node.key < current_root.key:
            current_root.left = self.add_helper_func(current_root.left, new_node)
        else:
            current_root.right = self.add_helper_func(current_root.right, new_node)
 
        return current_root

    # Time Complexity: O(log n) if tree is balanced, O(n) if unbalanced
    # Space Complexity: O(1)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if self.root is None:
            self.root = new_node
            return new_node
        
        self.add_helper_func(self.root, new_node)
    

    # Time Complexity: O(log n) if tree is balanced, O(n) if unbalanced
    # Space Complexity: O(1)
    def find(self, key):
        if self.root is None:
            return None

        current = self.root

        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return None

    def inorder_helper_func(self, current_node, items):
        if current_node is not None:
            self.inorder_helper_func(current_node.left, items)
            items.append({"key": current_node.key, "value": current_node.value})
            self.inorder_helper_func(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        items = []
        self.inorder_helper_func(self.root, items)
        return items

    def preorder_helper_func(self, current_node, items):
        if current_node is not None:
            items.append({"key": current_node.key, "value": current_node.value})
            self.preorder_helper_func(current_node.left, items)
            self.preorder_helper_func(current_node.right, items)

    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def preorder(self):
        items = []
        self.preorder_helper_func(self.root, items)
        
        return items


    def postorder_helper_func(self, current_node, items):
        if current_node is not None:
            self.postorder_helper_func(current_node.left, items)
            self.postorder_helper_func(current_node.right, items)
            items.append({"key": current_node.key, "value": current_node.value})

    # Time Complexity: O(n)
    # Space Complexity: O(n)  
    def postorder(self):
        items = []
        self.postorder_helper_func(self.root, items)
        
        return items

    def height_helper_func(self, current_node, height):
        if current_node is not None:
            left= self.height_helper_func(current_node.left, height)
            right= self.height_helper_func(current_node.right, height)
            return max(left, right) + 1
        
        return 0

    # Time Complexity: O(n)
    # Space Complexity: O(1)     
    def height(self):
        height = 0
        if self.root is None:
            return height

        return self.height_helper_func(self.root, height)

    def bfs_helper_func(self, current_node):
        level_by_level = []
        q = [current_node]

        while len(q) >= 1:
            current_node = q.pop(0)

            if current_node.left is not None:
                q.append(current_node.left)
            if current_node.right is not None:
                q.append(current_node.right)
            level_by_level.append({"key": current_node.key, "value": current_node.value})
        
        return level_by_level

#   # Optional Method
#   # Time Complexity: O(n)
#   # Space Complexity: O(n)
    def bfs(self):
        if self.root is None:
            return []
        return self.bfs_helper_func(self.root)

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"